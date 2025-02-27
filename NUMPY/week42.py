import numpy as np

d=np.arange(1,13,1)
e=np.reshape(d,(3,4))
f=np.arange(13,25,1)
g=np.reshape(f,(3,4))
h=np.concatenate((e,g),axis=0)
print(h)
h=np.concatenate((e,g),axis=1)
print(h)