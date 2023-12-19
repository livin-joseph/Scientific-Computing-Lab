# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:25:02 2023

@author: livin
"""

def leadingOne(aug_matrix, i, j):
    for x in range(j):
        if aug_matrix[i][x] != 0:
            return False
    return True

def solveLinearSystem(coeff_matrix, const_matrix):
    import numpy as np
    import sympy as sp
    
    eqn = len(coeff_matrix)
    var = len(coeff_matrix[0])
    
    aug_matrix = np.concatenate((coeff_matrix,const_matrix), axis=1)

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

    print("Rank of A: ", rankA)
    print("Rank of [A:B]: ", rankAB)
    
    solution = ()

    if rankA == rankAB and rankA == var:
        solution = ('unique')
        soln = []
        for i in range(len(aug_matrix)):
            soln.append(aug_matrix[i][var])
            if i >= var-1:
                break
        solution = (solution, soln)
    elif rankA == rankAB:
        solution = ('infinite')
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
                    if j in basic:
                        continue
                    if aug_matrix[rowIndex][j] == 1 and leadingOne(aug_matrix, rowIndex, j) == True:
                        continue
                    else:
                        st = st + " - " + "(" + str(aug_matrix[rowIndex][j]) + "x" + str(j+1) + ")"
                soln.append(st)
        freevar = ["x"+str(j+1) for j in free]
        basicvar = ["x"+str(j+1) for j in basic]
        solution = (solution, soln, basicvar, freevar)
        print(solution)
    else:
        solution = ('no solution')
    return solution

def main():
    import numpy as np

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

    solution = solveLinearSystem(coeff_matrix, const_matrix)
    
    if solution[0] == 'unique':
        print("Linear system has unique solution")
        print("Solution")
        soln = solution[1]
        for i in range(len(soln)):
            print("x"+str(i+1), "=", soln[i])
    elif solution[0] == 'infinite':
        print("Linear system has infinitely many solutions")
        basicvar = solution[2]
        freevar = solution[3]
        print("Basic variables: ", basicvar)
        print("Free variables: ", freevar)
        print("Solution form")
        print(solution[1])
    else:
        print("Linear system has no solution")

if __name__ == '__main__':
    main()
