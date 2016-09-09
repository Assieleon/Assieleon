__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-1, 1.01, 0.001)

def veershtrass(x):
    y = 0
    for n in range (50):
        y += 0.5**n*np.cos(5**n*np.pi*x)
    return y

plt.plot(x,veershtrass(x))
plt.show()