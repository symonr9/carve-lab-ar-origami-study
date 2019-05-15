#Arrow Functions

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



#### AR Marker setup ###############################################################
rightMarkerArray = [];
leftMarkerArray = [];

#rightMarker = rightCam.addMultiMarker('ar/cubeMarkerConfig.dat',width=40);
rightMarkerArray.append(rightMarker);
leftMarker = leftCam.addMultiMarker('ar/cubeMarkerConfig.dat',width=40);
leftMarkerArray.append(leftMarker);

rightMarker2 = rightCam.addMatrixMarker(63, width=200);
rightMarkerArray.append(rightMarker2);
leftMarker2 = leftCam.addMatrixMarker(63, width=200);
leftMarkerArray.append(leftMarker2);

rightMarker3 = rightCam.addMatrixMarker(62, width=125);
rightMarkerArray.append(rightMarker3);
leftMarker3 = leftCam.addMatrixMarker(62, width=125);
leftMarkerArray.append(leftMarker3);




### Objects Setup ##################################################################
####################################################################################
####################################################################################


#rh_sphere=vizshape.addSphere(radius=.02,slices=20,stacks=20) #Adding a sphere to represent user's fingertip
#viz.link(rightHandTracker, rh_sphere)

#ground = vizshape.addPlane(size=(50.0,50.0),axis=vizshape.AXIS_Y, cullFace=True)
#setupGround(ground);

#basketball = viz.add('basketball.osgb');
#basketball.setScale(0.1,0.1,0.1);

#linkMarkers(leftMarker, rightMarker, basketball, basketball);

####################################################################################
####################################################################################
####################################################################################


#### Augmented reality setup #######################################################
ar = viz.add('artoolkit.dle');