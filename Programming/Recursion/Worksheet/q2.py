n = int(input("Enter number:"))
if n%2 != 0:
    n +=1
else:
    n = n
def sumEven(n:int)->int:
    sum = 0
    if n == 0:
        return 0
    else:
        sum += n +sumEven(n-2)
        return sum
print(sumEven(n))