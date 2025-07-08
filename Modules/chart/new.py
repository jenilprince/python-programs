import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[88,64,95,24]
z=[99,55,33,77]
plt.plot(x,y,color='red',marker='*',linestyle='--',label='Students data')
plt.title("Student mark")
plt.plot(x,z,color='blue',marker='*',linestyle='--',label='Students data')
plt.legend(loc='best')
plt.grid(True)
plt.xlabel("roll")
plt.ylabel("score")
plt.show()