import sympy as sp

x = sp.Symbol('x')

def lagrange(xvalues, yvalues):
    n = len(xvalues)

    eqn = 0
    for i in range(len(xvalues)):
        s = 1
        for j in range(len(xvalues)):
            if i == j:
                continue
            s = s * (x - xvalues[j]) / (xvalues[i] - xvalues[j])
        s = s * yvalues[i]
        eqn = eqn + s
    eqn = eqn.expand()
    
    return eqn

x_values = [45, 46, 50, 55, 65]
y_values = [114.84, 110.525632, 96.16, 83.32, 68.48]

lag = lagrange(x_values, y_values)
print("Interpolating polynomial: ", lag)

print("Premium for policy with respect to age of maturing")
print("Age 46: ", lag.subs(x, 46))
print("Age 63: ", lag.subs(x, 63))

import numpy as np
import matplotlib.pyplot as plt

x_val = np.linspace(min(x_values), max(x_values), 1000)
y_val = [lag.subs(x, i) for i in x_val]

plt.plot(x_val, y_val)
plt.scatter(x_values, y_values, color = 'black')
plt.show()
