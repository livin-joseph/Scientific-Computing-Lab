def main():
    import numpy as np
    import sys
    sys.path.append(r'C:\Users\livin\GitHub\Scientific-Computing-Lab')
    import PS1.Q3_Matrix_to_RREF as pack

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix (row-wise)")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(float(input()))
        mat.append(arr)

    mat = np.array(mat)
    print("Matrix")
    print(mat)

    if np.linalg.det(mat) == 0:
        print("Singular matrix (determinant = 0)")
        print("Inverse of matrix does not exist")
        return

    concat_mat = np.concatenate((mat, np.identity(n = n)), axis = 1)
    print("Concatenated matrix")
    print(concat_mat)
    ref = pack.matrixToREF(concat_mat)
    print("REF")
    print(ref)
    rref = pack.REFtoRREF(ref)
    print("RREF")
    print(rref)
    print("Inverse of matrix")
    print(rref[:, n:])

if __name__ == '__main__':
    main()
