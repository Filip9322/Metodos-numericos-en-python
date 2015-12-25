import numpy as np

import matplotlib.pyplot as plt

# 2y+x(exp(3x)-exp(2x))
def f(y):
    return (2*y)+(1*((np.exp(3*1))-(np.exp(2*1))))
def g(yy):
    return (2*yy)+(1*((np.exp(3*1))-(np.exp(2*1))))
def hh(t):
    return (np.exp(3*t)*(t-1))-((np.exp(2*t)*(t*t))/2)+(np.exp(2*t)*3)

i=0
h=0.1
funcion=0
Deltay=0
mid=0
fmid=0
k1=0
k2=0
k3=0
k4=0
x=1
y=2
yy=2
y1=[]
y2=[]

while i<10:
    print ('PtM: ' + str(i) + ' ' + str(y))
    y1.append(y)
    print ('Rk4: ' + str(i) + ' ' + str(yy))
    y2.append(yy)
    
    #Punto Medio
    funcion=f(y)
    Deltay=funcion*(h/2)
    mid=y+Deltay
    fmid=f(mid)
    y=y+(h*fmid)
    
    #RK4
    k1=h*g(yy)
    k2=h*g(yy+(k1/2))
    k3=h*g(yy+(k2/2))
    k4=h*g(yy+k3)
    yy=yy+(k1/6)+(k2/3)+(k3/3)+(k4/6)
    
    i=i+1

t1=np.arange(0.0, 1.0, 0.1) 
   

plt.clf()   
plt.figure(1)
plt.plot(t1 ,hh(t1), 'b-')
plt.plot(t1 ,y1, 'g')
plt.plot(t1 ,y2, 'r') 

