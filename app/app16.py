'''a=[1,3,4,4,4,4,2,5]
c=a.copy()
a.insert(5,6)
a.index(6)
a.sort()
print(a.count(4))
print(a)
c.sort()
print(c)
s="Thiruvananthapuram"
cal = "Supercalifragilisticexpialidocious"
print(list(cal))
print(len(list(cal)))
print(list(s))
print(len(list(s)))
tup = (1,2,0,0,0,0,0,0,0,2,3,3,3,2,7,4,2,1,1,3,4,5)
print(tup)
print(tup.count(min(tup)))
print(tup.count(0))
list=[9,10,8,7,5,6,3,4,1,2]
c=list.copy()
list.sort(reverse=True)
print(list[::2])
print(list)
#TO PRINT SQUARE NO.S INSIDE A LIST#
def sq(x):
    print(x*x)
sq(2)
sq(9)
sqlist=[x**2 for x in range(100)]
print(sqlist)
#DISPLAY A LIST OF PRIMES#
primes=[x for x in range (2,100) if all (x%i!=0 for i in range(2,x//2+1))]
print(primes)
#DISPLAY HARSHAD NO.S IN INTERVAL IN LIST#
hars=[x for x in range(1,101) if x%sum(int(d) for d in str(x))==0]
print(hars)
#DISPLAY SPY NO.S IN INTERVAL IN LIST#
spy=[x for x in range(1,1000) if sum(int(dig) for dig in str(x))==(a*b for a,b in str(x))]
print(spy)'''







