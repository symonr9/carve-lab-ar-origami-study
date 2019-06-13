from setup import *


####################################################################################
### Function Declarations ##########################################################
####################################################################################

def saveResultsToCsvFile():
	print "Successfully saved results into database! ";
	
def updateScreenText(origamiType, stepNum):
	global textOnScreen, bottomTextOnScreen, boatInstructions, swanInstructions;

	if origamiType == "Boat":
		if(len(boatInstructions[stepNum]) < 50):
			textOnScreen.message(boatInstructions[stepNum]);
			bottomTextOnScreen.setScale(0.0001,0.00001,0.0001);
		else:
			textOnScreen.message(boatInstructions[stepNum][:49]);
			bottomTextOnScreen.message(boatInstructions[stepNum][49:]);
			bottomTextOnScreen.setScale(0.08,0.08,0.08);
			
	elif origamiType == "Swan":
		if(len(swanInstructions[stepNum]) < 50):
			textOnScreen.message(swanInstructions[stepNum]);
			bottomTextOnScreen.setScale(0.0001,0.00001,0.0001);
		else: 
			textOnScreen.message(swanInstructions[stepNum][:49]);
			bottomTextOnScreen.message(swanInstructions[stepNum][49:]);
			bottomTextOnScreen.setScale(0.08,0.08,0.08);
			
	textOnScreen.setScale(0.08,0.08,0.08);
		
def goToNextStep():
	global origamiType, isStepCompleted, currentStepNum, onScreenStepNum, taskData;
	
	if currentStepNum != endStepNum:
		#Continue to the next step.
		taskData.startNextStep();
		updateScreenText(origamiType, currentStepNum);
		currentStepNum += 1;
		onScreenStepNum = currentStepNum;
	else:
		print "You have completed this task!";
		print "Please save results by pressing the spacebar";
		taskData.updateOverallTime();		
		taskData.printData();
		taskIsCompleted = True;
		
		#FIXME: decide if you want to just run the save results to DB automatically or not.
		#saveResultsToCsvFile();
		
def goToPreviousStep():
	global origamiType, isStepCompleted, currentStepNum, onScreenStepNum, taskData;
	
	if(currentStepNum > 0):
		taskData.revertToLastStep();
		updateScreenText(origamiType, currentStepNum - 1);
		currentStepNum -= 1;
		onScreenStepNum = currentStepNum;

#Note: The keyboard press event for the numbers 0, 1, 2, and 3 all map to the 
#xbox controller inputs. 
def handleKeyPressEvent(key):
	global origamiType, onScreenStepNum, currentStepNum; 
	
	if key == ' ':
		if taskIsCompleted:
			saveResultsToCsvFile();
	else:
		if not taskIsCompleted:
			if key == '0':
				#The user is still going through the current task.
				goToNextStep();
			elif key == '1':
				if(onScreenStepNum < currentStepNum):
					onScreenStepNum += 1;
					updateScreenText(origamiType, onScreenStepNum);
			elif key == '2':
				if(onScreenStepNum > 0):
					onScreenStepNum -= 1;
					updateScreenText(origamiType, onScreenStepNum);
			elif key == '3':
				goToPreviousStep();
		else:
			print "Please save results by pressing the spacebar.";
			
#green "a" button - buttonNum: 0 - Increments the current step to the next step.
#red "b" button - buttonNum: 1 - Traverses to the next step (does not increment current step).
#blue "x" button - buttonNum: 2 - Traverses to the previous step.
#yellow "y" button - buttonNum: 3 - Reverts the current step to the previous step.
def handleXboxButtonPressEvent(e):
	handleKeyPressEvent(str(e.button));


####################################################################################
####################################################################################
####################################################################################


####################################################################################
### Program Execution ##############################################################
####################################################################################

#Initialize data recording object.
taskData = OrigamiTimeData(origamiType);

#Start vizard up.
viz.go(viz.STEREO_HORZ);

#Connect to the VideoVision cameras.
cameras = VideoVision.add(camType=VideoVision.UEYE);

#Setup callback functions to handle key and button press events.
viz.callback(viz.KEYDOWN_EVENT,handleKeyPressEvent);
viz.callback(viz.SENSOR_DOWN_EVENT, handleXboxButtonPressEvent);


####################################################################################
####################################################################################
####################################################################################