def main():
    import sympy as sp

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(input()))
        mat.append(arr)

    mat = sp.Matrix(mat)

    if mat.is_diagonalizable() == True:
        print("Matrix is diagonalizable")
    else:
        print("Matrix is not diagonalizable")

if __name__ == '__main__':
    main()
