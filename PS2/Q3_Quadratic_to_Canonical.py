def main():
    import sympy as sp

    mat = []

    print("Enter the quadratic form as a matrix")
    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(input()))
        mat.append(arr)

    mat = sp.Matrix(mat)
    print(mat)

    P, dmat = mat.diagonalize()
    print(dmat)
    print("Canonical form")
    for i in range(n):
        print("(" + str(dmat[i,i]) + ")", "x" + str(i+1), "^2", end=" ")
        if i != n-1:
            print(" + ", end=" ")
    print()

if __name__ == '__main__':
    main()
