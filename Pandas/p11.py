import pandas as pd
data=pd.read_csv("data.csv")
print(data.describe())
print(data.columns)
print(data.isnull())