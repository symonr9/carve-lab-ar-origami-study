import viz
import vizinfo
import vizact
import math
import vizshape

from config import * 


viz.setMultiSample(4)
viz.fov(60)
viz.go()


#Add the ground plane
#ground = viz.addChild('ground.osgb')

viz.MainView.move([5,0,-25])

#this function stores quadratic points of an equation into an array. 
def setPositionsQuadratic(array, numPositions, X, Y, Z, endX, endY, endZ, constant=0):
	Coe = numPositions;
	
	selector = "Y:zero";
	if endY > 0: 
		selector  = "Y:positive";
	elif endY < 0: 
		selector = "Y:negetive";
	
	
	if float(abs(endX) - abs(X)) == 0:
		denominator = 1;
	else:
		denominator = float(abs(endX) - abs(X));
		
	angle = math.atan(float(abs(endY) - abs(Y))/denominator);
	
	print "angle: " + str(angle);
	print "selector: " + selector;
	for p in range(numPositions+1): #for each position as specified in the parameter
		if selector == "Y:zero":
			X = (float(p)/float(numPositions))*endX; #X would need to stay consistently rising 
			Y = -p**2+Coe*p+constant;
			Z = (float(p)/float(numPositions))*endZ;
		elif selector == "Y:positive":
			#X=tcos(ø)-f(t)sin(ø) 
			#Y=tsin(ø)+f(t)cos(ø)
			X = p*math.cos(angle) - (-p**2+Coe*p+constant)*math.sin(angle); #troubleshooting: I wasn't using f(t) here, which was giving me problems 
			Y = p*math.sin(angle) + (-p**2+Coe*p+constant)*math.cos(angle);
			Z = (float(p)/float(numPositions))*endZ;
		elif selector == "Y:negetive":
			#X=tcos(ø)-f(t)sin(ø) 
			#Y=tsin(ø)+f(t)cos(ø)
			X = p*math.cos(angle) - (-p**2+Coe*p+constant)*math.sin(angle); #troubleshooting: I wasn't using f(t) here, which was giving me problems 
			Y = -p*math.sin(angle) - (-p**2+Coe*p+constant)*math.cos(angle);
			Z = (float(p)/float(numPositions))*endZ;
			
		pos = [X,Y,Z]; #store data point into variable
		array.append(pos); #append data point onto the end of the array
		print str(p) +  ": [" + str(X)+  ", " + str(Y)+  ", " + str(Z) + "]";
	return array;
		
#this function stores quadratic points of an equation into an array. 
def setPositionsLinear(array, numPositions, X, Y, Z, endX, endY, endZ, constant=0):
	#global baseValueX1, baseValueY1, baseValueZ1; #from config.py
	#pos = [X,Y,Z]; #store data point into variable
	#rray.append(pos); #append data point onto the end of the array
	
	for p in range(numPositions+1): #for each position as specified in the parameter
		X = (float(p)/float(numPositions))*endX;
		Y = (float(p)/float(numPositions))*endY;
		Z = (float(p)/float(numPositions))*endZ;
		
		pos = [X,Y,Z]; #store data point into variable
		array.append(pos); #append data point onto the end of the array
		
		print str(p) +  ": [" + str(X)+  ", " + str(Y)+  ", " + str(Z) + "]";
	return array;
	
#this function draws an arrow based on the array of points given.
def DrawArrow(positions, parabolaHeight):
	global pathSpeed; #from config file
	
	arrow = viz.addChild('thesis/greenArrow.dae'); #import the arrow .dae object
	#arrow = viz.addChild('thesis/niceHand_1.dae');
	scaleSize = parabolaHeight * 0.1;
	arrow.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
	
	path = viz.addAnimationPath(); #create an animation path

	for x,pos in enumerate(positions): #for every position in the array (x = pos)
		a = viz.addChild('beachball.osgb', cache=viz.CACHE_CLONE); #add a control point object
		a.setPosition(pos); #set the object at the position specified
		a.alpha(0.5); #make it almost invisible
		path.addControlPoint(x+1, pos=pos); #add it onto the path
		
	path.setSpeed(pathSpeed); #set the speed of the path
	path.setLoopMode(viz.LOOP); #set the path on a loop

	path.computeTangents(); #compute the tangents 
	path.setAutoRotate(viz.ON); #set it to auto rotate
	viz.link(path, arrow); #link the path to the arrow object so that the arrow will move
	path.play(); #play the animation


#Execution: 

positions = [];

parabolaHeight = 8; #controls the height of the parabola 
#parabolaHeight = numPositions; #so yeah, the parabola height should be the num of positions so that the proportion is correct 

#Test Suite: 
#[30,0,0] GOOD 
#[10,0,10] GOOD 
#[10,5,10] X: 8.944, Y: 4.472
#[10,-5,10] X: 8.944, Y: -4.472
#[10,10,10] X: 7.07, Y: 7.07
#[10,-10,10] X: 7.07, Y: -7.07
#[-10,0,10] GOOD
#[-10,-5,10] X: 8.944, Y: -4.472
#[-10,-6,10] X: 8.575, Y: -5.145

endValueX1 = 10; 
endValueY1 = 5; 
endValueZ1 = 10;

#the location of [baseValueX1, baseValueY1, baseValueZ1] is the first marker and [endValueX1, endValueY1, endValueZ1]

sphere = vizshape.addSphere(radius=1); 
#sphere = viz.addChild('thesis/niceHand_1.dae');
sphere.setPosition([baseValueX1, baseValueY1, baseValueZ1]); 
#sphere.setEuler(90);



sphere2 = vizshape.addSphere(radius=1); 
sphere2.setPosition([endValueX1, endValueY1, endValueZ1]); 


#positions = setPositionsLinear(positions, numPositions, baseValueX1, baseValueY1, baseValueZ1, endValueX1, endValueY1, endValueZ1);
positions = setPositionsQuadratic(positions, parabolaHeight, baseValueX1, baseValueY1, baseValueZ1, endValueX1, endValueY1, endValueZ1);

DrawArrow(positions, parabolaHeight);