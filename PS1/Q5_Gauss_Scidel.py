# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:33:53 2023

@author: livin
"""

def diagdom(coeff_matrix, const_matrix):
    import numpy as np
    import DiagonallyDominant as dd
    eqn = coeff_matrix.tolist()
    const = const_matrix.tolist()
    
    for i in range(len(eqn)):
        for j in range(len(eqn)):
            max1 = max(eqn[j])
            index = eqn[j].index(max1)
            eqn[index], eqn[j] = eqn[j], eqn[index]
            const[index], const[j] = const[j], const[index]
    
    new_coeff_matrix = np.array(eqn)
    new_const_matrix = np.array(const)
    new_aug_matrix = np.concatenate((new_coeff_matrix, new_const_matrix), axis = 1)

    flag = dd.diagonallyDominant(new_coeff_matrix)
    if flag == True:
        return tuple([True, new_aug_matrix])
    else:
        return tuple([False])
    
def gauss_scidel(aug_matrix, var):
    for i in range(len(aug_matrix)):
        temp = aug_matrix[i][-1]
        for j in range(len(aug_matrix[0])-1):
            if i == j:
                continue
            temp = temp - aug_matrix[i][j] * var[j]
        temp = temp / aug_matrix[i][i]
        var[i] = temp
    return var

def main():
    import numpy as np

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

    temp = diagdom(coeff_matrix, const_matrix)
    
    if temp[0] == False:
        print("Given equations cannot be converted into a diagonally dominant matrix")
        import sys
        sys.exit()

    aug_matrix = temp[1]
    print("Given equations are converted into a diagonally dominant matrix")
    print("Augumented matrix")
    print(aug_matrix)
    
    print("Enter initial values of variables")
    var = []
    for i in range(len(aug_matrix[0])-1):
        var.append(int(input()))

    import copy
    temp_var = []
    count = 1
    while temp_var != var:
        temp_var = copy.deepcopy(var)
        var = gauss_scidel(aug_matrix, var)
        print("Iteration ", count)
        count += 1
        print(var)
    
    print("Solution")
    print(var)

if __name__ == '__main__':
    main()
