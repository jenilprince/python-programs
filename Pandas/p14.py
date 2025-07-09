import pandas as pd
std=pd.read_csv("students.csv")
std["Total"]=std["Math"]+std["Physics"]+std["Chemistry"]+std["English"]+std["Computer"]
std["Percent"]=(std["Total"]*100)/500
def grade(mark):
    if mark>=91:
        return "A"
    elif 90>=mark>80:
        return "B"
    elif 80>=mark>70:
        return "C"
    elif 70>=mark>60:
        return "D"
    elif 60>=mark>50:
        return "E"
    elif 50>=mark>40:
        return "F"
    else:
        return "Fail"
std["Grade"]=std["Percent"].apply(grade)
print(std)
