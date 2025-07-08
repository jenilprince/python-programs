import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('data.csv')
print(data)
plt.pie(data["Maths"],labels=data["Name"],autopct="%1.2f%%",startangle=0,colors=["lightcoral","lightblue","lightyellow","lightgreen"],explode=[0.05,0.05,0.05,.05],wedgeprops={"width":.7})
plt.title("Maths",fontsize=20,fontweight="bold")
plt.axis('equal')
plt.show()