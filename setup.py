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

#viz.go(viz.STEREO_HORZ);
#cameras = VideoVision.add(camType=VideoVision.UEYE);


'''
vizconnect.go('./Vizconnect_config_2limbs.py'); #vizconnect configurations are initialized here
viz.ipd(.08); #vision as related between eyes?
viz.clip(near=.12);

headTracker = vizconnect.getRawTracker('optical_heading');
rightHandTracker = vizconnect.getRawTracker('ppt_rhand');

camera = VideoVision.add(VideoVision.UEYE);
rightCam = ar.addCamera(camera.rightcam, flipVertical=True, eye=viz.RIGHT_EYE);
leftCam = ar.addCamera(camera.leftcam, flipVertical=True, eye=viz.LEFT_EYE);
'''

####################################################################################
####################################################################################
####################################################################################