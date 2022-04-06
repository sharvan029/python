import pandas as pd
filepath = "C:/Users/sharv/Desktop/HAMEED SHARVAN/learn/python/datasets/air_quality.csv"
air_quality = pd.read_csv(filepath, index_col=0, parse_dates=True)
csv = 'C:/Users/sharv/Desktop/HAMEED SHARVAN/learn/python/datasets/titanic.csv'
titanic = pd.read_csv(csv)

#Sort by single column
# print(titanic.sort_values(by="Age", ascending=True).tail())

#sort by two column
# print(titanic.sort_values(by=["Pclass", "Fare"], ascending=False).head()

# Long to wide table format
# print(air_quality.head())

# filter for no2
no2 = air_quality[air_quality["parameter"] == "no2"]
# sub set of no2
no2_subset = no2.sort_index().groupby(["location"]).head(2)
# print(no2_subset)
# pivoting location and taking values
# pivot_no2 = no2_subset.pivot(columns="location", values="value")

pivot_airquality = air_quality.pivot_table(values="value", index = "location",  columns="parameter", aggfunc="sum")
print(pivot_airquality)