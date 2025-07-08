import pandas as pd
read=pd.read_csv('classmarks.csv')
print(read)
read["JoinDate"]=pd.to_datetime(read["JoinDate"])
print(read)
print(read["JoinDate"].dt.year)
