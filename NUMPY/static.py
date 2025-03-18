import numpy as np

# ar1 = np.array([1,2],[3,4])
# ar2 = np.array([4,5,6])
# ar3 = np.array([7,8,9])
# x=np.stack((ar1,ar2,ar3),axis=1)
# print(x)

# ar1 = np.array([[1,2],[3,4]])
# ar2 = np.array([[5,6],[7,8]])
# y=np.stack((ar1,ar2),axis=1)
# print(y)

# ar1 = np.array([1,2,3])
# ar2 = np.array([4,5,6])
# x=np.column_stack((ar1,ar2))
# print(x)

ar1=np.array(([1,2,3],[4,5,6]))
ar2=np.array(([7,8,9],[10,11,12]))
x=np.vstack((ar1,ar2))
print(x)

