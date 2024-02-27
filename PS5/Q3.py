def main():
    import scipy as sp

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix (row-wise)")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(float(input()))
        mat.append(arr)

    mat = sp.array(mat)
    print("Matrix")
    print(mat)

    P, L, U = sp.linalg.lu(mat)

    print("LU Decomposition")
    print("L")
    print(L)
    print("U")
    print(U)

if __name__ == '__main__':
    main()
