import pandas as pd
data=pd.read_csv("data.csv")
print(data.loc[0])
print(data.iloc[3])