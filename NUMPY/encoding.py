# import pandas as pd
# x=pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
# df=pd.DataFrame(x)
# print(df)


# from sklearn.preprocessing import MinMaxScaler
# import pandas as pd
# x=pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
# df=pd.DataFrame(x)
# num_cols=['Apllication','Loan_amount']
# scaler=MinMaxScaler()
# df[num_cols]=scaler.fit_transform(df[num_cols])
# print(df)


# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# x=pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
# df=pd.DataFrame(x)
# standardizer=StandardScaler()
# num_loc=['Apllication','Loan_amount']
# df[num_loc]=standardizer.fit_transform(df[num_loc])
# print(df)


# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# x = pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
# df_label = x.copy()
# le = LabelEncoder()
# for col in ['Gender', 'Married', 'Education', 'Local_status']:
#     df_label[col + '_label'] = le.fit_transform(df_label[col])
# print(df_label)


# import pandas as pd
# x = pd.read_excel("C:\\Users\\Karthik\\OneDrive\\Desktop\\LOAN.xlsx")
# df_onehot = pd.get_dummies(x, columns=['Gender', 'Married', 'Education', 'Local_status'])
# print(df_onehot)