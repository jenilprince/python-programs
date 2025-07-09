import pandas as pd
data=pd.read_csv("movies.csv")

def rate(rating):
    if rating>=9:
        return "Masterpiece"
    elif 9>rating>=8:
        return "Excellent"
    elif 8>rating>=7:
        return "Good"
    else:
        return "Average"
data["Category"]=data["Rating"].apply(rate)
print(data)