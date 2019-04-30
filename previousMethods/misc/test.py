import viz
import vizinfo
import vizact
import math
import vizshape

from config import * 



current = 1;

current = 0;

baseValueX = 0;
baseValueY = 0;
baseValueZ = 0;


endValueX = -5;
endValueY = -5;
endValueZ = -5;

parametricValueX = baseValueX + endValueX;
parametricValueY = baseValueY + endValueY; 
parametricValueZ = baseValueZ + endValueZ;

#Now I have the line (x,y,z) = (baseValueX, baseValueY, baseValueZ) + t(parametricValueX, parametricValueY, parametricValueZ)
#where t will give me a point on the line).

#next steps is to figure out what t is for the base value and the end value. 
#For the base value, t = 0. 
#for the end value, you get t = 1. 

#so if you wanted to plot points against the line
#with n as number of points, 
#you would do t = 1/n, 1/n-1, 1/n-2 ... 1/n

#equation is [baseValueX + parametricValueX * 1/r, baseValueY + parametricValueY * 1/r, baseValueZ + parametricValueZ * 1/r] 

positions = [[baseValueX,baseValueY,baseValueZ]];

n = 10;
for i in range(n-1):
	r = 1.0 / n;
	print "r: " + str(r);

	print "n: " + str(n);
	positions.append([baseValueX + parametricValueX * 2 * r, baseValueY + parametricValueY * 2 * r, baseValueZ + parametricValueZ * 2 * r] );
	
	#sphere = vizshape.addSphere(radius=1); 
	#sphere.setScale(0.2);
	
	#sphere.setPosition([baseValueX, baseValueY-i, baseValueZ+i]); 
	n = n - 1;
	
	print positions;


