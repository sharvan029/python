import pandas as pd
csv = 'C:/Users/sharv/Desktop/HAMEED SHARVAN/learn/python/datasets/titanic.csv'
# excel = 'C:/Users/sharv/Desktop/HAMEED SHARVAN/learn/python/datasets/titanic.xlsx'

titanic = pd.read_csv(csv)
# print(titanic.head())

#avarge of titanic passengers age and Fare
#
# print(titanic["Age"].mean())
#
#
# print(titanic[["Age", "Fare"]].median())
#
# print(titanic["Fare"].sum())

# group by in pandas

# grp = titanic[["Sex", "Age"]].groupby("Sex").median()
# print(grp)

# print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

# finding counts by category
print(titanic["Pclass"].value_counts(dropna=False)) # by default it takes no nulls
print(titanic.groupby(["Pclass"])["Pclass"].count())
