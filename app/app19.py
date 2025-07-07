with open ('app19.txt', 'r') as file:
    count=file.readlines()
    print(len(count))
    while len(count) <= 100:
        with open('app19.txt', 'a') as file:
            write=file.write('This is my Python Project. I am adding text into app19.txt\n')
        with open('app19.txt', 'r') as file:
            read=file.read()
            print(read)


