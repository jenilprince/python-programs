import pandas as pd
data=pd.read_csv("data.csv")
print(f"Shape: {data.shape}")
print(data["Title"])