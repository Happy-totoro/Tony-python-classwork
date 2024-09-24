def multiples(table, startnum, endnum, pupilName) ->None:    
    print("Hi,", pupilName, "... here is your times table")
    for i in range(startnum, endnum+1):
        answ = table*i
        print(str(table), "*", str(i), "=")
        answ_from_user = int(input("What is the answer?:"))
        if answ_from_user == answ:
            print("Well done")
        else:
            print("Wrong. The correct answer should be:"+str(answ))
d = input("What is your name?:")
a = int(input("Enter times table:"))
b = int(input("Start number:"))
c = int(input("End number:"))
multiples(a, b, c, d)