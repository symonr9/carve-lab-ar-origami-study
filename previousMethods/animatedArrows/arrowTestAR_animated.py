import viz
import vizinfo
import vizact
import math
import vizshape

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from config import * 


viz.setMultiSample(4)
viz.fov(60)
viz.go()

sphere = vizshape.addSphere(radius=1); 
sphere.setPosition([0, 0, 0]); 

ar = viz.add('./ar/artoolkit.dle');
camera = ar.addWebCamera();

marker = camera.addMatrixMarker(47, width=1000); #id works for 0-63
endMarker = camera.addMatrixMarker(0, width=1000); #id works for 0-63

current = 1;

#Notes: Will not matter, obscuring of marker is what matters, the animation
#would still occur
def main():
	global marker;
	global current;
	if marker.getVisible() and current == 1: 
		current = 0;
		print "MARKER:" + str(marker.getPosition());
		baseValueX1 = marker.getPosition(0)[0]; #this denotes the X position
		baseValueY1 = marker.getPosition(0)[1]; #this denotes the Y position
		baseValueZ1 = marker.getPosition(0)[2]; #this denotes the Z position
		
		#pinch = viz.addChild('thesis/niceHand_5.dae');
		#scaleSize = 0.5;
		#pinch.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		#pinch.setEuler([90,0,0]);
		#pinch.setPosition([baseValueX1, baseValueY1, baseValueZ1]);
		#markerLink = viz.link(marker,pinch);		
		
		
		logo = viz.add('thesis/greenArrow.dae')
		scaleSize = 0.5;
		logo.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		logo.setEuler([0,90,0]);
		logo.setPosition([baseValueX1, baseValueY1, baseValueZ1]);
		
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
			
			X = (float(p)/float(numPositions+1))*endX;
			Y = (float(p)/float(numPositions+1))*endY;
			Z = (float(p)/float(numPositions+1))*endZ + 5;
			
			#X = p*math.cos(angle) - (-p**2+Coe*p+constant)*math.sin(angle); #troubleshooting: I wasn't using f(t) here, which was giving me problems 
			#Y = p*math.sin(angle) + (-p**2+Coe*p+constant)*math.cos(angle);
			#Z = (float(p)/float(numPositions))*endZ;
			
			#X = p*math.cos(angle) - (-p**2+Coe*p+constant)*math.sin(angle); #troubleshooting: I wasn't using f(t) here, which was giving me problems 
			#Z = p*math.sin(angle) + (-p**2+Coe*p+constant)*math.cos(angle);
			#Y = (float(p)/float(numPositions))*endZ;
			
			positions.append([X,Y,Z]);
		
		for x,pos in enumerate(positions):
			b = viz.addChild('beachball.osgb',cache=viz.CACHE_CLONE)
			b.setPosition(pos);
			b.alpha(0);
			#bpath = viz.link(path, b);
			#bpath.remove();
			#Add the control point to the animation path
			path.addControlPoint(x+1, pos=pos);
		path.setSpeed(4);
		#path.setAxisAngle(90);
		#path.setLoopMode(viz.CUBIC_BEZIER) #not good, circular isn't good either 
		path.computeTangents()
		path.setAutoRotate(viz.ON); #important - this is how the arrow is orientated along the path 	
		path.play()		
		
		arrowPath = viz.link(path, logo);
		marker_arrowPath = viz.link(marker,arrowPath);
		def onEndReached():
			marker_arrowPath.remove();
			arrowPath.remove();
			logo.remove();
			global current; 
			current = 1;
			
		path.addEventAtEnd('end');
		vizact.onPathEvent(path, 'end', onEndReached);

vizact.ontimer(0,main);



