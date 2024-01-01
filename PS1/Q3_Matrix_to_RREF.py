# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:31:11 2023

@author: livin
"""

def leadingOne(aug_matrix, i, j):
    for x in range(j):
        if aug_matrix[i][x] != 0:
            return False
    return True

def REFtoRREF(mat):
    for i in range(len(mat)-1, 0, -1):
        for j in range(len(mat[i])):
            if mat[i][j] == 1 and leadingOne(mat, i, j) == True:
                for k in range(i-1, -1, -1):
                    factor = mat[k][j]
                    mat[k] = [ mat[k][x] - factor * mat[i][x] for x in range(len(mat[0])) ]
    return mat

def matrixToREF(mat):
    index = 0
    for j in range(len(mat[0])):
        flag = False
        for i in range(len(mat)):
            if mat[i][j] != 0 and flag == False and i >= index:
                flag = True
                factor = mat[i][j]
                mat[i] = [ x / factor for x in mat[i]]
                import copy # Swapping rows
                temp = copy.deepcopy(mat[index])
                mat[index] = mat[i]
                mat[i] = temp
                break
        for i in range(index + 1, len(mat)):
            factor = mat[i][j]
            mat[i] = [ mat[i][x] - factor * mat[index][x] for x in range(len(mat[0])) ]
        if flag == True:
            index += 1
    return mat

def main():
    import numpy as np

    mat = []

    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    print("Enter the elements of the matrix (row-wise)")

    for i in range(r):
        arr = []
        for j in range(c):
            arr.append(float(input()))
        mat.append(arr)

    mat = np.array(mat)

    print(mat)
    ref = matrixToREF(mat)
    print(ref)
    rref = REFtoRREF(ref)
    print(rref)
    
if __name__ == '__main__':
    main()
