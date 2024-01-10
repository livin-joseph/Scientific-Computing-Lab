# -*- coding: utf-8 -*-
"""
Created on Mon Jan 1 21:35:50 2024

@author: livin
"""

def main():
    import numpy as np
    import sympy as sp

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(input()))
        mat.append(arr)

    mat = np.array(mat)
    mat = sp.Matrix(mat)
    print(mat)
    
    ev = np.linalg.eig(mat)
    print("Eigen values")
    eigenvalues = [round(x,4) for x in ev[0]]
    print(eigenvalues)
    print("Eigen vectors")
    for j in range(len(ev[1])):
        eigenvector = []
        for i in range(len(ev[1])):
            eigenvector.append(round(ev[1][i][j],4))
        print(eigenvector)
    
    return

    """
    import sys
    sys.path.append("C:/Users/livin/GitHub/Scientific-Computing-Lab/PS1")
    import Q3_Matrix_to_RREF as rref
    """

    lam = sp.Symbol('lambda')
    newmat = mat - lam * sp.eye(n)
    char_eq = newmat.det()
    print("Characteristic equation: ",char_eq)
    ev = sp.solveset(char_eq, lam)
    ev = [round(i, 2) for i in ev]
    print("Eigenvalues: ", ev)

    for i in ev:
        tempmat = newmat.subs(lam, i)
        tempmat = tempmat.col_insert(n, sp.Matrix([0] * n))
        evec = sp.linsolve(tempmat)
        print("Eigenvectors corresponding to eigenvalue ", i, ": ", evec)

if __name__ == '__main__':
    main()
