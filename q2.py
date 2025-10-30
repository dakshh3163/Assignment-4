import numpy as np 

user_input = input("Enter the binary input: ")
arr = np.array(list(user_input), dtype=int)
arr = np.sort(arr)[::-1]

result = ''.join(arr.astype(str))
print("Result: ",result)