import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris=load_iris()
iris_df=pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df['species']=iris.target_names[iris.target]

#basic info
print("Dataset shape",iris_df.shape)
print("columns:",iris_df.columns)
print("species Distribution:\n",iris_df['species'].value_counts())

#histograms
iris_df.hist(figsize=(10,8))
plt.tight_layout()
plt.show()


#pairplot
sns.pairplot(iris_df,hue='species')
plt.show()

#boxplots
plt.figure(figsize=(10,8))
sns.boxplot(data=iris_df.drop('species',axis=1))
plt.show()

#correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(iris_df.drop('species',axis=1).corr(),annot=True,cmap='coolwarm')
plt.show()