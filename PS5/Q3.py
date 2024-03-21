def LU(matrix):
    import numpy as np

    n = matrix.shape[0]
    lower = np.zeros((n,n))
    upper = np.zeros((n,n))
    
    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += lower[i, j] * upper[j, k]
            upper[i, k] = matrix[i, k] - sum
        
        for k in range(i, n):
            if i == k:
                lower[i, i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += lower[k, j] * upper[j, i]
                lower[k, i] = (matrix[k, i] - sum) / upper[i, i]

    return lower, upper

def LU1(mat):
    import numpy as np
    import sympy as sp
    
    n = mat.shape[0]

    var_list = []
    var_mat_lower = []
    var_mat_upper = []

    k = 0
    # Lower triangular matrix
    for i in range(0, n):
        t = []
        for j in range(0, i):
            t.append(sp.Symbol('x' + str(k)))
            k += 1
        var_list = var_list + t
        t.append(1)
        for m in range(i+1, n):
            t.append(0)
        var_mat_lower.append(t)
    # Upper triangular matrix
    for i in range(0, n):
        t = []
        for j in range(0, i):
            t.append(0)
        for m in range(i, n):
            t.append(sp.Symbol('x' + str(k)))
            k += 1
            var_list = var_list + [t[-1]]
        var_mat_upper.append(t)
    
    print(var_mat_lower, var_mat_upper)
    matrix = np.dot(var_mat_lower, var_mat_upper)

    eq_list = []
    for i in range(0, n):
        for j in range(0, n):
            eq_list.append(sp.Eq(mat[i, j], matrix[i, j]))

    solution = list(sp.solve(eq_list, var_list)[0])
    print(solution)

    k = 0
    final_low_mat = []
    for i in range(0, n):
        t = []
        for j in range(0, i):
            t.append(solution[k])
            k += 1
        t.append(1)
        for m in range(i+1, n):
            t.append(0)
        final_low_mat.append(t)

    final_low_mat = np.matrix(final_low_mat)

    final_upp_mat = []
    for i in range(0, n):
        t = []
        for j in range(0, i):
            t.append(0)
        for m in range(i, n):
            t.append(solution[k])
            k += 1
        final_upp_mat.append(t)

    final_upp_mat = np.matrix(final_upp_mat)

    return final_low_mat, final_upp_mat

def LU2(mat):
    import scipy as sp

    P, L, U = sp.linalg.lu(mat)
    return L, U

def main():
    import numpy as np

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix (row-wise)")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(float(input()))
        mat.append(arr)

    mat = np.matrix(mat)
    print("Matrix")
    print(mat)

    if np.linalg.det(mat) == 0:
        print("Matrix is singular")
        print("LU Decomposition cannot be applied")
        return
    
    L, U = LU1(mat)

    print("LU Decomposition")
    print("L")
    print(L)
    print("U")
    print(U)
    print("L * U")
    print(np.dot(L, U))

if __name__ == '__main__':
    main()
