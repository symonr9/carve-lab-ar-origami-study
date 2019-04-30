from origamiData import *
from parameters import *

##########################################################################
######### Project Step Variables ########################################
##########################################################################

currentStepNum = 0;
isStepCompleted = 0;
isTrialCompleted = 0;

currentStep = "Step " + str(currentStepNum);

endStepNum = 0;

if origamiMode == 'Swan':
	endStepNum = lastSwanStepNum;
elif origamiMode == 'Boat':
	endStepNum = lastBoatStepNum;
	
##########################################################################

##########################################################################
######### Arrow Animation Variables ######################################
##########################################################################

#X axis is left to right 
#Y axis is up and down 
#Z axis is forwards and backwards


parabolaHeight = 8; #controls the height of the parabola 

baseValueX1 = 0;
baseValueY1 = 0;
baseValueZ1 = 0;

endValueX1 = 3;
endValueY1 = 4;
endValueZ1 = 5;

baseIncrementX1 = 3;

pathSpeed = 8;

#baseQuadraticX1 = -x**2+secondPolynomialCoefficient*x;
##########################################################################

