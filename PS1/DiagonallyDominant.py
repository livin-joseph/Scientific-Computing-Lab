def modsum(list1):
    s = 0
    for i in list1:
        s += abs(i)
    return s

def diagonallyDominant(mat):
    index = 0
    for i in mat:
        if modsum(i) - abs(i[index]) > abs(i[index]):
            return False
        index += 1
    return True

def strictlyDiagonallyDominant(mat):
    index = 0
    for i in mat:
        if modsum(i) - abs(i[index]) >= abs(i[index]):
            return False
        index += 1
    return True

def main():
    import numpy as np

    mat = []

    #r = int(input())
    #c = int(input())

    n = int(input("Enter number of rows/columns: "))

    print("Enter the elements of the matrix")

    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(input()))
        mat.append(arr)

    mat = np.array(mat)
    print(mat)

    if diagonallyDominant(mat) == True:
        print("Matrix is diagonally dominant")
    else:
        print("Matrix is not diagonally dominant")

    if strictlyDiagonallyDominant(mat) == True:
        print("Matrix is strictly diagonally dominant")
    else:
        print("Matrix is not strictly diagonally dominant")

if __name__ == '__main__':
    main()
