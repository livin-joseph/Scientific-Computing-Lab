# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:35:50 2024

@author: livin
"""

def main():
    import numpy as np

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(float(input()))
        mat.append(arr)

    mat = np.array(mat)
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

    import sys
    sys.path.append("C:/Users/livin/GitHub/Scientific-Computing-Lab/PS1")
    import Q3_Matrix_to_RREF as rref
    
    charPolyCoeffs = [1, -sum([mat[x][x] for x in range(len(mat))])]
    a11 = mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]
    a22 = mat[0][0] * mat[2][2] - mat[2][0] * mat[0][0]
    a33 = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
    charPolyCoeffs.append(a11 + a22 + a33)
    charPolyCoeffs.append(np.linalg.det(mat))
    
    eigenvalues = np.roots(charPolyCoeffs)
    print("Eigen values")
    print(eigenvalues)

if __name__ == '__main__':
    main()
