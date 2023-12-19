def main():
    import numpy as np

    eqn = int(input("Enter the number of equations: "))
    var = int(input("Enter the number of variables: "))

    coeff_matrix = []
    const_matrix = []

    print("Enter the elements of the coefficient matrix (row-wise)")
    for i in range(eqn):
        arr = []
        for j in range(var):
            arr.append(int(input()))
        coeff_matrix.append(arr)

    coeff_matrix = np.array(coeff_matrix)

    print("Enter the elements of the constant matrix (row-wise)")
    for i in range(eqn):
        const_matrix.append([int(input())])

    const_matrix = np.array(const_matrix)

    print("Augumented matrix")
    aug_matrix = np.concatenate((coeff_matrix,const_matrix), axis=1)
    print(aug_matrix)

if __name__ == '__main__':
    main()
