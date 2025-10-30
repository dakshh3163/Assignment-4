import numpy as np

original_arr = np.ones((4,4))

arr = np.zeros((5,5))
for i in range(1, 4):
    for j in range(1, 4):
        arr[i][j] = 1

print(arr)