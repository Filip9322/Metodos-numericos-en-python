
import numpy as np
import matplotlib.pyplot as plt

def ff(x):
    return -5*x+4
def f1(x2):
    return -5*x2+4
def r(t):
    return (4/5)+(11/5)*np.exp(-5*t)
x=3
x2=3
ft=0
fl=0
h=0.1

i=0
x1r=[]
x2r=[]

 
while i<10:
    print('E.' +str(i)+' '+str(x))
    print('PM.' +str(i)+' '+str(x2))
    
    x1r.append(x)
    x = x+h*ff(x)
    
    dx1=h*f1(x2)/2      #paso1

    fmid1=f1(x2+dx1)     #paso2
   
    x2r.append(x2)   
    x2=x2+h*fmid1  #paso3
    
    i=i+1

t1=np.arange(0.0,1.0,0.1)

plt.figure("  ")
plt.plot(t1,x1r)
plt.plot(t1,x2r)
plt.plot(t1,r(t1),'r-')

'''
x2r=[]

while t<1:
    print (str(t)+' '+str(x2))
    td.append(t)
    dx1=h*f1(x2)/2      #paso1

    fmid1=f1(x2+dx1)     #paso2
   
    x2r.append(x2)   
    x2=x2+h*fmid1  #paso3
    t=t+h
    
'''