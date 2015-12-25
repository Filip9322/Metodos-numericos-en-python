import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return ((9.8*100)/4)+np.exp((-1)*((4*t1)/100))

t1=np.linspace(0.0 , 10.0)
y1=np.linspace(0.0 , 100.0)
plt.clf()

plt.figure(1)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', y1, f(t2), 'k')

'''
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
'''
plt.show()

