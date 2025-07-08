import pandas as pd
data=pd.read_csv('data.csv')
data["Total"]=data["Maths"]+data["Science"]+data["English"]
hig=data[data["Total"]>265]
print(data[["Science","Maths","Total"]])




