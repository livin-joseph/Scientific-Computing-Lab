import sympy as sp

x, y = sp.symbols('x y')

def euler(f, xi, yi, xt):
    h = 0.01
    print('x \t y \t dy/dx \t y_new')
    print(xi, '\t', yi, '\t', f.subs(x, xi).subs(y, yi), '\t', yi + h * f.subs(x, xi).subs(y, yi))
    while xi != xt:
        yi = yi + h * f.subs(x, xi).subs(y, yi)
        xi = round(xi + h, 4)
        print(xi, '\t', yi, '\t', f.subs(x, xi).subs(y, yi), '\t', yi + h * f.subs(x, xi).subs(y, yi))
    return yi

rhs = sp.sympify('x - y + cos(x + y)')

result = euler(rhs, xi = 0.1, yi = 1, xt = 1.7)
print('y(1.7) = ', result)
