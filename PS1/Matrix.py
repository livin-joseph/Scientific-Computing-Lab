import numpy as np

mat = []

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

#n = int(input("Enter number of rows/columns: "))

print("Enter the elements of the matrix (row-wise)")

for i in range(r):
    arr = []
    for j in range(c):
        arr.append(int(input()))
    mat.append(arr)

mat = np.array(mat)
print(mat)