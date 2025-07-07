###STRING REVERSING#
num = int(input("Enter a number: "))
str = str(num)
reverse = ' '
for i in str:
    reverse = i + reverse
print(reverse)