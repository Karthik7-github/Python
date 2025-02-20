import numpy as np
n=int(input("enter num : "))
arr = np.ndarray(shape=(n),dtype=int)
print(f"enter {n} elements : ")
for i in range(n):
    arr[i] = int(input())

print(f"the array : {arr}")