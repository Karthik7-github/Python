import numpy as np
# a =np.array((1,2,3,4))
# print(f"the shape of a : {a.shape}\n {a}\n no of elements in an array : {a.ndim}")
# b=np.expand_dims(a,axis=0)
# print(f"shape of b is {b.shape}\n array is : {b}")
# c=np.expand_dims(a,axis=1)
# print(f"shape of c is {c.shape}\n array is : {c}")
# d=np.expand_dims(a,axis=-1)
# print(f"shape of d is {d.shape}\n array is : {d}")
# e=np.expand_dims(a,axis=(1,2))
# print(f"shape of e is {e.shape}\n array is : {e}")


# f=np.array(((1,2,3),(1,2,3)))
# g=np.expand_dims(f,axis=1)
# print(f"shape of g is {g.shape}\n array is : \n{g}")
# g=np.expand_dims(f,axis=0)
# print(f"shape of g is {g.shape}\n array is : \n{g}")
# k=np.array((((9,2,5),(3,7,4)),((2,8,5),(3,7,4))))
# print(k.ndim)
# print(k.shape)
# b=np.squeeze(k,axis=0)
# print(f"shape of b is {b.shape}\n array is : \n{b}")


# a=np.array((3,4,64,66,25,4,2,41))
# b=np.sort(a)
# print(f"array b after sorting : {b}")
# c=np.argsort(a)
# print(f"array c after sorting : {c}")
# a1=np.array(((1,2,5),(45,5,4)))
# b1=np.sort(a1,axis=None)
# c1=np.argsort(a1)
# print(f"array b1 after sorting : {b1}")
# print(f"array c1 after sorting : {c1}")


# a2=np.array((((1,2,3),(3,43,54)),((1,2,3),(3,23,42))))
# b1=np

# a3 = np.arange(10,100,10)
# print(f"array a3 : {a3[::]}")
# print(f"array from index 3 : {a3[3::]}")
# print(f"last lement with len :{a3[len(a3)-1::]}")
# print(f"last element with size : {a3[a3.size-1::]}")
# print(f"first element : {a3[:1:]}")
# print(f"elements in reverse order : {a3[::-1]}")
# print(a3)

b=np.arange(10,100,10)
# print(b)
# print(b[b.size-1])
# print(b[b.size//2])
# print(b[0:2])
# print(b[b.size-2:])
# print(b[::2])
# print(b[0:b.size//2:1])
# print(b[::-1])
# print(b[-1::-1])
# print(b[-(b.size)//2:])
# print(b[::])
# print(b[-(b.size+1):-(b.size)//2])
# print(b[-1])
# print(b[-b.size+2])

ar1=np.array(((2,2),(2,2)))
ar2=np.array(((3,3),(3,3)))
print(f"add :\n {ar1+ar2}")
print(f"sub :\n {ar1-ar2}")
print(f"mul :\n {ar1@ar2}")
print(f"mul :\n {np.dot(ar1,ar2)}")
print(f"determination :\n {np.linalg.det(ar1)}")
print(f"inverse  :\n {np.linalg.inv(ar2)}")
