## DISPLAY ARMSTRONG NUMBER ##
start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))
for i in range(start, end+1):
    string = str(i)
    sum = 0
    pow = 0
    for num in string:
        pow+=1
    for num in string:
       las = int(num)%10
       sum=sum+ las**pow
       if sum==i:
           print(i)


