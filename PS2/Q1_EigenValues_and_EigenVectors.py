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

def EigenVectors(mat, ev):
    import sympy as sp
    n = sp.shape(mat)[0]
    
    tempmat = mat - ev * sp.eye(n)
    tempmat = tempmat.col_insert(n, sp.Matrix([0] * n))
    evec = sp.linsolve(tempmat)
    return evec

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
    print(mat)

    ev = EigenValues(mat)
    print("Eigenvalues: ", ev)

    for i in ev:
        print("Eigenvectors corresponding to eigenvalue ", i, ": ", EigenVectors(mat, i))

if __name__ == '__main__':
    main()
