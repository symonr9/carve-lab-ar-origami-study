from setup import *

def saveResultsToDB():
	print "ERSAE";
	
	
	
def updateScreenText(origamiType, stepNum):
	global textOnScreen, boatInstructions, swanInstructions;

	if origamiType == "Boat":
		textOnScreen.message(boatInstructions[stepNum]);
	elif origamiType == "Swan":
		textOnScreen.message(swanInstructions[stepNum]);
	textOnScreen.setScale(0.10,0.10,0.10);
		
def nextStep():
	global origamiType, isStepCompleted, currentStepNum;
	if origamiType == "Boat" or origamiType == "Swan":
		updateScreenText(origamiType, currentStepNum);
		currentStepNum += 1;			
		if currentStepNum == endStepNum:
			print "You have completed this task!";
			print "Please save results by pressing the spacebar";
			taskIsCompleted = True;

def handleKeyPressEvent(key):
	if key == ' ':
		if taskIsCompleted:
			saveResultsToDB();
	else:
		if not taskIsCompleted:
			#The user is still going through the current task.
			nextStep();
		else:
			print "Please save results by pressing the spacebar.";

### Program Execution ##############
viz.go(viz.STEREO_HORZ);
cameras = VideoVision.add(camType=VideoVision.UEYE);
viz.callback(viz.KEYDOWN_EVENT,handleKeyPressEvent);
####################################