#!/usr/bin/env python

#import os,sys
import Image
import ImageDraw

#import numpy
#import math
import pylab

imgPath = "images/"
tmpPath = "tmp/"

im = Image.open(imgPath + "IR_0485.jpg")

print im.bits, im.size, im.format


# sample
'''
yRow = 155
xStart = 120
xStop = 220
'''

yStart = 10
yStop = 220
xStart = 170
xStop = 170

# value bar
'''
yRow = 228
xStart = 55
xStop = 180
'''

pixelsInt = []
pixels = list(im.getdata())

for x in range(xStart, xStop):
	val = pixels[yStart * 240 + x]
	pixelsInt.append(val)
	
for y in range(yStart, yStop):
	val = pixels[xStart + 240 * y]
	pixelsInt.append(val)

indices = range(1, len(pixelsInt)+1)
pylab.plot(indices, pixelsInt)

draw = ImageDraw.Draw(im)
draw.line([(xStart, yStart),(xStop, yStop)], fill=128)
del draw

im.save(tmpPath + "line.png", "PNG")
#pylab.show()
pylab.savefig(tmpPath + "graph.png")


