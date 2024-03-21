import sympy as sp
x = sp.Symbol('x')

def fun(i, eq, xvalues):
    interval_count = 0
    for j in range(1, len(xvalues)):
        if i <= xvalues[j]:
            break
        interval_count += 1
    t_eq = eq[interval_count]
    return t_eq.subs(x, i)

def cubic_spline(xvalues, yvalues):
    n = len(xvalues)
    var = []
    for i in range(4*(n-1)):
        var.append(sp.Symbol('x' + str(i)))

    eqn = []
    j = 0
    for i in range(0, 4*(n-1), 4):
        t = var[i] * x**3 + var[i+1] * x**2 + var[i+2] * x + var[i+3]
        eqn.append(sp.Eq(t.subs(x, xvalues[j]), yvalues[j]))
        eqn.append(sp.Eq(t.subs(x, xvalues[j+1]), yvalues[j+1]))

        if i == 0:
            eqn.append(sp.Eq(sp.diff(sp.diff(t, x), x).subs(x, xvalues[0]), 0))

        if i != 4*n - 8:
            t1 = var[i+4] * x**3 + var[i+5] * x**2 + var[i+6] * x + var[i+7]
            eqn.append(sp.Eq(sp.diff(t, x).subs(x, xvalues[j+1]), sp.diff(t1, x).subs(x, xvalues[j+1])))
            eqn.append(sp.Eq(sp.diff(sp.diff(t, x), x).subs(x, xvalues[j+1]), sp.diff(sp.diff(t1, x), x).subs(x, xvalues[j+1])))

        if i == 4*(n-1) - 4:
            eqn.append(sp.Eq(sp.diff(sp.diff(t, x), x).subs(x, xvalues[n-1]), 0))

        j = j + 1

    solution = sp.solve(eqn, var)

    eq = []
    for i in range(0, 4*(n-1), 4):
        t = solution[var[i]] * x**3 + solution[var[i+1]] * x**2 + solution[var[i+2]] * x + solution[var[i+3]]
        eq.append(t)

    print("Equations")
    for i in range(len(eq)):
        print(eq[i], ' : ', xvalues[i], ' < x <= ', xvalues[i+1])

    xp = float(input("Enter the value of x: "))
    print("f(", xp, ") = ", fun(xp, eq, xvalues))

    import numpy as np
    import matplotlib.pyplot as plt

    x_val = np.linspace(min(xvalues), max(xvalues), 1000)
    x_val = np.linspace(0, 3, 1000)
    y_val = [fun(i, eq, xvalues) for i in x_val]

    plt.plot(x_val, y_val, label = 'Cubic spline interpolation (Manual)')

    from scipy.interpolate import CubicSpline
    cs = CubicSpline(xvalues, yvalues)

    x_interp = np.linspace(0, 3, 1000)
    y_interp = cs(x_interp)

    plt.plot(x_interp, y_interp, label = 'Cubic spline interpolation (Built-in)')
    plt.scatter(xvalues, yvalues, color = 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    xvalues = [0, 1, 2, 3]
    yvalues = [1, 2, 9, 28]
    cubic_spline(xvalues, yvalues)

if __name__ == '__main__':
    main()
