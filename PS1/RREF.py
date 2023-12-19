# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:31:11 2023

@author: livin
"""

def matrixToRREF(mat, index = 0):
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if mat[i][j] != 0:
                

def main():
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

    mat = np.array(mat)
    print(mat)
