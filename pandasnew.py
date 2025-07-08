import pandas as pd
'''name=pd.Series(["a","b","c","d","e","f","g","h"])
print(name)
data={
    "Name": ["Ali", "Sara","John"],
    "English": [85,90,78],
    "Maths": [88,92,79]
}
frame=pd.DataFrame(data)
print(frame)'''
read=pd.read_csv('students.csv')

'''print(read.head(2))
print(read.tail(2))
print(read.shape)
print(read["English"])
print(read[["Maths","Science"]])
print(read.loc[0])
print(read.iloc[1])
more85=read[read["Maths"]>85]
print(more85)
read["Total"]=read["Maths"]+read["Science"]+read["English"]
print(read)
print(read.sort_values(by=["Science"], ascending=False))'''

