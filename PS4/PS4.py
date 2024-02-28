import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import Bisection as bi
import Fixed_Point as fp
import Newton_Raphson as nr
import Regula_Falsi as rf

x = sp.Symbol("x")

eq = input("Enter an equation with one variable\n")
eq = sp.sympify(eq)

low_lim = int(input("Enter the lower limit of the interval: "))
upp_lim = int(input("Enter the upper limit of the interval: "))

bi.bisection(eq, low_lim, upp_lim)

# Fixed point iteration method works only for polynomials
fp.fixed_point(eq, low_lim, upp_lim)

nr.newton_raphson(eq, low_lim, upp_lim)

rf.regula_falsi(eq, low_lim, upp_lim)

# Plotting
x_var = np.linspace(low_lim, upp_lim, 1000)
y_var = []

for i in x_var:
    y_var.append(eq.subs(x, i))

plt.plot(x_var, y_var)
plt.show()
