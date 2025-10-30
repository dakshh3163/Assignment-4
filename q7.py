import numpy as np

array1 = np.array(list(map(int, input("Enter elements of first array: ").split())))
array2 = np.array(list(map(int, input("Enter elements of second array: ").split())))

result = np.column_stack((array1, array2))

print("Stack arrays column-wise:")
print(result)
