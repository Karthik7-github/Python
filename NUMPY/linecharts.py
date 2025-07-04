
import numpy as np
import matplotlib as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]
f1={'family' : 'Times new roman','color':'red','size':12}
f2={'family' : 'Times new roman','color':'blue','size':12}
f3={'family' : 'Times new roman','color':'green','size':12}
plt.title("Line Chart",fontdict=f1)
plt.xlabel("x-axis",fontdict=f2)
plt.ylabel("y-axis",fontdict=f3)
plt.plot(x,y)
plt.show()


#subplots
# x = np.array([1,2,3,4])
# y = np.array([10,20,30,40])
# z = np.array([80,70,60,50])

# plt.suptitle("MULTIPLE PLOT")
# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title("Plot-1")
# plt.subplot(1,2,2)
# plt.plot(x,z)
# plt.title("Plot-2")
# plt.show()

# x=np.array([1,2,3,4])
# y=x**2
# z=x**3

# plt.plot(x,y)
# plt.plot(x,z)

# plt.show()

# import pandas as pd

# x = pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
# df = pd.DataFrame(x)
# print(x)

# from sklearn.preprocessing import MinMaxScaler
# num_cols = ['Application','Loan_anoumt']
# scaler = MinMaxScaler()
# df[num_cols]=scaler.fit_transform(df[num_cols])
# df

# from sklearn.preprocessing import StandardScaler
# Standardizer = StandardScaler()
# df[num_cols]=Standardizer.fit_transform(df[num_cols])
# df
