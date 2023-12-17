# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:56:10 2023

@author: livin
"""

def ConvertToRREF(a):
    n = len(a)
    i = 0
    j = 0
    k = 0
    c = 0
 
    # Performing elementary operations
    for i in range(n):
        if (a[i][i] == 0):
 
            c = 1
            while ((i + c) < n and a[i + c][i] == 0):
                c += 1
            if ((i + c) == n):
                 break
 
            j = i
            for k in range(1 + n):
 
                temp = a[j][k]
                a[j][k] = a[j+c][k]
                a[j+c][k] = temp
 
        for j in range(n):
 
            # Excluding all i == j
            if (i != j):
                # Converting Matrix to reduced row
                # echelon form(diagonal matrix)
                p = a[j][i] / a[i][i]
 
                k = 0
                for k in range(n):
                    a[j][k] = a[j][k] - (a[i][k]) * p

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

ConvertToRREF(mat)
print(mat)