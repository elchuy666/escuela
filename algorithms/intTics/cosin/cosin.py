import math
import matplotlib.pyplot as plt

def f(x):
    y = math.cos(x)
    return y

def g(x):
    y = math.sin(x)
    return y

N =1000
A=0
B=2*3.1416

dx=(B-A)/N
values = range(N+1)
print(values)

x=A
X=[]
Y=[]

X2=[]
Y2=[]

for jump in values:
    print(x)
    x= A + jump*dx
    y=f(x)
    X.append(x)
    Y.append(y)

    y=g(x)
    X2.append(x)
    Y2.append(y)

    print(x, y)

plt.plot(X,Y)
plt.plot(X2, Y2)