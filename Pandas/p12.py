import pandas as pd
data = pd.read_csv("data.csv")
print(data.groupby("Title").sum())
print(data.groupby("Title")["Release"].sum())
