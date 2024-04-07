import sympy as sp

x = sp.Symbol('x')
n = 100

def trapezoidal(f, a, b):
    h = (b - a) / (n - 1)
    xv = [a + h * i for i in range(n)]
    yv = [f.subs(x, i) for i in xv]

    s = yv[0] + yv[n - 1] + 2 * sum(yv[1:-1])
    s = s * h / 2
    return s

def simpson_1_3(f, a, b):
    h = (b - a) / (n - 1)
    xv = [a + h * i for i in range(n)]
    yv = [f.subs(x, i) for i in xv]

    s = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            s = s + yv[i]
        elif i % 2 == 0:
            s = s + 2 * yv[i]
        else:
            s = s + 4 * yv[i]
    s = s * h / 3
    return s

def simpson_3_8(f, a, b):
    h = (b - a) / (n - 1)
    xv = [a + h * i for i in range(n)]
    yv = [f.subs(x, i) for i in xv]

    s = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            s = s + yv[i]
        elif i % 3 == 0:
            s = s + 2 * yv[i]
        else:
            s = s + 3 * yv[i]
    s = s * h * 3 / 8
    return s

def integrate(y, a, b):
    print('y = ', y)

    # Built-in function
    res = sp.integrate(y, (x, a, b))
    print('Built-in function: ', round(res, 4))

    # Trapezoidal rule
    res = trapezoidal(y, a, b)
    print('Trapezoidal rule: ', round(res, 4))

    # Simpson's 1/3 rule
    res = simpson_1_3(y, a, b)
    print('Simpson\'s 1/3 rule: ', round(res, 4))

    # Simpson's 3/8 rule
    res = simpson_3_8(y, a, b)
    print('Simpson\'s 3/8 rule: ', round(res, 4))
    print()

integrate(y = sp.sympify('log(2, x)'), a = 4, b = 5.2)
integrate(y = sp.sympify('exp(-x**2)'), a = 0, b = 1)
integrate(y = sp.sympify('x**2 / (1 + x**3)'), a = 0, b = 1)
