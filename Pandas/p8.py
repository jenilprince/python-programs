import pandas as pd
data=pd.read_csv("data.csv")
## For sorting data giving conditions
print(data[data["Rating"]>8.5])
print(data[data["Release"]>2020])