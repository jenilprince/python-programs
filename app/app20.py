with open ('app19.txt', 'r') as file:
    read=file.read()
    org="org: " + read
    print(org)
    rev=read[::-1]
    print(rev)


