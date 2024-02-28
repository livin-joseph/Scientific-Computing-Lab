import sympy as sp
from prettytable import PrettyTable

def newton_raphson(eq, low_lim, upp_lim):
    x = sp.Symbol("x")

    """
    eq = input("Enter an equation with one variable\n")
    eq = sp.sympify(eq)
    """

    h = eq / sp.diff(eq)

    table = PrettyTable(['x(n)', 'x(n+1)'])
    
    xn = (low_lim + upp_lim) / 2
    xn1 = round(xn - h.subs(x, xn), 4)
    table.add_row([xn, xn1])

    while round(xn, 4) != round(xn1, 4):
        xn = round(xn1, 4)
        xn1 = round(xn - h.subs(x, xn), 4)
        table.add_row([xn, xn1])

    print(table)
    print("Solution to", eq, ": ", round(xn, 4))

if __name__ == '__main__':
    eq = sp.sympify(input("Enter an equation with one variable\n"))
    low_lim = int(input("Enter the lower limit of the interval: "))
    upp_lim = int(input("Enter the upper limit of the interval: "))
    newton_raphson(eq, low_lim, upp_lim)
