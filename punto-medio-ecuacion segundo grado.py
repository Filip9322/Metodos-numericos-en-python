import numpy as np

import matplotlib.pyplot as plt

#x''+2x'+5x=0
def f1(x2):
    return x2
    
def f2(x1,x2):
    return -5*x1-2*x2
    

h=0.1
t=0
x1=1
x2=0
x1r=[]
x2r=[]
td=[]

while t<5:
    print (str(t)+' '+str(x1))
    td.append(t)
    
    dx1=h*f1(x2)/2      #paso1
    dx2=h*f2(x1,x2)/2      #paso1
    
    
    fmid1=f1(x2+dx2)     #paso2
    fmid2=f2(x1+dx1,x2+dx2)     #paso2
    x1r.append(x1)   
    x1=x1+h*fmid1  #paso3
    
    x2r.append(x2)        
    x2=x2+h*fmid2 #paso3
    t=t+h
    
    
    



plt.figure(1)
plt.plot(td, x1r,'y')