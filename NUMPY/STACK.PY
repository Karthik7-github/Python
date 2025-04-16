import numpy as np
# a = np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.stack([a,b])
# print(c)
# d=np.stack([a,b],axis=0)
# print(f"0 : \n {d}")
# e=np.stack([a,b],axis=1)
# print(f"1 : \n {e}")
# f=np.stack([a,b],axis=-1)
# print(f"-1 : \n {f}")




# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# b1=np.array([[7,8,9],[10,11,12]])
# c=np.stack([a1,b1])
# print(c)
# d=np.stack([a1,b1],axis=0)
# print(f"0 : \n {d}")
# e=np.stack([a1,b1],axis=1)
# print(f"1 : \n {e}")
# f=np.stack([a1,b1],axis=-1)
# print(f"-1 : \n {f}")

# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# b1=np.array([[7,8,9],[10,11,12]])
# c=np.hstack([a1,b1])
# print(c)
# d=np.hstack([a1,b1])
# print(f"0 : \n {d}")
# e=np.hstack([a1,b1])
# print(f"1 : \n {e}")
# f=np.hstack([a1,b1])
# print(f"-1 : \n {f}")

# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# b1=np.array([[7,8,9],[10,11,12]])
# c=np.vstack([a1,b1])
# print(c)
# d=np.vstack([a1,b1])
# print(f"0 : \n {d}")
# e=np.vstack([a1,b1])
# print(f"1 : \n {e}")
# f=np.vstack([a1,b1])
# print(f"-1 : \n {f}")

# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# b1=np.array([[7,8,9],[10,11,12]])
# c=np.dstack([a1,b1])
# print(c)
# d=np.hstack([a1,b1])
# print(f"0 : \n {d}")
# e=np.hstack([a1,b1])
# print(f"1 : \n {e}")
# f=np.hstack([a1,b1])
# print(f"-1 : \n {f}")


# import numpy as np
# a=np.arange(1,100,10)
# print(a)
# add = a + 1
# print(add)
# sub= a-1
# print(sub)
# mul= a*10
# print(mul)
# div= a/10
# print(div)
# mod=a%10
# print(mod)
# pow=a**2
# print(pow)

# import numpy as np
# a=np.arange(1,100,10)
# a1=np.add(a,3)
# print(a1)
# b1=np.subtract(a,3)
# print(b1)
# c1=np.multiply(a,3)
# print(c1)
# d1=np.divide(a,3)
# print(d1)
# e1=np.mod(a,3)
# print(e1)
# f1=np.power(a,2)
# print(f1)
# g1=np.remainder(a,3)
# print(g1)


# a=np.arange(1,4,1)
# print(f"Shape of a : {a.shape}")
# print(f"array is : {a}")
# b=np.array([[1,2,3],[4,5,6]])
# print(f"Shape of b : {b.shape}")
# print(f"array is : {b}")
# res = a + b
# print(f" res : {res}")


# a1=np.array([1,2,3])
# print(f"Shape of a1 : {a1.shape}")
# print(f"Array is : {a1}")
# b1=np.array([[4],[5],[6]])
# print(f"Shape of b1 : {b1.shape}")
# print(f"Array is : {b1}")
# res= a1 + b1
# print(f"Shape of res : {res.shape}")
# print(f"Array is : {res}")


# import numpy as np
# a = np.arange(1,10,1)
# print(f"max : {np.max(a)}")
# print(f"min : {np.min(a)}")
# print(f"avg : {np.average(a)}")
# print(f"sum : {np.sum(a)}")
# print(f"reverse : {np.flip(a)}")
# print(f"median : {np.median(a)}")
# print(f"mean : {np.mean(a)}")
# a[0] = 11
# print(f"after modification : {a}")
# a[4:]= 22
# print(f"after modification : {a}")
# print(f"after inserting : {np.insert(a,3,a)}")
# print(f"after deletion : {np.delete(a,6)}")

# a=np.array([24,43,343,43,4,2,23,4034,4,45,5,342])
# x=np.where(a%4==1)
# print(x)
# x=np.searchsorted(np.sort(a),25)
# print(np.sort(a))
# print(x)
# b=np.searchsorted([6,8,9],7)
# print(b)


arr=np.array([5,1,3,7])

x=np.searchsorted(arr,2)
print(x)
