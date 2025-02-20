# import numpy as np
# arr = np.asarray(10)
# print(arr)

# arr1 = np.array([1,2])
# print(arr1)

# arr2 = np.array([[1,2],[3,4]])
# print(arr2)

# arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(arr3)

# arr4 = np.array(10)
# print(arr4)

# arr5 = np.array((1,2))
# print(arr5)

# arr6 = np.array(((1,2),(3,4)))
# print(arr6)

# arr7 = np.array((((1,2),(3,4)),((5,6),(7,8))))
# print(arr7)

# import numpy as np
# arr = np.asarray(10)
# print(arr)

# arr1 = np.asarray([1,2])
# print(arr1)

# arr2 = np.asarray([[1,2],[3,4]])
# print(arr2)

# arr3 = np.asarray([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(arr3)

# arr4 = np.asarray(10)
# print(arr4)

# arr5 = np.asarray((1,2))
# print(arr5)

# arr6 = np.asarray(((1,2),(3,4)))
# print(arr6)

# arr7 = np.asarray((((1,2),(3,4)),((5,6),(7,8))))
# print(arr7)

import numpy as np
# n=int(input("Enter size : "))
# arr = np.ndarray(shape=n,dtype=int)
# arr1 = np.ndarray(shape=n)
# print("Enter elements : ")
# for i in range(n):
#     arr[i]=int(input())
#     arr1[i]=arr[i]

# print(arr)
# print(arr1)

n=int(input("enter n : "))
r=int(input("enter row :"))
c=int(input("enter col :"))

arr = np.ndarray(shape=(n,r,c),dtype=int)
print("enter ele : ")
for k in range(n):
    for i in range(r):
        for j in range(c):
            arr[k][i][j]=int(input())

print(arr)