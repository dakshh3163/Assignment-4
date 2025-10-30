import numpy as np

array1 = np.array(list(map(int, input("Enter elements of first array: ").split())))
array2 = np.array(list(map(int, input("Enter elements of second array: ").split())))

result = np.setxor1d(array1, array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(result)
