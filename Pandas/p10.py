import pandas as pd
data=pd.read_csv("data.csv")
## For sorting
print(data.sort_values(by=["Release"]),"\n")
print(data.sort_values(by=["Rating"],ascending=False),"\n")
print(data[::-1],"\n")
print(data[::2])