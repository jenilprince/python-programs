import pandas as pd
data=pd.read_csv("data.csv")
## For adding a new column or row
data["Box Office"]=[829.9,263.1,121.0,807.1]
print(f"{data}\n")
print(data[data["Box Office"]>500],"\n")
print(data["Title"][data["Box Office"]>500],"\n")