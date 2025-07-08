import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

x=[1,2,3,4,5]
b=[90,44,56,62,72]
a=plt.bar(x,b,color='red',width=0.5,edgecolor='black',label='Student ID')
plt.ylim(0,100)
for i in range(len(b)):
    plt.text(i+1,b[i]+2,str(b[i]),ha='center')


plt.xlabel('Student ID',fontsize=20)
plt.ylabel('Grade',fontsize=20)
plt.title('Student Mark',fontsize=25,fontweight='bold')
plt.grid(True)
plt.show()