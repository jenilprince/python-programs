
'''print(data.isnull())
print(data.describe())
mean=np.mean(datanum[:,3])
stdrev=np.std(datanum[:,5])
print(stdrev)
Totalrev=np.sum(datanum[:,3]*datanum[:,4])
print(Totalrev)
max=np.max(datanum[:,5])
print(max)'''
'''grouped=data.groupby("Product")["Unit_Price"].sum()
print(grouped)
topselling=data.sort_values("Units_Sold",ascending=False)
print(topselling.head(1))
maxrev=data.sort_values("Revenue",ascending=False)
print(maxrev["Date"].head(1))
data["Profit"]=data["Revenue"]-.8*data["Unit_Price"]*data["Units_Sold"]
print(data)
totsum=data.groupby("Category")["Revenue"].sum()
print(totsum)
plt.bar(data["Category"],data["Revenue"],color='blue',width=.3)

plt.title("Bar chart",fontsize=25,fontweight='bold')
plt.xlabel("Category",fontsize=15)
plt.ylabel("Revenue",fontsize=15)
plt.show()
plt.plot(data["Date"],data["Revenue"],color='blue',marker='o')
plt.grid(True)
plt.xlabel("Days",fontsize=20)
plt.ylabel("Revenue",fontsize=20)
plt.title("Line chart",fontsize=25,fontweight='bold')
plt.show()'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('data.csv')

print(data)


share=data.groupby("Product")["Revenue"].sum()
print(share)
label=data["Product"]

plt.pie(share.values,labels=share.index,autopct='%1.1f%%')
plt.title("Pie chart",fontsize=25,fontweight='bold')
plt.legend(loc='upper right')
plt.show()
