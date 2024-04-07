import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

x = sp.Symbol('x')
np.set_printoptions(suppress=True) # To print float values in fixed point representation rather than scientific notation

def newtons_forward(xv, yv):
    n = len(yv)
    table = np.zeros((n, n))
    for i in range(n):
        table[i][0] = yv[i]
    for i in range(1, n):
        for j in range(n - i):
            table[j][i] = table[j+1][i-1] - table[j][i-1]
    h = xv[1] - xv[0]
    r = (x - xv[0]) / h
    poly = 0
    for i in range(n):
        t = 1
        for j in range(i):
            t = t * (r - j)
        poly = poly + t / math.factorial(i) * table[0][i]
    poly = sp.simplify(poly)
            
    print("Newton's forward difference table\n", table)
    print()
    return poly

def newtons_backward(xv, yv):
    n = len(yv)
    table = np.zeros((n, n))
    for i in range(n):
        table[i][0] = yv[i]
    for i in range(1, n):
        for j in range(n - i):
            table[j][i] = table[j+1][i-1] - table[j][i-1]
    h = xv[1] - xv[0]
    r = (x - xv[n-1]) / h
    poly = 0
    for i in range(n):
        t = 1
        for j in range(i):
            t = t * (r + j)
        poly = poly + t / math.factorial(i) * table[n-i-1][i]
    poly = sp.simplify(poly)
            
    print("Newton's backward difference table\n", table)
    print()
    return poly
    
xv = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
yv = [0.1023, 0.1047, 0.1071, 0.1096, 0.1122, 0.1148]

# Q1 - a
poly_forward = newtons_forward(xv, yv)
poly_backward = newtons_backward(xv, yv)

# Q1 - b
print("Interpolated polynomial (forward difference)\n", poly_forward)
print('f(0.015) = ', round(poly_forward.subs(x, 0.015), 4))
print()

# Q1 - c
print("Interpolated polynomial (backward difference)\n", poly_backward)
print('f(0.0505) = ', round(poly_backward.subs(x, 0.0505), 4))
print()

# Q1 - d
diff_1_forward = sp.diff(poly_forward, x)
diff_2_forward = sp.diff(diff_1_forward, x)

print("First derivative of forward difference polynomial\n", diff_1_forward)
print("Second derivative of forward difference polynomial\n", diff_2_forward)
print('f\'(0.0125) = ', round(diff_1_forward.subs(x, 0.0125), 4))
print('f\'\'(0.0125) = ', round(diff_2_forward.subs(x, 0.0125), 4))

# Q1 - e
diff_1_backward = sp.diff(poly_backward, x)
diff_2_backward = sp.diff(diff_1_backward, x)

print("First derivative of backward difference polynomial\n", diff_1_backward)
print("Second derivative of backward difference polynomial\n", diff_2_backward)
print('f\'(0.0575) = ', round(diff_1_backward.subs(x, 0.0575), 4))
print('f\'\'(0.0575) = ', round(diff_2_backward.subs(x, 0.0575), 4))

x_val = np.linspace(min(xv), max(xv), 1000)
x_val = np.linspace(-1, 1, 1000)

# Q1 - f
y_val = [poly_forward.subs(x, i) for i in x_val]
y_diff_1_val = [diff_1_forward.subs(x, i) for i in x_val]
y_diff_2_val = [diff_2_forward.subs(x, i) for i in x_val]

plt.title('Newton\'s forward difference interpolation')
plt.plot(x_val, y_val, color='red', label='Polynomial')
plt.plot(x_val, y_diff_1_val, color='yellow', label='1st Derivative')
plt.plot(x_val, y_diff_2_val, color='green', label='2nd Derivative')
plt.scatter(xv, yv)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Q1 - g
y_val = [poly_backward.subs(x, i) for i in x_val]
y_diff_1_val = [diff_1_backward.subs(x, i) for i in x_val]
y_diff_2_val = [diff_2_backward.subs(x, i) for i in x_val]

plt.title('Newton\'s backward difference interpolation')
plt.plot(x_val, y_val, color='red', label='Polynomial')
plt.plot(x_val, y_diff_1_val, color='yellow', label='1st Derivative')
plt.plot(x_val, y_diff_2_val, color='green', label='2nd Derivative')
plt.scatter(xv, yv)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
