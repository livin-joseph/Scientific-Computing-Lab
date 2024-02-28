import sympy as sp
from prettytable import PrettyTable

def fixed_point(eq, low_lim, upp_lim):
    x = sp.Symbol("x")

    """
    eq = input("Enter an equation with one variable\n")
    eq = sp.sympify(eq)
    """
   
    a = low_lim
    b = upp_lim
    if eq.subs(x, a) * eq.subs(x, b) < 0:
        print("Fixed point iteration method can be applied")
    else:
        print("Fixed point iteration method cannot be applied")
        return
    
    table = PrettyTable(['an', 'f(an)'])
    
    if abs(eq.subs(x, a)) < abs(eq.subs(x, b)):
        t = a
    else:
        t = b

    y = sp.Symbol('y')

    degree = sp.degree(eq, x)
    f = sp.solve(sp.Eq(0, eq.subs(x**degree, y)), y)[0]
    f = sp.root(f, degree)
    table.add_row([round(t, 4), round(f.subs(x, t), 4)])
    while round(f.subs(x, t), 4) != round(t, 4):
        t = f.subs(x, t)
        table.add_row([round(t, 4), round(f.subs(x, t), 4)])

    print(table)
    print("Solution to", eq, ": ", round(t, 4))

if __name__ == '__main__':
    eq = sp.sympify(input("Enter an equation with one variable\n"))
    low_lim = int(input("Enter the lower limit of the interval: "))
    upp_lim = int(input("Enter the upper limit of the interval: "))
    fixed_point(eq, low_lim, upp_lim)
