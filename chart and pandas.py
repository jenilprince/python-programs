import matplotlib.pyplot as plt
data=[88,99,42,55]
labels=["alex","anu","jack","man"]
colors=["red","green","blue","yellow"]
explode=[0.0,0.0,0.1,0.0]
plt.pie(data,labels=labels,colors=colors, autopct="%1.0f%%",explode=explode)
plt.title("marks")
plt.show()
