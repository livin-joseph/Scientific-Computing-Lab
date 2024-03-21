def lagrange(xvalues, yvalues):
    n = len(xvalues)

    import sympy as sp
    x = sp.Symbol('x')

    eqn = 0
    for i in range(len(xvalues)):
        s = 1
        for j in range(len(xvalues)):
            if i == j:
                continue
            s = s * (x - xvalues[j]) / (xvalues[i] - xvalues[j])
        s = s * yvalues[i]
        eqn = eqn + s
    eqn = eqn.expand()
    
    print(eqn)


    import numpy as np
    import matplotlib.pyplot as plt

    x_val = np.linspace(min(xvalues), max(xvalues), 1000)
    y_val = []

    for i in x_val:
        y_val.append(0)

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
    lagrange(xvalues, yvalues)

if __name__ == '__main__':
    main()
