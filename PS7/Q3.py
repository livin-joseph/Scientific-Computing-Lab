def inverse_lagrange(xvalues, yvalues):
    xvalues, yvalues = yvalues, xvalues

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

    print("Interpolating polynomial: ", eqn)

    import numpy as np
    import matplotlib.pyplot as plt

    x_val = np.linspace(min(xvalues), max(xvalues), 1000)
    y_val = [eqn.subs(x, t) for t in x_val]

    plt.plot(x_val, y_val)
    plt.scatter(xvalues, yvalues)
    plt.show()

def main():
    xvalues = [0, 1, 2, 3]
    yvalues = [1, 2, 9, 28]
    inverse_lagrange(xvalues, yvalues)

if __name__ == '__main__':
    main()
