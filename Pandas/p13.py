import pandas as pd
data = pd.read_csv("data.csv")
data.loc[data["Title"]=="Inception", 'Rating']=8.9
#First it locates the title "Inception" and then goes to Rating column, changes the value of rating
print(data)