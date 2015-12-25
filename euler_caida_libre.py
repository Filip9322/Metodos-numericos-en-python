import numpy as np
import matplotlib.pyplot as plt

def f(v):
    return g-((b*v)/m)
    
i=0
h=0.1
v=0
g=9.8
m=2
b=1
y1=[]

while i<10:
    print(str(i)+' '+str(v))
    y1.append(v)
    v=v+h*f(v)
    i=i+1
    

t1 = np.arange(0.0, 1.0, 0.1)

plt.clf()

plt.figure(1)
plt.plot(t1, y1)
plt.show()