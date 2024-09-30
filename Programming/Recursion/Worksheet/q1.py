def addOne(n):
    if n<4:
        print(n)
        addOne(n+1)
    else:
        print(n)
addOne(1)