def cholesky(matrix):
    import numpy as np
    import math

    n = matrix.shape[0]
    lower = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0
            if i == j:
                for k in range(j):
                    sum1 += pow(lower[j, k], 2)
                lower[j, j] = math.sqrt(matrix[j, j] - sum1)
            else:
                for k in range(j):
                    sum1 += (lower[i, k] * lower[j, k])
                if(lower[j, j] > 0):
                    lower[i, j] = (matrix[i, j] - sum1) / lower[j, j]

    lower = np.matrix(lower)
    return lower, lower.T

def cholesky1(mat):
    import numpy as np
    import sympy as sp

    n = mat.shape[0]
    no_of_var = int(n * (n + 1) / 2)

    var_list = []
    var_mat = []

    k = 0
    for i in range(0, n):
        t = []
        for j in range(0, i+1):
            t.append(sp.Symbol('x' + str(k)))
            k += 1
        var_list = var_list + t
        for m in range(i+1, n):
            t.append(0)
        var_mat.append(t)
    
    lowmat = np.matrix(var_mat)

    new_mat = np.dot(lowmat, lowmat.T)
    print(new_mat, var_list)

    eq_list = []
    for i in range(0, n):
        for j in range(0, n):
            eq_list.append(sp.Eq(new_mat[i, j], mat[i, j]))
    
    solution = list(sp.solve(eq_list, var_list)[0])
    solution = [abs(x) for x in solution]

    final_low_mat = []
    k = 0
    for i in range(0, n):
        t = []
        for j in range(0, i+1):
            t.append(solution[k])
            k += 1
        for m in range(i+1, n):
            t.append(0)
        final_low_mat.append(t)

    final_low_mat = np.matrix(final_low_mat)
    return final_low_mat, final_low_mat.T

def cholesky2(mat):
    import numpy as np

    lower = np.linalg.cholesky(mat)
    return lower, lower.T

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

    if np.all(np.linalg.eigvals(mat) > 0) == False:
        print("Matrix is not positive definite")
        print("Cholesky Decomposition cannot be applied")
        return
    
    L, U = cholesky2(mat)

    print("Choleskey Decomposition")
    print("L")
    print(L)
    print("U")
    print(U)
    print("L * U")
    print(np.dot(L, U))

if __name__ == '__main__':
    main()
