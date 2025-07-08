import matplotlib.pyplot as plt
roll = [1, 2, 3, 4, 5]
math_marks = [45, 67, 56, 70, 62]
science_marks = [50, 60, 58, 65, 68]
plt.plot(roll,math_marks,color='green',marker='^',label='Maths')
plt.plot(roll,science_marks,color='blue',linestyle='dashed',marker='o',label='Science')
plt.title("Student Marks Comparison")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.legend(loc='best')
plt.grid(True)
plt.ylim(40,80)
plt.show()

