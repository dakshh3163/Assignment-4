import numpy as np 


print(f"Numpy Version: {np.__version__}")

user_input = input("Enter elements of the list: ")
elements = user_input.split()
freq = {}

for item in elements:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1


print("Frequency of each element: ")
for key, value in freq.items():
    print(f"'{key} : {value}")