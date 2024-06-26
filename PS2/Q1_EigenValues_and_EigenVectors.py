def EigenValues(mat):
    import sympy as sp
    n = sp.shape(mat)[0]

    lam = sp.Symbol('lambda')
    print(n)
    newmat = mat - lam * sp.eye(n)
    char_eq = newmat.det()
    print("Characteristic equation: ", char_eq)
    ev = sp.solveset(char_eq, lam)
    ev = [round(i, 2) for i in ev]
    return ev   

def main():
    import sympy as sp
    import numpy as np

    mat = []

    global n
    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(input()))
        mat.append(arr)

    matrix = np.array(mat)
    mat = sp.Matrix(mat)
    print(mat)

    ev = EigenValues(mat)
    print("Eigenvalues: ", ev)

    a, b = np.linalg.eig(matrix)
    print("Eigenvalues:\n", a)
    print("Eigenvectors:\n", b)

if __name__ == '__main__':
    main()
