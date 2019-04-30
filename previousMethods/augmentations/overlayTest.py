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
	triangle = viz.addChild('thesis/triangle_1.dae');
	triangle2 = viz.addChild('thesis/triangle_1.dae');
	if marker.getVisible() and endMarker.getVisible():
		current = 0;
		print "MARKER:" + str(marker.getPosition());
		baseValueX = marker.getPosition(0)[0]; #this denotes the X position
		baseValueY = marker.getPosition(0)[1]; #this denotes the Y position
		baseValueZ = marker.getPosition(0)[2]; #this denotes the Z position
		
		scaleSize = 0.5;
		triangle.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		#pinch.setEuler([90,0,0]);
		triangle.setPosition([baseValueX, baseValueY, baseValueZ]);
		markerLink = viz.link(marker,triangle);
		
		endValueX = endMarker.getPosition(0)[0]; #this denotes the X position
		endValueY = endMarker.getPosition(0)[1]; #this denotes the Y position
		endValueZ = endMarker.getPosition(0)[2]; #this denotes the Z position
		

		scaleSize = 0.5;
		triangle2.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
		#pinch.setEuler([90,0,0]);
		triangle2.setPosition([endValueX, endValueY, endValueZ]);
		markerLink = viz.link(endMarker,triangle2);
		
		
		parametricValueX = baseValueX + endValueX;
		parametricValueY = baseValueY + endValueY; 
		parametricValueZ = baseValueZ + endValueZ;
		
		#Now I have the line (x,y,z) = (baseValueX, baseValueY, baseValueZ) + t(parametricValueX, parametricValueY, parametricValueZ)
		#where t will give me a point on the line).
		
		
		
		#next steps is to figure out what t is for the base value and the end value. 
		#For the base value, t = 0. 
		#for the end value, you get t = 1. 
		
		#so if you wanted to plot points against the line
		#with n as number of points, 
		#you would do t = 1/n, 1/n-1, 1/n-2 ... 1/n
		
		#equation is [baseValueX + parametricValueX * 1/r, baseValueY + parametricValueY * 1/r, baseValueZ + parametricValueZ * 1/r] 
		
		positions = [[baseValueX,baseValueY,baseValueZ]];
		
		n = 5;
		
		viz.startLayer(viz.LINES);
		
		for i in range(n):
			r = 1.0 / (n);
			
			newPoint = [baseValueX + parametricValueX * 2 * r, baseValueY + parametricValueY * 2 * r, baseValueZ + parametricValueZ * 2 * r];
			positions.append(newPoint);
	
			#sphere = vizshape.addSphere(radius=1); 
			#sphere.setScale(0.2);
			#sphere.setPosition(newPoint); 
			
			viz.vertex(newPoint);
			
			n = n - 1;
			print positions; 

		myLines = viz.endLayer();
		markerLink2 = viz.link(marker,myLines);
		
		
	if not marker.getVisible() or not endMarker.getVisible():
		triangle.remove();
		triangle2.remove();
		
vizact.ontimer(0,main);

