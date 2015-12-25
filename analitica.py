import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (np.exp(3*x)*(x-1))-((np.exp(2*x)*(x*x))/2)+(np.exp(2*x)*3)


x=np.arange(0.0, 1.0, 0.1)

plt.clf()

plt.figure(1)
plt.plot(x, f(x), 'b-')
plt.show()
