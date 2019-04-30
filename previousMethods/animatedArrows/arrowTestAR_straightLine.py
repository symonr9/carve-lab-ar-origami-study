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
		
		baseValueX1 = marker.getPosition(0)[0]; #this denotes the X position
		baseValueY1 = marker.getPosition(0)[1]; #this denotes the Y position
		baseValueZ1 = marker.getPosition(0)[2]; #this denotes the Z position
		
		endValueX1 = endMarker.getPosition()[0];
		endValueY1 = endMarker.getPosition()[1];
		endValueZ1 = endMarker.getPosition()[2];
		
		arrow = viz.add('thesis/greenArrow.dae')
		scaleSize = 0.5;
		arrow.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		arrow.setEuler(90);
		arrow.setPosition([baseValueX1, baseValueY1, baseValueZ1]);
		
		positions = [ [baseValueX1,baseValueY1,baseValueZ1], [1,1,1], [2,2,2], [3,3,3], [4,4,4]];
		
		for p in range(5):
			pinch = viz.addChild('thesis/niceHand_5.dae');
			scaleSize = 0.5;
			pinch.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
			pinch.setEuler([90,0,0]);
			pinch.setPosition(positions[p]);

vizact.ontimer(0,main);



