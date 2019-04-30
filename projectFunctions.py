### Libraries #######################################################################
import viz # general viz module
import vizinfo # vizinfo is used along w/ vizinput to gather input throughout the program 
import vizshape # vizshape is used for the creation and manipulation of the box sensors and tiles. 
import math # vizmath is used for various mathematical operations used in the program.
import viztask
import vizproximity # vizproximity is used for the creation and function of all proximity sensors.
import vizinput # vizinput is used along w/ vizinfo to gather input throughout the program 
import vizconnect # Vizconnect is used for tracking the position and orientation of the head and hand. 
import hand # (From fitz test) Kept in case it was needed.
import random # Used to cycle test list.
import time	# Used for its CPU clock time function
import os.path #used to check file I/O
import VideoVision
import vizdlg
import win32api
import win32con
from threading import Timer

from config import * 

#####################################################################################



### Experiment Functions ############################################################
def nextStep():
	global testStep, currentStep, endStepNum, instructionPanel, additionalInfo, separator;
	testStep = testStep + 1;
	if testStep > endStepNum:
		testStep = 0;
	currentStep = "Step " + str(testStep);
	instructionPanel.setText(currentStep); 
	
	instructionPanel.removeItem(additionalInfo);
	instructionPanel.removeItem(separator);
	
	separator = instructionPanel.addSeparator();
	additionalInfo = instructionPanel.addLabelItem(stepCommand, viz.addText("hey"));


#####################################################################################
### Camera Functions ################################################################
	
def getCameraPosition():
	# may change in future, but currently cameras have 6cm ipd
	r_camera.setEuler(vizconnect.getTracker('optical_heading').getEuler())
	r_camera.setPosition(vizconnect.getTracker('optical_heading').getPosition() + [0.03,0,0])
	l_camera.setEuler(vizconnect.getTracker('optical_heading').getEuler())
	l_camera.setPosition(vizconnect.getTracker('optical_heading').getPosition() + [-0.03,0,0])
	
def checkVisibility(left_marker, right_marker, left_object, right_object):
	if left_marker.getVisible():
		left_object.visible(viz.ON);
	else:
		left_object.visible(viz.OFF);
	
	if right_marker.getVisible():
		right_object.visible(viz.ON);
	else: 
		right_object.visible(viz.OFF);


#Method that updates whether the marker is visible
def updateCameras():
	getCameraPosition();
	checkVisibility(l_marker, r_marker, basketball, r_m1Axes);
	

#####################################################################################


### Object Functions ##############################################################

#link together the objects to the specific markers so they show up ----------------
def linkMarkers(left_marker, right_marker, left_object, right_object):
	viz.link(left_marker, left_object);
	viz.link(right_marker, right_object);
	
def setupGround(ground):
	ground.disable(viz.COLOR_WRITE)
	ground.alpha(0.5)
	ground.collidePlane()
	gAxes = vizshape.addAxes(.2 )
	viz.link( ground, gAxes )
	gAxes.alpha(0.5)
	
###################################################################################


### Arrow Functions ###############################################################



#this function stores quadratic points of an equation into an array. 
def setPositionsQuadratic(array, numPositions, X, Y, Z, endX, endY, endZ, constant=0):
	Coe = numPositions;
	
	selector = "Y:zero";
	if endY > 0: 
		selector  = "Y:positive";
	elif endY < 0: 
		selector = "Y:negetive";
	
	angle = math.atan(float(abs(endY) - abs(Y))/float(abs(endX) - abs(X)));
	
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
	scaleSize = parabolaHeight * 0.1;
	arrow.setScale(scaleSize, scaleSize, scaleSize); #change the size of arrow object
	
	path = viz.addAnimationPath(); #create an animation path

	for x,pos in enumerate(positions): #for every position in the array (x = pos)
		a = viz.addChild('beachball.osgb', cache=viz.CACHE_CLONE); #add a control point object
		a.setPosition(pos); #set the object at the position specified
		a.alpha(0.1); #make it almost invisible
		path.addControlPoint(x+1, pos=pos); #add it onto the path
		
	path.setSpeed(pathSpeed); #set the speed of the path
	path.setLoopMode(viz.LOOP); #set the path on a loop

	path.computeTangents(); #compute the tangents 
	path.setAutoRotate(viz.ON); #set it to auto rotate
	viz.link(path, arrow); #link the path to the arrow object so that the arrow will move
	path.play(); #play the animation

###################################################################################

