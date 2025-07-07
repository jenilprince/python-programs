#factorial
num = int(input("Enter a number: "))
prod = 1
fact = 1
while prod<= num:
    fact = prod*fact
    prod += 1
print(fact)