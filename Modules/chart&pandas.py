import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('data.csv')
print(data)
plt.plot(data["ID"],data["Maths"],color='red',label='Maths',marker='o')
plt.plot(data["ID"],data["Science"],color='blue',label='Science',linestyle='--',marker='s')
plt.plot(data["ID"],data["English"],color='green',label='Enlgish',linestyle=':',marker='*')
plt.legend(loc='best')
plt.title("Student Marks",fontsize=20,fontweight='bold')
plt.xlabel("Student ID",fontsize=20)
plt.ylabel("Marks",fontsize=20)
plt.grid(True)
plt.show()