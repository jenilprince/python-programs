num1 = int(input('Enter a start number: '))
num2 = int(input('Enter an end number: '))
if num1 > num2:
    num1, num2 = num2, num1
while num1<=num2:
    print(num1**3, end=' ')
    num1 += 1



