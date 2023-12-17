# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:45:34 2023

@author: livin
"""

def check1(mat):
    # All leading entries should be 1
    for i in mat:
        for j in i:
            if j == 1:
                break
            if j == 0:
                continue
            else:
                print("Unsatisfied property: All leading entries should be 1")
                return False
    return True

def check2(mat):
    # All zero rows should be at the bottom of the matrix
    flag = False
    zeroRowFound = False
    for i in mat:
        if zeroRowFound == False:
            flag = True
            for j in i:
                if j != 0:
                    flag = False
                    break
            if flag == True:
                # First zero row found
                zeroRowFound = True
        else:
            for j in i:
                if j != 0:
                    print("Unsatisfied property: All zero rows should be at the bottom of the matrix")
                    return False
    return True

def check3(mat):
    # Each leading 1 of a row is in a column to the right of the leading 1 of the row above it
    columnIndex = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                if j <= columnIndex:
                    print("Unsatisfied property: Each leading 1 of a row is in a column to the right of the leading 1 of the row above it")
                    return False
                else:
                    columnIndex = j
                    break
            if mat[i][j] == 0:
                continue
    return True

def RREFcheck(mat):
    # Each leading 1 is the only nonzero entry in its column
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                for k in range(len(mat)):
                    if mat[k][j] != 0 and k != i:
                        print("Unsatisfied property: Each leading 1 of a row is in a column to the right of the leading 1 of the row above it")
                        return False
                break                
    return True

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

REF = False
if check1(mat) == True and check2(mat) == True and check3(mat) == True:
    REF = True
    print("The Matrix is in REF")
else:
    print("The Matrix is not in REF")

if REF == True and RREFcheck(mat) == True:
    print("The Matrix is in RREF")
else:
    print("The Matrix is not in RREF")
