def main():
    import sympy as sp
    import numpy as np

    mat = []

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

    print("Diagonalized matrix")
    P, B = mat.diagonalize()
    print(B)

    a, b = np.linalg.eig(matrix)
    print("Eigenvalues:\n", a)
    print("Eigenvectors:\n", b)

if __name__ == '__main__':
    main()
