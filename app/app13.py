##TO CHECK IF A NO. IS PALINDROME##
num = int(input('Enter a number: '))
string = str(num)
reverse = ''
for i in string:
    reverse = i+reverse
if string == reverse:
    print("YES")
else:
    print("NO")