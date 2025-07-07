def spy(start,end):
    list = []
    for x in range(start,end):
        st = str(x)
        sum = 0
        prod = 1
        for i in st:
            d=int(i)
            sum+=d
            prod*=d
        if sum==prod:
            list.append(x)
    print(list)
spy(1,10000)

