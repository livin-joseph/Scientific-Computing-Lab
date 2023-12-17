def modsum(list1):
    s = 0
    for i in list1:
        s += abs(i)
    return s

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

index = 0
flag = True
for i in mat:
    if modsum(i) - abs(i[index]) > abs(i[index]):
        print("Matrix is not diagonally dominant")
        flag = False
        break
    index += 1

if flag == True:
    print("Matrix is diagonally dominant")
