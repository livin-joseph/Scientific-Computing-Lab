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
        print("Choleskey Decomposition cannot be applied")
        return

    lower = np.linalg.cholesky(mat)
    upper = lower.getH()
    # Returns the (complex) conjugate transpose of self.
    # Equivalent to np.transpose(self) if self is real-valued.

    print("Choleskey Decomposition")
    print("L")
    print(lower)
    print("U")
    print(upper)

if __name__ == '__main__':
    main()
