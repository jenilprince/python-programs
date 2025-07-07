##FACTORIAL FINDER##
inp = int(input('Enter a number: '))
while inp<0:
    print("Invalid number: ")
    inp = int(input('Enter a number: '))
start = 1
fact = 1
while start<=inp:
    fact = fact*start
    start = start+1
print(fact)

