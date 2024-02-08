def main():
    import numpy as np

    mat = []

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(input()))
        mat.append(arr)

    mat = np.array(mat)
    x = np.array([[1]] * n)

    temp = []

    print("Power method iterations")
    while(True):
        a = np.matmul(mat, x)
        print(a)
        absmin = min(abs(a))
        if absmin != min(a):
            absmin = -1 * absmin

        if np.array_equal(np.round(temp, decimals=2), np.round(a / absmin, decimals=2)):
            temp = a / absmin
            break
        temp = a / absmin
        x = a
    print("End of Power method iterations")

    dominantevect = np.round(temp, decimals=1)
    print("Dominant Eigenvector:\n", dominantevect)

    ax = np.transpose(np.matmul(mat, dominantevect))
    x = np.transpose(dominantevect)
    axx = ax * x # Component-wise multiplication
    xx = x * x
    dominantev = np.sum(axx) / np.sum(xx)
    print("Dominant Eigenvalue: ", dominantev)

if __name__ == '__main__':
    main()
