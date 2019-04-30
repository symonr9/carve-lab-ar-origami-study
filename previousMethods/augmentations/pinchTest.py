import viz
import vizinfo
import vizact
import math
import vizshape

from config import * 

viz.setMultiSample(4)
viz.fov(60)
viz.go()

viz.MainView.move([5,0,-25])


#sphere = vizshape.addSphere(radius=1); 
#sphere.setPosition([0, 0, 0]); 

ar = viz.add('./ar/artoolkit.dle');
camera = ar.addWebCamera();

marker = camera.addMatrixMarker(47, width=1000); #id works for 0-63
endMarker = camera.addMatrixMarker(40, width=1000); #id works for 0-63


current = 1;
def main():
	if marker.getVisible():
		current = 0;
		print "MARKER:" + str(marker.getPosition());
		baseValueX1 = marker.getPosition(0)[0]; #this denotes the X position
		baseValueY1 = marker.getPosition(0)[1]; #this denotes the Y position
		baseValueZ1 = marker.getPosition(0)[2]; #this denotes the Z position
		
		pinch = viz.addChild('thesis/niceHand_5.dae');
		scaleSize = 0.5;
		pinch.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		pinch.setEuler([90,0,0]);
		pinch.setPosition([baseValueX1, baseValueY1, baseValueZ1]);
		markerLink = viz.link(marker,pinch);



vizact.ontimer(0,main);

