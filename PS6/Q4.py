import sympy as sp
import numpy as np

def divided_diff(xval, yval):
    n = len(xval)
    a = np.zeros((n, n))

    for i in range(n):
        a[i][0] = yval[i]

    for i in range(1, n):
        for j in range(n - i):
            a[j][i] = (a[j+1][i-1] - a[j][i-1]) / (xval[i+j] - xval[j])

    yt = np.reshape(yval, (len(yval), 1))
    a = np.concatenate((yt, a), axis = 1)
    print("Divided Difference Table: ")
    print(a)

    x = sp.Symbol('x')
    eq = a[0][1]
    for i in range(1, n):
        f = 1
        for j in range(1, i+1):
            f = f * (x - xval[j-1])
        f = f * a[0][j+1]
        eq = eq + f
    eq = sp.simplify(eq)

    print('Interpolating polynomial: ', eq)
    xp = float(input("Enter the value of x: "))
    print("f(", xp, ") = ", eq.subs(x, xp))

    xvalues = np.linspace(min(xval), max(xval), 1000)
    yvalues = [eq.subs(x, xv) for xv in xvalues]

    import matplotlib.pyplot as plt

    plt.plot(xvalues, yvalues)
    plt.scatter(xval, yval)
    plt.show()

x_q4_a = [654, 658, 659, 661]
y_q4_a = [2.8156, 2.8182, 2.8189, 2.8202]

x_q4_b = [0, 0.1, 0.2, 0.3, 0.4]
y_q4_b = [1, 1.1052, 1.2214, 1.3499, 1.4918]

print("Question 4 a")
divided_diff(x_q4_a, y_q4_a)

print("Question 4 b")
divided_diff(x_q4_b, y_q4_b)
