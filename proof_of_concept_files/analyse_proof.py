import os,sys
import Image
import ImageDraw

import numpy
import math
import pylab
im = Image.open("IR_0485.jpg")

print im.bits, im.size, im.format


# sample

yRow = 155
xStart = 120
xStop = 220

'''
yRow = 228
xStart = 55
xStop = 180
'''
pixelsInt = []
pixR = []
pixG = []
pixB = []
pixels = list(im.getdata())
numpy
for x in range(xStart, xStop):
	val = pixels[yRow * 240 + x]
	print val
	pixR.append(pixels[yRow + x][0])
	pixG.append(pixels[yRow + x][1])
	pixB.append(pixels[yRow + x][2])
	#pixelsInt.append( (pixels[yRow + x][0] << 16) + (pixels[yRow + x][1] << 8) + pixels[yRow + x][2] ) 
	pixelsInt.append( val ) 

#print pixelsInt
#print range(0, 2**24+1, 1024)
#import scipy

matrixResults = numpy.empty(240 * 240).reshape(240, 240)
#matrixResults[0][0] = 1

indices = range(1, len(pixelsInt)+1)
binDistance = math.sqrt(len(indices))
binEdges = range(0, len(indices), int(binDistance))

bins = []
for i in range(0, len(binEdges)-1):
	bins.append(indices[binEdges[i]:binEdges[i+1]])

plotMatrix = []
for b in bins:
	result = numpy.mean(b)
	plotMatrix.append(result)

print len(binEdges), len(plotMatrix)
#pylab.plot(binEdges[1:], plotMatrix)

print len(indices), len(pixelsInt)
pylab.plot(indices, pixelsInt)

'''
binsAr = range(0, 2**24+1, 4096)
npA = numpy.histogram(pixelsInt, bins=binsAr)
npR = numpy.histogram(pixR, bins=binsAr)
npG = numpy.histogram(pixG, bins=binsAr)
npB = numpy.histogram(pixB, bins=binsAr)
#print np
import pylab
#print len(np[1]), len(np[0])
#np[0][len(np[0])-1] = 0
#print len(np[1]), len(np[0])
pylab.plot(npA[1][1:], npA[0])
pylab.plot(npR[1][1:], npR[0])
pylab.plot(npG[1][1:], npG[0])
pylab.plot(npB[1][1:], npB[0])
pylab.show()'''


draw = ImageDraw.Draw(im)
draw.line([(xStart, yRow),(xStop, yRow)], fill=128)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw 

im.save("tmp.jpg", "JPEG")
pylab.show()


