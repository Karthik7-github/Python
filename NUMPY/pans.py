import pandas as pd
import numpy as np
import pickle
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(data,index=["I","II","III"],columns=['A','B','C'])
print(df)

df.to_pickle('demo.pkl')

df = pd.read_pickle('demo.pkl')
print(df)

