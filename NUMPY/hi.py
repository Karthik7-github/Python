# import numpy as np
# # arr7 = np.asarray((((1,2,8,7),(3,5,7,4),(4,6,5,7))),(((5,6,3,6),(7,,6,4,8),(4,5,7,3))))
# arr7 = np.array((((1,3,6,2),(3,5,6,4),(3,7,7,5)),((5,6,4,7),(7,8,5,4),(4,5,6,3))))
# print(arr7)
# print(arr7)

# print(arr7)
# print(arr7.ndim)

import numpy as np 
# a=np.array([1,2,3,5])
# # b=np.reshape(a,(3,-1))
# b=a.reshape((1,2,2))
# print(b)

#flatten and ravel

# a=np.ones((2,3),dtype=int)
# print(a)

# b=a.flatten()
# print(b)
# b[2]=10
# print(b)
# print(a)

# c=a.ravel()
# print(c)
# c[4]=4
# print(c)
# print(a)
# print(b)

#transpose matrix

d=np.array([[1,2,3],[4,5,6]])
print(d.shape)
print(d)

e=np.transpose(d)
print(e.shape)
print(e)