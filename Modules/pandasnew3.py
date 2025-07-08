import pandas as pd
read=pd.read_csv('employees.csv')
print(read)
print(f"Employee Count == {len(read)}")
dep=read["Department"].nunique()
print(dep)
sales=read[read["Department"]=="Sales"]
print(sales[["Name","Salary"]])
max=read["Salary"].max()
print(read[read["Salary"]==max])
read["JoiningDate"]=pd.to_datetime(read["JoiningDate"])
print(read[read["JoiningDate"]<"2020"])
salary=read[read["Salary"]>46000]
print(salary)
read["Bonus"]=read["Salary"]*.1
print(read)
read["Total Earnings"]=read["Salary"]+read["Bonus"]+read["Sales"]*100
print(read)
earning=read[read["Total Earnings"]>70000]
print(earning)
salesmore=read[read["Sales"]>0]
print(f"Sales: {len(salesmore)}")
group=read.groupby("Department")["Salary"].mean()
print(group)
sorting=read.sort_values("Sales", ascending=False)
print(sorting)
print(sorting.head(1))
read["JoiningDate"]=pd.to_datetime(read["JoiningDate"])
print(read)
print(read["JoiningDate"].dt.year)
print(read["JoiningDate"].dt.month)
print(read[read["JoiningDate"].dt.year==2021])
print(read["JoiningDate"].dt.day)
