import numpy as np

import matplotlib.pyplot as plt

# 2y+x(exp(3x)-exp(2x))
def f(y):
    return (2*y)+(1*((np.exp(3*1))-(np.exp(2*1))))
 
i=0
h=0.1
funcion=0
Deltay=0
mid=0
fmid=0
x=1
y=2
y1=[]


while i<10:
    print (str(i)+' '+str(y))
    y1.append(y)
    funcion=f(y)
    Deltay=funcion*(h/2)
    mid=y+Deltay
    fmid=f(mid)
    y=y+(h*fmid)
    i=i+1

t1=np.arange(0.0, 1.0, 0.1)    
plt.clf()   
plt.figure(1)
plt.plot(t1, y1,'y')