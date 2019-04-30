﻿import viz
import vizinfo
import vizact
import math
import vizshape

from config import * 

viz.setMultiSample(4)
viz.fov(60)
viz.go()

sphere = vizshape.addSphere(radius=1); 
sphere.setPosition([0, 0, 0]); 

ar = viz.add('./ar/artoolkit.dle');
camera = ar.addWebCamera();

marker = camera.addMatrixMarker(47, width=1000); #id works for 0-63
endMarker = camera.addMatrixMarker(40, width=1000); #id works for 0-63

current = 1;
def main():
	global marker;
	global current;
	if marker.getVisible() and current == 1: 
		current = 0;
		print "MARKER:" + str(marker.getPosition());
		baseValueX1 = marker.getPosition(0)[0]; #this denotes the X position
		baseValueY1 = marker.getPosition(0)[1]; #this denotes the Y position
		baseValueZ1 = marker.getPosition(0)[2]; #this denotes the Z position
		
		path = viz.addAnimationPath()
		positions = [ [baseValueX1,baseValueY1,baseValueZ1]];

		endValueX1 = endMarker.getPosition()[0];
		endValueY1 = endMarker.getPosition()[1];
		endValueZ1 = endMarker.getPosition()[2];
		print "END:" + str(endValueX1) + "," + str(endValueY1) + "," + str(endValueZ1)
		
		i = 0;
		numPositions = 5;
		Coe = numPositions;
		constant = 0;
		X = baseValueX1;
		endX = endValueX1;
		Y = baseValueY1;
		endY = endValueY1;
		endZ = endValueZ1;
		Z = baseValueZ1;
		
		if float(abs(endX) - abs(X)) == 0:
			denominator = 1;
		else:
			denominator = float(abs(endX) - abs(X));
		angle = math.atan(float(abs(endY) - abs(Y))/denominator);

		for p in range(numPositions+1): #need the +1 to complete the parabolic path
			#altering p affects the end point and speed of the parabolas
			
			X = (float(p)/float(numPositions))*endX;
			Y = (float(p)/float(numPositions))*endY;
			Z = (float(p)/float(numPositions))*endZ + 10;
			print str(p) +  ": [" + str(X)+  ", " + str(Y)+  ", " + str(Z) + "]";
			positions.append([X,Y,Z]);
		
		for i in range(numPositions):
			b = viz.addChild('beachball.osgb');
			#print pos;
			b.setPosition(positions[i]);
			b.alpha(0.5);
		

vizact.ontimer(0,main);



