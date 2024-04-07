import sympy as sp

x, y = sp.symbols('x y')

def milne(f, xv, yv, xp):
    if not len(xv) == len(yv) == 4:
        return
    h = xv[1] - xv[0]
    y_diff = [f.subs(x, xv[i]).subs(y, yv[i]) for i in range(len(xv))]

    yp = yv[0] + 4/3 * h * (2 * y_diff[1] - y_diff[2] + 2 * y_diff[3])

    xv.append(xp)
    yv.append(yp)
    y_diff.append(f.subs(x, xv[-1]).subs(y, yv[-1]))

    yc = yv[2] + 1/3 * h * (y_diff[2] + 4 * y_diff[3] + y_diff[4])

    y_new = y_curr = yc
    if round(yp, 4) != round(yc, 4):
        while(True):
            f_4 = f.subs(x, xp)
            f_4 = f_4.subs(y,y_curr)
            y_new = yv[2] + 1/3 * h * (y_diff[2] + 4 * y_diff[3] + f_4)
            if round(y_new, 4) == round(y_curr, 4):
                break
            else:
                y_curr = y_new

    return y_new


f = sp.sympify('(1 + x**2) * y**2 / 2')

xv = [0, 0.1, 0.2, 0.3]
yv = [1, 1.06, 1.12, 1.21]

yi = milne(f, xv, yv, xp = 0.4)
print('y(0.4) = ', yi)
