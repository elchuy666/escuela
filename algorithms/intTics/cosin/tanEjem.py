import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.tan(x)

N =10000
epsilon =1e-1
A=-np.pi/2.0+epsilon
B=np.pi/2

dx=(B-A)/N
x = np.arange(A,B,dx)

plt.plot(x,f(x))
plt.show()