import matplotlib.pyplot as plt

a=[]
b=[]
# y=0
# x=-50

for x in range(0,21,1):
    y=-x**2+20*x+10
    a.append(x)
    b.append(y)
    #x= x+1

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()
