import viz
import vizinfo
import vizinput


from config import * 
#from projectFunctions import *

viz.go()

phase = 1;
endPhase = 10;

currentPhase = "Phase " + str(phase);
command = "";

instructionPanel = vizinfo.InfoPanel(currentPhase,fontSize=40);
separator = instructionPanel.addSeparator();
additionalInfo = instructionPanel.addLabelItem(command, viz.addText(""));
additionalInfo.label.color(viz.BLUE);



def nextPhase(phaseCommand):
	global testPhase, currentPhase, endPhase, instructionPanel, additionalInfo, separator;
	testPhase = testPhase + 1;
	if testPhase > endPhase:
		testPhase = 0;
	currentPhase = "Phase " + str(testPhase);
	instructionPanel.setText(currentPhase); 
	#additionalInfo.setText(phaseCommand);
	
	instructionPanel.removeItem(additionalInfo);
	instructionPanel.removeItem(separator);
	
	separator = instructionPanel.addSeparator();
	additionalInfo = instructionPanel.addLabelItem(phaseCommand, viz.addText(""));

	if phaseCommand == flattenCommand: 
		additionalInfo.label.color(viz.BLUE);
	elif phaseCommand == foldCommand: 
		additionalInfo.label.color(viz.GREEN);
	
vizact.onkeydown('o', nextPhase, foldCommand);
vizact.onkeydown('l', nextPhase, flattenCommand);