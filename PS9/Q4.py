import sympy as sp

x, y = sp.symbols('x y')

def runge_kutta_4_ynew(f, xi, yi):
    h = 0.01

    k1 = h * f.subs(x,xi).subs(y,yi)
    
    k2 = h * f.subs(x, xi + h/2).subs(y, yi + k1/2)

    k3 = h * f.subs(x, xi + h/2).subs(y, yi + k2/2)

    k4 = h * f.subs(x, xi + h).subs(y, yi + k3)

    return yi + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

def runge_kutta_4(f, xi, yi, xt):
    h = 0.01

    print('x \t y \t y_new')
    print(xi, '\t', yi, '\t', runge_kutta_4_ynew(f, xi, yi))
    while xi != xt:
        yi = runge_kutta_4_ynew(f, xi, yi)
        xi = round(xi + h, 4)
        print(xi, '\t', yi, '\t', runge_kutta_4_ynew(f, xi, yi))
    return yi


rhs = sp.sympify('x * y + x - y**3')

result = runge_kutta_4(rhs, xi = 1, yi = -4, xt = 2.5)
print('y(2.5) = ', result)
