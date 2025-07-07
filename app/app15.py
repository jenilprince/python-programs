def fact(num):
    prod=1
    for i in range(1,num+1):
        prod = prod * i
        i+=1
    print(prod)
fact(5)
