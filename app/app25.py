def div():
    a=int(input("Number: "))
    div=100/a
    print(div)
while True:
    try:
        div()
        break
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print("Not Possible")