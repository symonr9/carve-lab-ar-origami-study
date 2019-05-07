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

#import data dependency and project files.
#from origamiData import *
#from parameters import *
from config import * 
from projectFunctions import *
#####################################################################################

### Misc Setup ######################################################################
#####################################################################################
#####################################################################################

viz.mouse.setVisible(viz.OFF); # remove mouse cursor when program starts
viz.phys.enable();   

#####################################################################################
#####################################################################################
#####################################################################################


### Camera Setup ####################################################################
#####################################################################################
#####################################################################################

viz.go(viz.STEREO_HORZ)
cameras = VideoVision.add(camType=VideoVision.UEYE)

text2D = viz.addText('After folding the paper in half ian Step 3,',pos=[0,1,4]);
text2D.setScale(0.08,0.08,0.08)
text2D.alignment(viz.ALIGN_CENTER_BOTTOM)
text2D.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
text2D.resolution(1)

text2D = viz.addText(' fold the top-left and top-right corners',pos=[0,0.9,4]);
text2D.setScale(0.08,0.08,0.08)
text2D.alignment(viz.ALIGN_CENTER_BOTTOM)
text2D.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
text2D.resolution(1)


text2D = viz.addText('of the paper so that the two corners mee',pos=[0,0.8,4]);
text2D.setScale(0.08,0.08,0.08)
text2D.alignment(viz.ALIGN_CENTER_BOTTOM)
text2D.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM)
text2D.resolution(1)


'''
vizconnect.go('./Vizconnect_config_2limbs.py'); #vizconnect configurations are initialized here
viz.ipd(.08); #vision as related between eyes?
viz.clip(near=.12);

headTracker = vizconnect.getRawTracker('optical_heading');
rightHandTracker = vizconnect.getRawTracker('ppt_rhand');
#### Augmented reality setup #######################################################
ar = viz.add('artoolkit.dle');

camera = VideoVision.add(VideoVision.UEYE);
rightCam = ar.addCamera(camera.rightcam, flipVertical=True, eye=viz.RIGHT_EYE);
leftCam = ar.addCamera(camera.leftcam, flipVertical=True, eye=viz.LEFT_EYE);
'''

'''
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
'''

####################################################################################
####################################################################################
####################################################################################


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
