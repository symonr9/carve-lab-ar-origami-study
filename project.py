from setup import *

### Execution Setup ################
textOnScreen = viz.addText('Begin by pressing the down key.',pos=[0,0.8,4]);
#Perform configurations for text.
textOnScreen.setScale(0.13,0.13,0.13);
textOnScreen.alignment(viz.ALIGN_CENTER_BOTTOM);
textOnScreen.setBackdrop(viz.BACKDROP_RIGHT_BOTTOM);
textOnScreen.font('Times New Roman') 
textOnScreen.resolution(1);
####################################

### Program Execution ##############
#vizact.ontimer(0.0,updateCameras); #this bad boy runs the camera
viz.go(); #starts up viz
####################################

def printStep(origamiMode, stepNum):
	global textOnScreen;

	if origamiMode == "Boat":
		textOnScreen.message(boatInstructions[stepNum]);
		#textOnScreen = viz.addText(boatInstructions[stepNum]);
	elif origamiMode == "Swan":
		#textOnScreen = viz.addText(swanInstructions[stepNum]);
		textOnScreen.message(swanInstructions[stepNum]);
		
def nextStep(key):
	global origamiMode, isStepCompleted, currentStepNum;
	if origamiMode == "Boat" or origamiMode == "Swan":
		printStep(origamiMode, currentStepNum);
		currentStepNum += 1;			
		if currentStepNum == endStepNum:
			print "You have completed this task!";
			exit();
	else: 
		print "Incorrect Mode selected!";

viz.callback(viz.KEYDOWN_EVENT,nextStep);

