from setup import *

### Execution Setup ################
instructionPanel = vizinfo.InfoPanel(currentStep,fontSize=40);
instructionPanel.addSeparator();
additionalInfo = instructionPanel.addLabelItem("as", viz.addText("Hello world"));
additionalInfo.label.color(viz.BLUE);
####################################

### Program Execution ##############
#vizact.ontimer(0.0,updateCameras); #this bad boy runs the camera
#viz.go(); #starts up viz
####################################

if origamiMode == 'Swan': #Swan mode 
	print "Entering Swan Mode!";
	while isTrialCompleted == 0:
		print "In Step " + str(currentStepNum);
		print swanInstructions[currentStepNum];

		#when step is completed, set isStepCompleted to 1
		if isStepCompleted == 1:
			nextStep();
			isStepCompleted = 0;
			currentStepNum += 1;
			if currentStepNum == endStepNum:
				isTrialCompleted = 1; #this goes to the last one 
elif origamiMode == 'Boat':
	print "Entering Boat Mode!";
	while isTrialCompleted == 0:
		print "In Step " + str(currentStepNum);
		print boatInstructions[currentStepNum];
		
		#when step is completed, set isStepCompleted to 1
		if isStepCompleted == 1:
			nextStep();
			isStepCompleted = 0;
			currentStepNum += 1;
			if currentStepNum == endStepNum:
				isTrialCompleted = 1; #this goes to the last one 
	
else: 
	print "Incorrect Mode selected!";



