import pandas as pd
data={
    "Name": ["Ali", "Sara","John"],
    "Maths": [88,75],
    "Science": [90,85,]
}
read=pd.read_csv('students.csv')
print(read.isnull().sum())
read["Science"]=read["Science"].fillna(0)
