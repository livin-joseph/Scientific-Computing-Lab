import sympy as sp

x, y = sp.symbols('x y')

def runge_kutta_3_ynew(f, xi, yi):
    h = 0.01

    k1 = h * f.subs(x,xi).subs(y,yi)
    
    k2 = h * f.subs(x, xi + h/2).subs(y, yi + k1/2)

    k_ = h * f.subs(x, xi + h).subs(y, yi + k1)

    k3 = h * f.subs(x, xi + h).subs(y, yi + k_)

    return yi + 1/6 * (k1 + 4*k2 + k3)

def runge_kutta_3(f, xi, yi, xt):
    h = 0.01

    print('x \t y \t y_new')
    print(xi, '\t', yi, '\t', runge_kutta_3_ynew(f, xi, yi))
    while xi != xt:
        yi = runge_kutta_3_ynew(f, xi, yi)
        xi = round(xi + h, 4)
        print(xi, '\t', yi, '\t', runge_kutta_3_ynew(f, xi, yi))
    return yi


rhs = sp.sympify('(x * y) / (x**2 + y**2 - x * y)')

result = runge_kutta_3(rhs, xi = 0, yi = 10, xt = 3)
print('y(3) = ', result)
