# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:45:34 2023

@author: livin
"""

def REFcheck1(mat):
    # All leading entries should be 1
    for i in mat:
        for j in i:
            if j == 1:
                break
            if j == 0:
                continue
            else:
                return False
    return True

def REFcheck2(mat):
    # All zero rows should be at the bottom of the matrix
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
                    return False
    return True

def REFcheck3(mat):
    # Each leading 1 of a row is in a column to the right of the leading 1 of the row above it
    columnIndex = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                if j <= columnIndex:
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
                        return False
                break                
    return True

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

    REF = False
    if REFcheck1(mat) == True and REFcheck2(mat) == True and REFcheck3(mat) == True:
        REF = True
        print("The Matrix is in REF")
    else:
        print("The Matrix is not in REF")
        if REFcheck1(mat) == False:
            print("Unsatisfied property: All leading entries should be 1")
        if REFcheck2(mat) == False:
            print("Unsatisfied property: All zero rows should be at the bottom of the matrix")
        if REFcheck3(mat) == False:
            print("Unsatisfied property: Each leading 1 of a row is in a column to the right of the leading 1 of the row above it")

    if REF == True and RREFcheck(mat) == True:
        print("The Matrix is in RREF")
    else:
        print("The Matrix is not in RREF")
        if REF == False:
            print("Unsatisfied property: The matrix is not in REF")
        if RREFcheck(mat) == False:
            print("Unsatisfied property: Each leading 1 of a row is in a column to the right of the leading 1 of the row above it")

if __name__ == '__main__':
    main()
