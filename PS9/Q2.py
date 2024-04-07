import sympy as sp
import pandas as pd

x, y = sp.symbols('x y')

df = pd.DataFrame(columns=['x', 'y', 'dy/dx', 'dy/dx_n', 'yn_c'])

def modified_euler(f, xi, yi, xt):
    h = 0.01
    
    dydx = f.subs(x, xi).subs(y, yi)
    dydxn = f.subs(x, xi + h).subs(y, yi + h * dydx)

    t = [xi, yi, dydx, dydxn, yi + h * (dydx + dydxn) / 2]
    df.loc[len(df)] = t

    xi = xi + h
    yi = t[-1]
    
    while xi != xt:
        dydx = f.subs(x, xi).subs(y, yi)
        dydxn = f.subs(x, xi + h).subs(y, yi + h * (dydx + dydxn) / 2)
        
        t = [xi, yi, dydx, dydxn, yi + h * (dydx + dydxn) / 2]
        df.loc[len(df)] = t

        xi = round(xi + h, 4)
        yi = t[-1]
    return yi

rhs = sp.sympify('x**2 - y + 2*x + 4*y')

result = modified_euler(rhs, xi = 0.3, yi = -0.18, xt = 2.5)
print(df)
print('y(2.5) = ', result)
