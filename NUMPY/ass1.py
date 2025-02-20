import numpy as np
arr=np.array((1,2,3))
print(arr,end="\n\n")

# arr1=np.array(((1,2,3,4),(5,6,7,8)))
# print(arr1,end="\n\n")

# import numpy as np
# arr2=np.asarray(((1,1,1,1),(1,1,1,1),(1,1,1,1)))
# print(arr2,end="\n\n")

# import numpy as np
# arr3=np.asarray((1,2,3))
# print(arr3,end="\n\n")

# import numpy as np
# arr4=np.asarray(((1,2,3,4),(5,6,7,8)))
# print(arr4,end="\n\n")

# import numpy as np
# arr5=np.asarray(((1,1,1,1),(1,1,1,1)),(1,1,1,1)))
# print(arr5,end="\n\n")

# import numpy as np
# n=int(input("ENTER SIZE : "))
# arr6=np.ndarray(shape=(n),dtype=int)
# for i in range(n):
#     arr6[i]=int(input())
# print(arr6,end="\n\n")

# import numpy as np
n=int(input("ENTER ROW : "))
m=int(input("ENTER COL : "))
arr7=np.ndarray(shape=(n,m),dtype=int)
for i in range(n):
    for j in range(m):
        arr7[i][j]=int(input())
print(arr7,end="\n\n")
print(arr7.ndim)
 