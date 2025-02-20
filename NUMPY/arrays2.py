import numpy as np

# arr = np.empty(0)
# print(arr)

# arr1 = np.empty(3)
# print(arr1)

# arr3 = np.empty([3,3])
# print(arr3)

# arr = np.zeros(5)
# print(arr)

# arr1=np.zeros(5,dtype=int)
# print(arr1)

# arr2=np.zeros([3,3],dtype=int)
# print(arr2)

# arr = np.ones(5)
# print(arr)

# arr1=np.ones(5,dtype=int)
# print(arr1)

# arr2=np.ones([3,3],dtype=int)
# print(arr2)


# arr = np.full(3,5)
# print(arr)

# arr1=np.full([3,3],5,dtype=int)
# print(arr1)

arr1=np.full([3,3,3],5,dtype=int)
print(arr1)

# arr=np.arange(1,200,1)
# print(arr)

# z=np.arange(1,200,2)
# print(z)

s=np.linspace(1,10,2)
print(s)



# b=np.random.randint(1,10,size=(5,5))
# print(b)

a=np.array([1,2,3,4])
b=np.array([[5,6],[7,8]])
c=np.array([[[9,10],[11,12]],[[13,14],[15,16]]])


# print(a.ndim)
# print(b.ndim)
# print(c.ndim)

print(a.shape)
print(b.shape)
print(c.shape)

# print(a.size)
# print(b.size)
# print(c.size)

# print(a.dtype)
# print(b.dtype)
# print(c.dtype)

# print(a.itemsize)
# print(b.itemsize)
# print(c.itemsize)