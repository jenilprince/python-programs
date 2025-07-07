## PRINT MULTIPLICATION TABLES ##
inp = int(input('Enter a number: '))
table = 1

while table <= inp:
    pro = 1
    while pro <= 10:
        print(f'{table} * {pro} = {table * pro}')
        pro += 1
    print()
    table += 1