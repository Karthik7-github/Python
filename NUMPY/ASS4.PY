import numpy as np
a=np.array([[1,3,5,7,9],[2,4,6,8,10]])
print("array before adding new dimension : \n",a)
print("array shape : \n",a.shape)
b=np.expand_dims(a,axis=1)
print("array after changing the dimensions : \n",b)
print("array shape : \n",b.shape)


#[[[1,3,5,7,9],[2,4,6,8,10]],[[1,3,5,7,9],[2,4,6,8,10]]]