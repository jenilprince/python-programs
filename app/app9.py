##PRINT FIBONACCI SEQUENCE##
num = int(input("Enter a number: "))
fib1 = 0
fib2 = 1
while fib1<=num:
    print(fib1)
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3