import numpy as np
def removeNthChar(n):
    arr = np.array(list(user_input),dtype=str)
    arr = np.delete(arr,n-1)
    result = ''.join(arr.astype(str))
    return result

user_input = input("Enter the string: ")
n = int(input("Enter the value for nth index: "))
print(removeNthChar(n))