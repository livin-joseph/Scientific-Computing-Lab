import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

def NF(xx, y):
    n = len(xx)
    yy = np.zeros((n,n))
    for i in range(n):
        yy[i][0] = y[i]
    for i in range(1, n): 
        for j in range(n - i): 
            yy[j][i] = yy[j + 1][i - 1] - yy[j][i - 1]
    x = sp.Symbol('x')
    c = sp.Symbol('c')
    h = xx[1] - xx[0]
    c = (x - xx[0]) / h
    eq = yy[0][0]
    for i in range(1, n):
        f = 1
        for j in range(1, i+1):
            f = f * (c - j + 1)
        f = f * yy[0][i]
        f = f / math.factorial(i)
        eq = eq + f
    eq = sp.simplify(eq)
    return eq, yy

xx = [3, 4, 5, 6, 7, 8, 9]
y = [4.8, 8.4, 14.5, 23.6, 36.2, 52.8, 73.9]

x = sp.Symbol('x')

s, t = NF(xx, y)

print('Interpolated Value when x = 3.5 : ', round(s.subs(x, 3.5), 4))
print('Interpolated Value when x = 8.5 : ', round(s.subs(x, 8.5), 4))
print('Newton\'s Forward Difference Table')
print(t)

print('Interpolating polynomial: ', s)

xv = np.linspace(0, 12, 1000)
plt.plot(xv, [s.subs(x, val) for val in xv])
plt.scatter(xx, y)
plt.show()
