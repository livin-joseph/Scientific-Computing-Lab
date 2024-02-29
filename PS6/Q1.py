import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')
y = sp.Symbol('y')

print("Enter the data points")
x1 = float(input("x1 = "))
y1 = float(input("f(x1) = "))
x2 = float(input("x2 = "))
y2 = float(input("f(x2) = "))

m = (y2 - y1) / (x2 - x1)

eq = sp.Eq(y - y1, m * (x - x1))

xp = float(input("Enter the value of x: "))
yp = sp.solve(eq.subs(x, xp))[0]

print("f(", x, ") = ", yp)

# Plotting
x_var = [x1, x2]
y_var = []

for i in x_var:
    y_var.append(sp.solve(eq.subs(x, i))[0])

plt.plot(x_var, y_var)
plt.scatter([x1, x2], [y1, y2])
plt.show()
