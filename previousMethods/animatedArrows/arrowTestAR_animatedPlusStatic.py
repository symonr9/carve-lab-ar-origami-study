import viz
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
		
		logo = viz.add('thesis/greenArrow.dae')
		scaleSize = 0.5;
		logo.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		logo.setEuler(270);
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
			
			X = (float(p)/float(numPositions))*endX;
			Y = (float(p)/float(numPositions))*endY;
			Z = (float(p)/float(numPositions))*endZ + 10;
			positions.append([X,Y,Z]);

		#for i in enumerate(positions): 
		#	b = viz.addChild('beachball.osgb');
		#	pathTrajectory = [];
		pathTrajectory = [];
		for x,pos in enumerate(positions):
			b = viz.addChild('beachball.osgb');
			b.setPosition(pos);
			b.alpha(0.5);
			#pathTrajectory.append(b);
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
			print "path: " + str(enumerate(pathTrajectory));
			marker_arrowPath.remove();
			arrowPath.remove();
			logo.remove();
			global current; 
			current = 1;
			
		path.addEventAtEnd('end');
		vizact.onPathEvent(path, 'end', onEndReached);

vizact.ontimer(0,main);



