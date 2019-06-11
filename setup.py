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
import time
from threading import Timer

#import data dependency and project files.
from config import * 
#####################################################################################

### Setup ###########################################################################
participantID = "";
origamiType = "";
methodType = "";
taskType = "";
taskNum = "";
setNum = "";

#All of these variables are subject to change based on user input. 
#The RA will specify these variables when they launch the program.

#FIXME TODO: See if it should be an integer or a string in the database.

participantID = raw_input("Please enter participant ID: ");

while origamiType not in {"Boat", "Swan", "boat", "swan", "BOAT", "SWAN", "b", "s", "B", "S"}:
    origamiType = raw_input("Please enter origami type (enter 'b' for 'Boat', 's' for 'Swan'): ");

if(origamiType == "boat" or origamiType == "BOAT" or origamiType == "b" or origamiType == "B"):
    origamiType = "Boat";
elif(origamiType == "swan" or origamiType == "SWAN" or origamiType == "s" or origmaiType == "S"):
    origamiType = "Swan";

while methodType not in {"Normal", "AR", "N", "A", "n", "a", "normal", "ar"}:
    methodType = raw_input("Please enter method type (enter 'n' for 'Normal', 'a' for 'AR'): ");

if(methodType == "normal" or methodType == "N" or methodType == "n"):
    methodType = "Normal";
elif(methodType == "ar" or methodType == "A" or methodType == "a"):
    methodType == "AR";


#The task type is determined by two separate user inputs in order to reduce ambiguity.
while setNum not in {"1", "2"}:
    setNum = raw_input("Is this origami set 1 or 2? (enter '1' or '2'):");

while taskNum not in {"1", "2", "3"}:
    taskNum = raw_input("Is this task 1, 2, or 3? (enter '1', '2', or '3') (note: test is NOT done with AR): ");

if setNum == "1":
    if taskNum == "1":
        taskType = "First1";
    elif taskNum == "2":
        taskType = "First2";
    elif taskNum == "3":
        taskType = "First3";
elif setNum == "2":
    if taskNum == "1":
        taskType = "Second1";
    elif taskNum == "2":
        taskType = "Second2";
    elif taskNum == "3":
        taskType = "Third3";
    

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



### StopWatch class declaration ####################################################
class OrigamiTimeData: 
    def __init__(self, origamiType):
        self.origamiType = origamiType;
        #lastStepNum is used to determine when the task has been completed.
        self.lastStepNum = 0;
        if self.origamiType == "Boat":
            self.lastStepNum = lastBoatStepNum;
        elif self.origamiType == "Swan":
            self.lastStepnum = lastSwanStepNum;
        
        
        #Note that the beginning step number is 0, not 1. This is intentional in order to 
        #allow the participant to determine the official start of the timer.
        self.currentStepNum = 0;

        self.currentStepStartTime = 0;
        self.currentStepEndTime = 0;
        
        #The boat instructions have more steps than the swan and thus,
        #the data is saved in the database for up to the number of boat steps,
        #even if the task is for a swan. The remainding steps are simply not counted 
        #and are set to 0.
        
        #A 1 is added to the lastBoatStepNum because the instructions are labeled from 
        #1 onwards. A grace period time is also set for stepTimes[0] and doesn't count 
        #to the overall time it takes to execute the program. This is to allow for the 
        #research assistants to conduct any additional actions while also allowing the 
        #particpiant themselves to dictate when to start, similar to the normal paper manual
        #method with the tablet.
        self.stepTimes = [0] * (lastBoatStepNum + 1);
        
        self.overallTime = 0;
    def updatedOverallTime(self):
        self.overallTime = 0;
        
        #Subtract from the initial grace period time before the timer officially started.
        for t in range(len(self.stepTimes)):
            #Skip the intermediate step.
            if t > 0:
                self.overallTime += self.stepTimes[t];
    def startNextStep(self):
        self.currentStepStartTime = self.currentStepEndTime;
        self.currentStepEndTime = time.time();
        
        self.stepTimes[self.currentStepNum] = self.currentStepEndTime - self.currentStepStartTime;
        self.updatedOverallTime();
        
        self.currentStepNum += 1;
    def printData(self):
        print "Origami Type: ";
        print self.origamiType;
        print "Last Step Num: ";
        print self.lastStepNum;
        print "Overall Time: "; 
        print self.overallTime;
        print "Step Times: ";
    
        for t in range(len(self.stepTimes)):
            print "Step ", str(t), ": ";
            print self.stepTimes[t];
    
####################################################################################