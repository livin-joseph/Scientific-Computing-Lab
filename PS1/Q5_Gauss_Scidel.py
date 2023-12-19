# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:33:53 2023

@author: livin
"""

import numpy as np

mat = []

n = int(input("Enter number of variables/equations: "))

coeff_matrix = []
const_matrix = []

print("Enter the elements of the coefficient matrix (row-wise)")
for i in range(n):
    arr = []
    for j in range(n):
        arr.append(int(input()))
    coeff_matrix.append(arr)

coeff_matrix = np.array(coeff_matrix)

print("Enter the elements of the constant matrix (row-wise)")
for i in range(n):
    const_matrix.append([int(input())])

const_matrix = np.array(const_matrix)
