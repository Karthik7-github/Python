import numpy as np
a=np.arange(1,13,1)
# print(a)
b=np.reshape(a,(3,4))
# print(b)
# print(b[2,:])
# print(b[:,3])
# print(b[0,[0,1]])
# print(b[1,[1,2]])
# print(b[2,[2,3]])
# print(b[0:2,1:3])
# print(b[1:3,:])

# print(f"the elements 1,2 in row 0 : {b[-3,-4:-2]}")
# print(f"the elements 6,7 in row 1 : {b[-2,-3:-1]}")
# print(f"the elements 11,12 in row 2 : {b[-1,-2:]}")
# print(f"the elements 2,3 in row 0  : {b[-3:-1,-3:-1]}")
# print(f"the elements all in row 1,2 : {b[-2:2,:4]}")


#     -3   -2    -1         
# -3
# -2
# -1
a=np.arange(1,28,1)
b=np.reshape(a,(3,3,3))
# print(b)
print(f"{b[0,0,0]}\n--------")
print(f"{b[1,1,1]}\n--------")
print(f"{b[2,2,2]}\n--------")
print(f"{b[0]}\n --------")
print(f"{b[-2,-1,-2]}\n-----------")
print(f"{b[:,:,0]}\n----------")
print(f"{b[:,0:2,0:2]}\n--------")
print(f"{b[:,0:3,1]}\n--------")
# print(f"{b[]}\n--------")

print(f"{b[:,-3:-1,:]}\n--------")
print(f"{b[:,:,-2]}\n--------")
print(f"{b[-1,-1,-1]}\n--------")
print(f"{b[-2,-1,-1]}\n--------")
print(f"{b[-1,:,-1]}\n--------")
print(f"{b[:,:,:]}\n--------")
