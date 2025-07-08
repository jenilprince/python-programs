import matplotlib.pyplot as plt
weeks = [1, 2, 3, 4, 5]
shoes = [1200, 1350, 1100, 1500, 1450]
bags = [1000, 1250, 1150, 1400, 1300]
plt.plot(weeks,shoes,color='red',marker='s',label='Shoes')
plt.plot(weeks,bags,color='purple',linestyle='dotted',marker='*',label='Bags')
plt.title("Product Sales Over 5 Weeks")
plt.xlabel("Week Number")
plt.ylabel("Sales (₹)")
plt.legend(loc='best')
plt.ylim(900,1600)
plt.grid(True)
plt.show()