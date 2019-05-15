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