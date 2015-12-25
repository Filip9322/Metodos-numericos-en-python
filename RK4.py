import numpy as np

import matplotlib.pyplot as plt

# 2y+x(exp(3x)-exp(2x))
def f(y):
    return -5*x+4
    #(2*y)+(x*((np.exp(3*x))-(np.exp(2*x))))
 
i=0
h=0.1
k1=0
k2=0
k3=0
k4=0
x=1
y=2
y1=[]


while i<10:
    print (str(i)+' '+str(y))
    y1.append(y)
    k1=h*f(y)
    k2=h*f(y+(k1/2))
    k3=h*f(y+(k2/2))
    k4=h*f(y+k3)
    y=y+(k1/6)+(k2/3)+(k3/3)+(k4/6)

    i=i+1

t1=np.arange(0.0, 1.0, 0.1)    
plt.clf()   
plt.figure(1)
plt.plot(t1, y1,'r')