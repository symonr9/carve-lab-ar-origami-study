from setup import *


### Execution Setup ################
#5/15/19: Resolved bug where certain text dissapears when attempting to reference textOnScreen object inside of 
#key event functions. Each letter that was missing was correlated to the letter not being in the starting text. 
#In order to fix this, I added all possible characters that could be used in the initial text. 
textOnScreen = viz.addText('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.()/ ',pos=[0,0.8,4]);

#Possible configurations for VideoVision testing.
#textOnScreen = viz.addText('Begin by pressing the down key.',pos=viz.ABSOLUTE);
#textOnScreen = viz.addText('Begin by pressing the down key.',viz.RELATIVE_LOCAL);

#Set initial text to negligible scale so that the user won't see the extra characters needed.
textOnScreen.setScale(0.0001,0.00001,0.0001);

#Perform configurations for text.
textOnScreen.alignment(viz.ALIGN_CENTER_BOTTOM);
textOnScreen.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM);
textOnScreen.font('Times New Roman'); 
textOnScreen.resolution(1);


### Program Execution ##############
viz.go(viz.STEREO_HORZ);
cameras = VideoVision.add(camType=VideoVision.UEYE);
####################################


def updateScreenText(origamiMode, stepNum):
	global textOnScreen, boatInstructions, swanInstructions;

	if origamiMode == "Boat":
		textOnScreen.message(boatInstructions[stepNum]);
	elif origamiMode == "Swan":
		textOnScreen.message(swanInstructions[stepNum]);
	textOnScreen.setScale(0.10,0.10,0.10);
		
def nextStep(key):
	global origamiMode, isStepCompleted, currentStepNum;
	if origamiMode == "Boat" or origamiMode == "Swan":
		updateScreenText(origamiMode, currentStepNum);
		currentStepNum += 1;			
		if currentStepNum == endStepNum:
			print "You have completed this task!";
			exit();
	else: 
		print "Incorrect Mode selected!";





### Program Execution ##############
viz.callback(viz.KEYDOWN_EVENT,nextStep);
####################################


