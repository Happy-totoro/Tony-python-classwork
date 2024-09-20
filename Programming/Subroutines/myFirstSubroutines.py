def multiply(a: int, b: int) -> None: #parameters
    print("the product is:", a*b)
#end procedure
multiply(2, 5) #arguments
"""
parameters appear in subroutine definitions
arguments appear in subroutine calls

"""
def proc1(x, y) -> None:
    x = x-2
    y = 0
#end procedure
m = 8
n = 10
proc1(m, n)
print(m, n)