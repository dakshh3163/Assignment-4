import numpy as np

array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])


array1 = np.array(list(map(int, input("Enter elements of first array: ").split())))
array2 = np.array(list(map(int, input("Enter elements of second array: ").split())))

# Compare elements
result = np.isin(array1, array2)
print(result)