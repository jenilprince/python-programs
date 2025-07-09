import pandas as pd
data={
    'Name': ["Amal","Bobby","Charles","David","Edward"],
    'Age': [25,36,29,33,30],
    'Grade': ["A+","B","A","C","B+"]
}
table=pd.DataFrame(data)
print(table)