# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:42:53 2024

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

def heaviside(x):
    """See http://stackoverflow.com/a/15122658/554319"""
    y = 0.5 * (np.sign(x) + 1)
    #y[np.diff(y) >= 0.5] = np.nan
    return y

x = np.linspace(-1000000000000, 1000000000000, 10001)
#plt.plot(x, heaviside(x))
plt.scatter(x, heaviside(x))
plt.ylim(-1, 2)
