start = int(input('Enter a start number: '))
end = int(input('Enter an end number: '))
if start>end:
    start, end = end, start
if start%2 == 0:
    start += 1
while start<=end:
    print(start, end=' ')
    start +=2