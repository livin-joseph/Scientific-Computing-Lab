# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:18:44 2023

@author: 22pd20
"""

"""
import sys
sys.path.append("C:/Users/livin/GitHub/Scientific-Computing-Lab/PS1")
import Q3_Matrix_to_RREF as rref
"""

import matplotlib.pyplot as plt

import numpy as np

def f1(x):
    #if x > 0:
    return x*x

def f2(x):
    #if x == 0:
    return 1
    
def f3(x):
    #if x > 0:
    return -x-1

x1 = np.linspace(1, 0, 1000)
x3 = np.linspace(0, -1, 1000)


plt.plot(x1,f1(x1))
plt.scatter(0,0)
plt.plot(x3,f3(x3))
plt.show()
