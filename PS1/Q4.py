# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:25:02 2023

@author: livin
"""

import numpy as np
import sympy as sp

eqn = int(input("Enter the number of equations: "))
var = int(input("Enter the number of variables: "))

coeff_matrix = []
const_matrix = []

print("Enter the elements of the coefficient matrix (row-wise)")
for i in range(eqn):
    arr = []
    for j in range(var):
        arr.append(int(input()))
    coeff_matrix.append(arr)

coeff_matrix = np.array(coeff_matrix)

print("Enter the elements of the constant matrix (row-wise)")
for i in range(eqn):
    const_matrix.append([int(input())])

const_matrix = np.array(const_matrix)

print("Augumented matrix")
aug_matrix = np.concatenate((coeff_matrix,const_matrix), axis=1)
print(aug_matrix)

rankA = np.linalg.matrix_rank(coeff_matrix)
rankAB = np.linalg.matrix_rank(aug_matrix)

mat = aug_matrix
mat = np.mat(mat)
mat = sp.Matrix(mat)
print("RREF")
mat = mat.rref()[0]
mat = mat.tolist()
aug_matrix = np.array(mat)
print(aug_matrix)

def leadingOne(aug_matrix, i, j):
    for x in range(j):
        if aug_matrix[i][x] != 0:
            return False
    return True

print("Rank of A: ", rankA)
print("Rank of [A:B]: ", rankAB)

if rankA == rankAB and rankA == var:
    print("Linear system has unique solution")
    soln = []
    for i in range(len(aug_matrix)):
        soln.append(aug_matrix[i][var])
        if i >= var-1:
            break
    print("Solution")
    for i in range(len(soln)):
        print("x"+str(i+1), "=", soln[i])
elif rankA == rankAB:
    print("Linear system has infinitely many solutions")
    variables = [i for i in range(var)]
    free = []
    for j in range(var):
        freeFlag = True
        for i in range(eqn):
            if aug_matrix[i][j] == 1 and leadingOne(aug_matrix, i, j) == True:
                freeFlag = False
                break
        if freeFlag == True:
            free.append(j)
    basic = [x for x in variables if x not in free]
    soln = []
    for i in range(var):
        if i in free:
            soln.append("x"+str(i+1))
        else:
            for k in range(eqn):
                if aug_matrix[k][i] == 1:
                    rowIndex = k
                    break
            st = str(aug_matrix[rowIndex][var])
            for j in range(var):
                if aug_matrix[rowIndex][j] == 1 and leadingOne(aug_matrix, rowIndex, j) == True:
                    continue
                else:
                    st = st + " - " + "(" + str(aug_matrix[i][j]) + "x" + str(j+1) + ")"
            soln.append(st)
    freevar = ["x"+str(j+1) for j in free]
    basicvar = ["x"+str(j+1) for j in basic]
    print("Free variables: ", freevar)
    print("Basic variables: ", basicvar)
    print("Solution form")
    print(soln)
else:
    print("Linear system has no solution")
