import pandas as pd

x = pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
df = pd.DataFrame(x)
print(x)

from sklearn.preprocessing import MinMaxScaler
num_cols = ['Application','Loan_anoumt']
scaler = MinMaxScaler()
df[num_cols]=scaler.fit_transform(df[num_cols])