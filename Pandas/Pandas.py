import pandas as pd
# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )

# print(df)
# print(df["Name"])

# ages = pd.Series([10,20,30], name ="age")
# print(ages)
# print(df["Age"].max())
# print(df.describe())

# reading tabular data

csv = 'C:/Users/sharv/Desktop/HAMEED SHARVAN/learn/python/datasets/titanic.csv'
excel = 'C:/Users/sharv/Desktop/HAMEED SHARVAN/learn/python/datasets/titanic.xlsx'

titanic = pd.read_csv(csv)

# print(titanic)
# print(titanic.head(3))
# print(titanic.tail(3))
# print(titanic.dtypes)

#write csv into xcel
# titanic.to_excel(excel, sheet_name='passengers', index=False)

# titanic.info()

# reading subset of data or reading specific columns

ages = titanic["Age"]
# print(ages.head())
# print(type(ages))
# print(ages.shape)
# print(titanic["Age"].shape)
# print(titanic[["Age", "Sex", "Survived"]].head(10))
# print(titanic[["Age", "Sex", "Survived"]].shape)


# reading subset of data or reading specific rows

# below_30 = titanic[titanic["Age"]<30]
# print(below_30.head(1))
# print(titanic["Age"]<30)
# print(below_30.shape)
# print(titanic[titanic["Pclass"].isin([1, 2])]) #filtering Pclass with 1 or 2
# print(titanic[( titanic["Pclass"]==1) | (titanic["Pclass"] == 2)]) # same as above

# compare male and female survivors
# malesurvivors = titanic[( titanic["Survived"] == 1) & (titanic["Sex"] == "male")]
# femalesurvivors = titanic[( titanic["Survived"] == 1) & (titanic["Sex"] == "female")]
# print(malesurvivors.shape, femalesurvivors.shape)

# age_no_na = titanic[titanic["Age"].notna()]
# print(age_no_na.shape)


# reading specific column and row

# old_passengers = titanic.loc[titanic["Age"]>60, "Name"]
# old_passengers = titanic.loc[titanic["Age"]>60, ["Name","Age"]]

# print(old_passengers)

# print rows from 10 to 25, and columns 3 to 5
# print(titanic.iloc[9:25, 2:5])

# update 3rd column and first 3 rows as anonymous
# titanic.iloc[0:3, 3] = "anonymous"

