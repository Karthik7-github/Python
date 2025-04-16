# import pandas as pd
# data = {
#     "A":501,
#     "B":502,
#     "C":503    
#     }
# s=pd.Series(data)
# print(s)
# print(data["A"])

# s=pd.Series(data)

import pandas as pd
# l1=[1,2,3,4]
# l2=[1,2,3,4]

# s1=pd.Series(l1)
# s2=pd.Series(l2)

# sum=s1+s2
# print(sum)


# l3=[1,2,3,4]
# l4=[4,3,2,1]

# s3=pd.Series(l3)
# s4=pd.Series(l4)

# sum1=s3+s4
# print(sum1)

# l5=[1,2,3,4]
# l6=[4,3,2,1]

# s5=pd.Series(l3)
# s6=pd.Series(l4,)

# sum1=s3+s4
# print(sum1)


import numpy as np
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(data,index=["I","II","III"],columns=['A','B','C'])
print(df)

