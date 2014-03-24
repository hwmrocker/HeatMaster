#!/usr/bin/env python

import sys, os
from PIL import Image
from PyQt4 import QtCore, QtGui
from gui.guiMaster import *
import analyse

class SignalHandler(object):
	def __init__(self, ui):
		self._ui = ui
		QtCore.QObject.connect(self._ui.cmdSelectPath, QtCore.SIGNAL("clicked()"), self.cmdSelectPath_clicked)
		QtCore.QObject.connect(self._ui.lstFiles, QtCore.SIGNAL("currentItemChanged()"), self.lstFiles_on_item_changed)
		self._ui.lblSelect.mousePressEvent = self.lblSelect_onClick_getPos

		self._ui.lstFiles.currentItemChanged.connect(self.lstFiles_on_item_changed)

		# vars
		self.selectionClick = 0
		self.coords = []

		# init foo
		self._ui.txtPath.setText(os.path.dirname(os.path.abspath(__file__)) + "/images")
		self.syncPath()

	def setImageForControl(self, control, imageFullPath):
		#use full ABSOLUTE path to the image, not relative
		print imageFullPath
		control.setPixmap(QtGui.QPixmap(imageFullPath))

	def syncPath(self):
		self._ui.lstFiles.clear()
		dirList = os.listdir(self._ui.txtPath.text())
		for fname in dirList:
			self._ui.lstFiles.addItem(fname)

	def doAnalyse(self, imgName):
		imgFullPath = str(self._ui.txtPath.text()) + "/" + imgName
		an = analyse.Analyse()
		an.analyseImage(imgFullPath, self.coords[0], self.coords[1], self.coords[2], self.coords[3])

		tmpPath = os.path.dirname(os.path.abspath(__file__)) + "/tmp/"

		self.setImageForControl(self._ui.lblSelect, tmpPath + "line.png")
		self.setImageForControl(self._ui.lblGraph, tmpPath  + "graph.png")

	def lblSelect_onClick_getPos(self , event):
		x = event.pos().x()
		y = event.pos().y()
		print x, y
		if self.selectionClick == 0:
			self.coords = []
			self.coords.append(x)
			self.coords.append(y)
			self.selectionClick += 1
		elif self.selectionClick == 1:
			self.coords.append(x)
			self.coords.append(y)
			self.selectionClick = 0
			self.doAnalyse(str(self._ui.lstFiles.currentItem().text()))

	def lstFiles_on_item_changed(self, curr, prev):
		#http://www.pythoncentral.io/pyside-pyqt-tutorial-the-qlistwidget/
		#entry.setText(curr.text())
		if not curr is None:
			#print curr.text()
			imageFullPath = os.path.join(str(self._ui.txtPath.text()), str(curr.text()))
			im = Image.open(imageFullPath)
			print im.bits, im.size, im.format

			self.setImageForControl(self._ui.lblSelect, imageFullPath)
		else:
			#TODO: clear images!
			pass

	def cmdSelectPath_clicked(self):
		dirName = str(QtGui.QFileDialog.getExistingDirectory(None, "Select Directory with DCM files", self._ui.cmdSelectPath.text()))
		self._ui.txtPath.setText(dirName)
		self.syncPath()



app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

sh = SignalHandler(ui)

MainWindow.show()
sys.exit(app.exec_())