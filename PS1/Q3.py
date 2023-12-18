# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:56:10 2023

@author: livin
"""

import sympy as sp
import numpy as np

mat = []

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter the elements of the matrix (row-wise)")

for i in range(r):
    arr = []
    for j in range(c):
        arr.append(int(input()))
    mat.append(arr)

mat = sp.Matrix(mat)
RREF = mat.rref()[0]

mat = np.array(mat.tolist())
RREF = np.array(RREF.tolist())

print("Original matrix")
print(mat)
print("RREF")
print(RREF)
