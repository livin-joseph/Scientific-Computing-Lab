# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:05:28 2024

@author: Administrator
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)
c = np.random.standard_normal(100)

img = ax.scatter(x, y, z, c=c, cmap = plt.hot())
fig.colorbar(img)
plt.show()

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)

# Z = np.power(X, 2) - np.power(Y, 2)
Z = np.sin(X) * np.cos(Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = 'plasma')
plt.show()
