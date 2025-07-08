from operator import index

import numpy as np
'''mrp=np.array([1000,750,600,850,1200])
disc=mrp-(mrp*.1)
gst=disc+disc*.18
print(f"price={gst}")
marks=np.array([
    [78,85,90],
    [65,70,60],
    [80,88,84],
    [50,45,55],
    [92,95,96]

])
sum=print(marks.sum(axis=1))
avg=marks.mean(axis=1)
print(avg)
print(max(avg))
print(min(avg))
salaries=np.array([25000,30000,28000,35000,40000,37000])
hra=salaries*.2
print(hra)
income=salaries+hra
print(income)
inc_tax=income-income*.1
print(inc_tax)'''
'''num=np.array([100,200,300])
print(num.std())
num1=np.array([1000,2000,3000])
print(num1.std())'''
'''units=np.array([
    [120,110,115,130,125,118,121],
    [100,98,97,105,103,99,101],
    [140,138,142,150,145,143,139]
])'''
'''sum=units.sum(axis=1)
print(sum)
av=units.mean(axis=1)
print(av)
print(max(units[:,3]))
print(max(units.sum(axis=0)))
print(units.sum(axis=0))'''
'''refill = np.array([
    [5,3,0,2,4],
    [0,0,1,0,2],
    [3,4,2,4,3],
    [1,1,0,1,0]
])
l=(refill==0)
p=np.sum(l,axis=1)
print(p)
for i in refill:
    if i == p:
        print(i)'''


#4 pdcts 5 days#
'''print(refill.sum(axis=1))
print(max(refill.sum(axis=0)))

delivery_time=np.array([28,35,32,40,30,45,38,25])
avg=delivery_time.mean()

count=0
for i in delivery_time:
    if i>avg:
        count=count+1

a=np.copy(delivery_time)
a[a>40]=40
print(a)
perc=np.percentile(delivery_time,75)
print(perc)
print(b)
hours=np.array([
    [8,9,7,8,6],
    [9,8,8,9,7],
    [7,7,6,8,7],
    [8,8,9,8,8]
])
'''
'''print(hours.sum(axis=1))
print(hours.mean(axis=1))
print(hours.transpose())
print(hours[:,2])'''
np.random.seed(10)
stock=np.random.randint(50,150,size=(4,6))


low=stock.sum(axis=0)
min=low[0]
for i in stock:
    print(i)
for items in low:
    if min>items:
        min=items
print("\n")
print(low)
print(min)
for i in low:
    print(i)
'''base_price=np.array([
    [100,120,130],
    [110,125,130],
    [115,130,140],
    [120,135,150]
])
seasonal_increase=np.array([1.05,1.10,1.15])
newp=seasonal_increase+base_price
print(newp)
print(newp-base_price)
'''










