#####################################################################################
### Libraries #######################################################################
#####################################################################################

import viz # general viz module
import vizact
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

import datetime

#import data dependency and project files.
from config import * 

#####################################################################################
#####################################################################################
#####################################################################################


####################################################################################
######### Variables Declarations ###################################################
####################################################################################

#There are XX boat steps and YY swan steps, but an extra buffer step is added in order 
#to programmatically account for the intermediate time between when the actual experiment 
#begins and when the program is executed by the research assistant. 
lastSwanStepNum = 10 + 1;
lastBoatStepNum = 15 + 1;


#Note that for both the boat and swan instructions, an extra element "You have completed this task!"
#is included.

boatInstructions = [
	"1. position the paper vertically.",
	"2. Fold the left side to the right side.",
	"3. Unfold the left side from the right side.",
	"4. Fold the top side to the bottom side.",
	"5. Fold the top-left and top-right corners        towards the center so that the two corners meet.",
	"6. Fold the top layer of the bottom flap upwards and crease.",
	"7. Turn the paper over. ",
	"8. Fold the bottom flap upwards and crease.",
	"9. Pull the two layers apart from the bottom and collapse it into a diamond.",
	"10. Fold the top layer from the bottom corner to the top corner.",
	"11. Turn the paper over. ",
	"12. Fold the top layer from the bottom corner to the top corner.",
	"13. Pull the two layers apart from the bottom and collapse it into a diamond.",
	"14. Gently pull apart the two thin layers on the left and right sides.",
	"15. Crease the triangle-shaped section and       position it vertically.",
	"You have completed this task!"
];

swanInstructions = [
	"1. Position the paper like a diamond.",
	"2. Fold the bottom-left and bottom-right sides to the center so that the sides meet.",
	"3. Flip the paper over.",
	"4. Fold the bottom-left and bottom-right sides to the center so that the sides meet.",
	"5. Fold the bottom corner towards the top.",
	"6. Fold down a small section from the top corner of the top layer.",
	"7. Flip the paper over.",
	"8. Fold the left side (both layers) to the right and crease.",
	"9. Hold the bottom layer down and pull the top   layer up.",
	"10. Pull the small section of the top layer out.",
	"You have completed this task!"
];

#All of these variables are subject to change based on user input. 
#The RA will specify these variables when they launch the program.
participantID = "";
origamiType = "";
methodType = "";
taskType = "";
taskNum = "";
setNum = "";

currentStepNum = 0;
onScreenStepNum = 0;
endStepNum = 0;
taskIsCompleted = False;

currentStep = "Step " + str(currentStepNum);


currentDateTime = datetime.datetime.utcnow();

#####################################################################################
#####################################################################################
#####################################################################################

#####################################################################################
### User Input ######################################################################
#####################################################################################

participantID = raw_input("Please enter participant ID: ");

while origamiType not in {"Boat", "Swan", "boat", "swan", "BOAT", "SWAN", "b", "s", "B", "S"}:
    origamiType = raw_input("Please enter origami type (enter 'b' for 'Boat', 's' for 'Swan'): ");

if(origamiType == "boat" or origamiType == "BOAT" or origamiType == "b" or origamiType == "B"):
    origamiType = "Boat";
elif(origamiType == "swan" or origamiType == "SWAN" or origamiType == "s" or origmaiType == "S"):
    origamiType = "Swan";
    
#The method type will always be AR when running from the computer.
methodType = "AR";

#The task type is determined by two separate user inputs in order to reduce ambiguity.
while setNum not in {"1", "2"}:
    setNum = raw_input("Is this origami set 1 or 2? (enter '1' or '2'):");

while taskNum not in {"1", "2", "3"}:
    taskNum = raw_input("Is this task 1, 2, or 3? (enter '1', '2', or '3') (note: test is NOT done with AR): ");

#Determine the taskType based on user input.
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
    
#Print User Input that the RA provides
print "Current Date: ", currentDateTime;
print "Participant ID: ", participantID;
print "Origami Type: ", origamiType;
print "Method Type: ", methodType;
print "Task Type: ", taskType;

if origamiType == "Swan":
	endStepNum = lastSwanStepNum;
elif origamiType == "Boat":
	endStepNum = lastBoatStepNum;

####################################################################################
####################################################################################
####################################################################################



####################################################################################
### Vizard Text Initialization #####################################################
####################################################################################

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

bottomTextOnScreen = viz.addText('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.()/ ',pos=[0,0.7,4]);

#Set initial text to negligible scale so that the user won't see the extra characters needed.
bottomTextOnScreen.setScale(0.0001,0.00001,0.0001);

#Perform configurations for text.
bottomTextOnScreen.alignment(viz.ALIGN_CENTER_BOTTOM);
bottomTextOnScreen.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM);
bottomTextOnScreen.font('Times New Roman'); 
bottomTextOnScreen.resolution(1);


#Misc Setup
viz.mouse.setVisible(viz.OFF); # remove mouse cursor when program starts
viz.phys.enable();   

# Load DirectInput plug-in for xbox controller interface.
dinput = viz.add('DirectInput.dle');
joy = dinput.addJoystick();
joy.setDeadZone(0.2);

####################################################################################
####################################################################################
####################################################################################


####################################################################################
### StopWatch class declaration ####################################################
####################################################################################

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
    def updateOverallTime(self):
        self.overallTime = 0;
        
        #Subtract from the initial grace period time before the timer officially started.
        for t in range(len(self.stepTimes)):
            #Skip the intermediate step.
            if t > 0:
                self.overallTime += self.stepTimes[t];
    def startNextStep(self):
        self.currentStepStartTime = self.currentStepEndTime;
        self.currentStepEndTime = time.time();
        
        #The difference between the last step's end time and the current time is used to calculate the 
        #total time elapsed for a particular step.
        self.stepTimes[self.currentStepNum] = self.currentStepEndTime - self.currentStepStartTime;
        
        self.updateOverallTime();
        
        self.currentStepNum += 1;
    def revertToLastStep(self):
        self.currentStepNum -= 1;
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
####################################################################################
####################################################################################