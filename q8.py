import numpy as np


r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

print("Enter the elements row-wise:")
matrix = []

for i in range(r):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)

matrix = np.array(matrix)

print("\nInput Matrix:")
print(matrix)

rank = np.linalg.matrix_rank(matrix)
trace = np.trace(matrix)
det = np.linalg.det(matrix) if r == c else None  # determinant only for square matrices

print("\nMatrix Properties:")
print("Rank of the matrix:", rank)
print("Trace of the matrix:", trace)
if det is not None:
    print("Determinant of the matrix:", det)
else:
    print("Determinant not defined for non-square matrices.")
