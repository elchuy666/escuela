import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

def g(x):
    return np.sin(x)

N =1000
A=0
B=20* 2 * np.pi

dx=(B-A)/N
x = np.arange(A,B,dx)

plt.plot(x,f(x))
plt.plot(x, g(x))