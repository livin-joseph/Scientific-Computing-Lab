import sympy as sp
import numpy as np
import math
import matplotlib.pyplot as plt

x = sp.Symbol("x")

eq = input("Enter an equation with one variable\n")
eq = sp.sympify(eq)

low_lim = int(input("Enter the lower limit of the interval: "))
upp_lim = int(input("Enter the upper limit of the interval: "))

# Newton Raphson method
h = eq / sp.diff(eq)

print("Iteration table")
print("x(n) \t x(n+1)")

xn = low_lim
xn1 = round(xn - h.subs(x, xn), 2)
print(round(xn, 2), "\t", round(xn1, 2))

while round(xn, 2) != round(xn1, 2):
    xn = round(xn1, 2)
    xn1 = round(xn - h.subs(x, xn), 2)
    print(round(xn, 2), "\t", round(xn1, 2))

print("Real root of the equation: ", round(xn1, 4))

# Bisection method
a = low_lim
b = upp_lim
if eq.subs(x, a) * eq.subs(x, b) < 0:
    print("Bisection method can be applied")
else:
    print("Bisection method cannot be applied")
t = (a + b) / 2
print("a \t b \t t \t f(a) \t f(b) \t f(t)")
print(a, "\t", b, "\t", t, "\t", round(eq.subs(x, a), 2), "\t", round(eq.subs(x, b), 2), "\t", round(eq.subs(x, t), 2))
while round(eq.subs(x, t), 2) != 0:
    if round(eq.subs(x, t), 2) > 0:
        b = t
    else:
        a = t
    t = (a + b) / 2
    print(a, "\t", b, "\t", t, "\t", round(eq.subs(x, a), 2), "\t", round(eq.subs(x, b), 2), "\t", round(eq.subs(x, t), 2))

print("Solution: ", round(t, 2))

# Regula Falsi method
a = low_lim
b = upp_lim
if eq.subs(x, a) * eq.subs(x, b) < 0:
    print("Regula Falsi method can be applied")
else:
    print("Regula Falsi method cannot be applied")
t = (a * eq.subs(x, b) - b * eq.subs(x, a)) / (eq.subs(x, b) - eq.subs(x, a))
print("a \t b \t t \t f(a) \t f(b)")
print(a, "\t", b, "\t", t, "\t", round(eq.subs(x, a), 2), "\t", round(eq.subs(x, b), 2))
while round(eq.subs(x, t), 2) != 0:
    if t * round(eq.subs(x, a), 2) < 0:
        b = t
    else:
        a = t
    t = (a * eq.subs(x, b) - b * eq.subs(x, a)) / (eq.subs(x, b) - eq.subs(x, a))
    print(a, "\t", b, "\t", t, "\t", round(eq.subs(x, a), 2), "\t", round(eq.subs(x, b), 2))

print("Solution: ", round(t, 2))
"""
c = a
    while abs(f(c)) >= tol:
        c = b - f(b)*(b-a)/(f(b)-f(a))
        if f(c) == 0.0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return c
"""

# Fixed point iteration method
"""
def fixed_point_iteration(g, x0, tol):
    x1 = g(x0)
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = g(x0)
    return x1
def g1(x):
    return -2/(x**2-x)
root = fixed_point_iteration(g1, -4, 0.0001)
print("The root is: ", root)
"""

# Plotting
x_var = np.linspace(low_lim, upp_lim, 1000)
y_var = []

for i in x_var:
    y_var.append(eq.subs(x, i))

plt.plot(x_var, y_var)
plt.show()
