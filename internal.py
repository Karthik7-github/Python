# # 1. Basic 1D NumPy array
import numpy as np
# arr1 = np.array([10, 20, 30, 40])
# print(arr1)

# # 2. 2D NumPy array of zeros and shape
# zeros_2d = np.zeros((3, 4))
# print(zeros_2d.shape)

# # 3. 3x3 array of random numbers
# random_arr = np.random.rand(3, 3)
# print(random_arr)

# # 4. Array with evenly spaced values between 0 and 50
# evenly_spaced = np.linspace(0, 50, 11)
# print(evenly_spaced)

# # 5. Reshape 1D to 3x3
# arr_1d = np.arange(9)
# reshaped = arr_1d.reshape((3, 3))
# print(reshaped)

# # 6. Flatten 2D to 1D
# flattened = reshaped.flatten()
# print(flattened)

# # 7. Transpose 2D array
# transposed = reshaped.T
# print(transposed)

# 8. Expand 1D to 2D
arr = np.array([1, 2, 3])
expanded = np.expand_dims(arr, axis=0)
print(expanded)
print(expanded.shape)

# # 9. Squeeze 3D array
# arr_3d = np.array([[[1], [2], [3]]])
# squeezed = np.squeeze(arr_3d)
# print(squeezed)

# # 10. Sort NumPy array
# unsorted = np.array([4, 1, 3, 9])
# sorted_arr = np.sort(unsorted)
# print(sorted_arr)

# # 11. Slice every second element
# arr = np.array([0, 1, 2, 3, 4, 5])
# print(arr[::2])

# # 12. Extract specific row and column
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Row 1:", matrix[1])
# print("Col 2:", matrix[:,2])

# # 13. Negative slicing (reverse)
# print(arr[::-1])

# # 14. Stack arrays vertically
# a = np.array([1, 2])
# b = np.array([3, 4])
# stacked = np.vstack((a, b))
# print(stacked)

# # 15. Concatenate arrays
# concatenated = np.concatenate((a, b), axis=0)
# print(concatenated)

# # 16. Broadcasting
# a = np.array([1, 2, 3])
# b = 5
# print(a + b)

# import pandas as pd
# import numpy as np

# # 17. DataFrame from dictionary
# data = {'Name': ['A', 'B', 'C'], 'Age': [21, 22, 23]}
# df = pd.DataFrame(data)
# print(df.head())

# # 18. Add new column using list
# df['City'] = ['X', 'Y', 'Z']
# print(df)

# # 19. Fill NaN values
# df2 = pd.DataFrame({'Name': ['A', 'B', None], 'City': [None, 'Y', 'Z']})
# print(df2.fillna('Unknown'))

# # 20. Sort DataFrame by column
# sorted_df = df.sort_values(by='Age')
# print(sorted_df)

# # 21. Group and summarize
# group_data = pd.DataFrame({'Branch': ['CSE', 'ECE', 'CSE'], 'Placed': [1, 0, 1]})
# print(group_data.groupby('Branch').sum())

# # 22. Concatenate two DataFrames
# df3 = pd.DataFrame({'Name': ['D', 'E'], 'Age': [24, 25]})
# concat_df = pd.concat([df, df3])
# print(concat_df)

# # 23. Read CSV and show first 4 rows
# df_csv = pd.read_csv('sample.csv')
# print(df_csv.head(4))

# # 24. Import Excel file
# df_excel = pd.read_excel('sample.xlsx')
# print(df_excel)

# # 25. Read JSON to DataFrame
# df_json = pd.read_json('sample.json')
# print(df_json)

# # 26. Read multiple .txt using glob
# import glob
# for file in glob.glob("data/*.txt"):
#     with open(file) as f:
#         print(f.read())

# # 27. Import SQLite data
# import sqlite3
# conn = sqlite3.connect('sample.db')
# df_sql = pd.read_sql("SELECT * FROM students", conn)
# print(df_sql)

# # 28. Create and read pickle
# df.to_pickle('data.pkl')
# df_loaded = pd.read_pickle('data.pkl')
# print(df_loaded)

# # 29. Min-Max Scaling
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(df[['Age']])
# print(scaled)

# # 30. Standard Scaling
# from sklearn.preprocessing import StandardScaler
# std_scaler = StandardScaler()
# standardized = std_scaler.fit_transform(df[['Age']])
# print(standardized)

# # 31. Label Encoding
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# df['EncodedCity'] = le.fit_transform(df['City'])
# print(df)

# # 32. One Hot Encoding
# df_encoded = pd.get_dummies(df, columns=['City'])
# print(df_encoded)

# import matplotlib.pyplot as plt

# # 33. Bar Graph
# branches = ['CSE', 'ECE', 'EEE']
# placements = [30, 20, 10]
# plt.bar(branches, placements)
# plt.title("Placements per Branch")
# plt.show()

# # 34. Pie Chart
# plt.pie(placements, labels=branches, autopct='%1.1f%%')
# plt.title("Placement Distribution")
# plt.show()

# # 35. Histogram
# data = np.random.randn(1000)
# plt.hist(data, bins=20)
# plt.title("Histogram")
# plt.show()

# # 36. Line chart and subplots
# x = np.arange(0, 10)
# y1 = x**2
# y2 = np.sqrt(x)
# plt.subplot(1, 2, 1)
# plt.plot(x, y1, label='x^2')
# plt.legend()
# plt.subplot(1, 2, 2)
# plt.plot(x, y2, label='sqrt(x)')
# plt.legend()
# plt.show()

# # 37. Box Plot
# data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# plt.boxplot(data)
# plt.title("Box Plot Example")
# plt.show()

# # 38. Scatter Plot
# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.show()

# 28 8 17

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Save the DataFrame to a pickle file
df.to_pickle('data.pkl')

# Read the DataFrame back from the pickle file
df_loaded = pd.read_pickle('data.pkl')

# Display the loaded DataFrame
print(df_loaded)
