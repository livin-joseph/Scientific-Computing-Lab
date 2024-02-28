import sympy as sp
from prettytable import PrettyTable

def regula_falsi(eq, low_lim, upp_lim):
    x = sp.Symbol("x")

    """
    eq = input("Enter an equation with one variable\n")
    eq = sp.sympify(eq)
    """

    a = low_lim
    b = upp_lim
    if eq.subs(x, a) * eq.subs(x, b) < 0:
        print("Regula falsi method can be applied")
    else:
        print("Regula falsi method cannot be applied")
        return
    
    table = PrettyTable(['a', 't', 'b', 'f(a)', 'f(t)', 'f(b)'])
    
    t = (a * eq.subs(x, b) - b * eq.subs(x, a)) / (eq.subs(x, b) - eq.subs(x, a))
    table.add_row([round(a, 4), round(t, 4), round(b, 4), round(eq.subs(x, a), 4), round(eq.subs(x, t), 4), round(eq.subs(x, b), 4)])
    while round(eq.subs(x, t), 4) != 0:
        if round(eq.subs(x, t), 4) / abs(round(eq.subs(x, t), 4)) == round(eq.subs(x, a), 4) / abs(round(eq.subs(x, a), 4)):
            a = t
        else:
            b = t
        t = (a * eq.subs(x, b) - b * eq.subs(x, a)) / (eq.subs(x, b) - eq.subs(x, a))
        table.add_row([round(a, 4), round(t, 4), round(b, 4), round(eq.subs(x, a), 4), round(eq.subs(x, t), 4), round(eq.subs(x, b), 4)])

    print(table)
    print("Solution to", eq, ": ", round(t, 4))

if __name__ == '__main__':
    eq = sp.sympify(input("Enter an equation with one variable\n"))
    low_lim = int(input("Enter the lower limit of the interval: "))
    upp_lim = int(input("Enter the upper limit of the interval: "))
    regula_falsi(eq, low_lim, upp_lim)
