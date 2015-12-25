import numpy as np

import matplotlib.pyplot as plt

def f(v):
    return 9.8*t+v
 
i=0
h=0.1
funcion=0
Deltay=0
mid=0
fmid=0
v=0
t=0

v1=[]


while i<10:
    print (str(i)+'     '+str(v))
    v1.append(v)
    funcion=f(v)
    Deltay=funcion*(h/2)
    mid=v+Deltay
    fmid=f(mid)
    v=v+(h*fmid)
    i=i+1

t1=np.arange(0.0, 1.0, 0.1)    
plt.clf()   
plt.figure(1)
plt.plot(t1, v1,'r')