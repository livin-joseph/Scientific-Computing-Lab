import sympy as sp
import matplotlib.pyplot as plt

a = sp.Symbol('a')
b = sp.Symbol('b')
x = sp.Symbol('x')

print("Enter the data points")
x1 = float(input("x1 = "))
y1 = float(input("f(x1) = "))
x2 = float(input("x2 = "))
y2 = float(input("f(x2) = "))

eq1 = sp.Eq(y1, a * x1 + b)
eq2 = sp.Eq(y2, a * x2 + b)

xp = float(input("Enter the value of x: "))
coeff = sp.solve([eq1, eq2], [a, b])

eq = coeff[a] * x + coeff[b]
yp = eq.subs(x, xp)

print("Interpolating polynomial: ", eq)
print("f(", xp, ") = ", yp)

import numpy as np
xt = [x1, x2]
x_var = np.linspace(max(xt), min(xt), 1001)
y_var = []

for i in x_var:
    y_var.append(eq.subs(x, i))

plt.plot(x_var, y_var)
plt.scatter([x1, x2], [y1, y2])
plt.show()
