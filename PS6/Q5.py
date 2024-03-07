def lagrange(xx, yy, x):
    y = 0
    for i in range(len(xx)):
        t = 1
        for j in range(len(xx)):
            if(i != j):
                t = t * ((x - xx[j]) / (xx[i] - xx[j]))
        t = t * yy[i]
        y = y + t
    return y

x_values = [45, 46, 50, 55, 65]
y_values = [114.84, 110.525632, 96.16, 83.32, 68.48]

print("Premium for policy with respect to age of maturing")
print("Age 60: ", lagrange(x_values, y_values, 60))
print("Age 63: ", lagrange(x_values, y_values, 63))
