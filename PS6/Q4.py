import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def divided_diff(xx, y, interpolate_x):
    n = len(xx)
    yy = np.zeros((n,n))

    for i in range(n):
        yy[i][0] = y[i]

    for i in range(1, n): 
        for j in range(n - i): 
            yy[j][i] = ((yy[j][i - 1] - yy[j + 1][i - 1]) / (xx[j] - xx[i + j]))

    x = sp.Symbol('x')
    eq = yy[0][0]

    for i in range(1,n):
        f = 1
        for j in range(1,i+1):
            f = f * (x - xx[j-1])
        f = f * yy[0][j]
        eq = eq + f

    print("f(", interpolate_x, ") = ", eq.subs(x, interpolate_x))
    print('Divided Difference Table\n', yy)
    print('Polynomial: ', eq)

    xvalues = np.linspace(min(xx), max(xx), 1000)
    yvalues = [eq.subs(x, xv) for xv in xvalues]

    plt.plot(xvalues, yvalues)
    plt.scatter(xx, y)
    plt.show()

x_q4_a = [654, 658, 659, 661]
y_q4_a = [2.8156, 2.8182, 2.8189, 2.8202]

x_q4_b = [0, 0.1, 0.2, 0.3, 0.4]
y_q4_b = [1, 1.1052, 1.2214, 1.3499, 1.4918]

print("\nQuestion 4 a\n")
divided_diff(x_q4_a, y_q4_a, 656)
print("\nQuestion 4 b\n")
divided_diff(x_q4_b, y_q4_b, 0.38)
