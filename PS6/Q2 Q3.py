import sympy as sp
import matplotlib.pyplot as plt

a = sp.Symbol('a')
b = sp.Symbol('b')
c = sp.Symbol('c')
x = sp.Symbol('x')

print("Enter the data points")
x1 = float(input("x1 = "))
y1 = float(input("f(x1) = "))
x2 = float(input("x2 = "))
y2 = float(input("f(x2) = "))
x3 = float(input("x3 = "))
y3 = float(input("f(x3) = "))

eq1 = sp.Eq(y1, a * x1**2 + b * x1 + c)
eq2 = sp.Eq(y2, a * x2**2 + b * x2 + c)
eq3 = sp.Eq(y3, a * x3**2 + b * x3 + c)

xp = float(input("Enter the value of x: "))
coeff = sp.solve([eq1, eq2, eq3], [a, b, c])

eq = coeff[a] * x**2 + coeff[b] * x + coeff[c]
yp = eq.subs(x, xp)

print("Quadratic equation: ", eq)
print("f(", x, ") = ", yp)

# Plotting
import numpy as np
xt = [x1, x2, x3]
x_var = np.linspace(max(xt), min(xt), 1001)
y_var = []

for i in x_var:
    y_var.append(eq.subs(x, i))

plt.plot(x_var, y_var)
plt.scatter([x1, x2, x3], [y1, y2, y3])
plt.show()
