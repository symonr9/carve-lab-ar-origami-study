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
from config import * 
#####################################################################################

### Setup ###########################################################################
participantID = "";
origamiType = "";
methodType = "";
taskType = "";

#All of these variables are subject to change based on user input. 
#The RA will specify these variables when they launch the program.

#FIXME TODO: See if it should be an integer or a string in the database.
participantID = raw_input("Please enter participant ID: ");

while origamiType not in {"Boat", "Swan"}:
    origamiType = raw_input("Please enter origami type ('Boat' or 'Swan'): ");
while methodType not in {"Normal", "AR"}:
    methodType = raw_input("Please enter method type ('Normal' or 'AR'): ");
while taskType not in {"First1", "First2", "First3", "Test1", "Second1", "Second2", "Second3", "Test2"}:
    taskType = raw_input("Please enter task type ('First1', 'First2', 'First3', 'Test1', 'Second1', 'Second2', 'Second3', or 'Test2', ex: First2 is the first origami learning task #2): ")


#Output User Input that the RA provides
print "Participant ID: ", participantID;
print "Origami Type: ", origamiType;
print "Method Type: ", methodType;
print "Task Type: ", taskType;

if origamiType == "Swan":
	endStepNum = lastSwanStepNum;
elif origamiType == "Boat":
	endStepNum = lastBoatStepNum;

#5/22/19: Resolved bug where certain text dissapears when attempting to reference textOnScreen object inside of 
#key event functions. Each letter that was missing was correlated to the letter not being in the starting text. 
#In order to fix this, I added all possible characters that could be used in the initial text. 
textOnScreen = viz.addText('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.()/ ',pos=[0,0.8,4]);

#Set initial text to negligible scale so that the user won't see the extra characters needed.
textOnScreen.setScale(0.0001,0.00001,0.0001);

#Perform configurations for text.
textOnScreen.alignment(viz.ALIGN_CENTER_BOTTOM);
textOnScreen.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM);
textOnScreen.font('Times New Roman'); 
textOnScreen.resolution(1);


#Misc Setup
viz.mouse.setVisible(viz.OFF); # remove mouse cursor when program starts
viz.phys.enable();   

####################################################################################