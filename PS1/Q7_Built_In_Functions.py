# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:22:00 2023

@author: livin
"""

def main():
    import numpy as np
    import sympy as sp

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

    aug_matrix = np.concatenate((coeff_matrix, const_matrix), axis = 1)
    print("Augumented Matrix")
    print(aug_matrix)
    
    aug_matrix = sp.Matrix(aug_matrix.tolist())
    rref = aug_matrix.rref()[0]
    rref = np.array(rref.tolist())
    print("RREF")
    print(rref)
    
    x = np.linalg.solve(coeff_matrix, const_matrix) # Solves Ax = b
    print("Solution to the linear system")
    print(x)

if __name__ == '__main__':
    main()
