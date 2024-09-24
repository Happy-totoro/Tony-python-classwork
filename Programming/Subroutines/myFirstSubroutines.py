def multiply(a: int, b: int) -> None: #parameters -local variables in the subroutine
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

#passing by arguments: 
#passing by refrences:

#refrence refers to the memory address of the variable that has been assigned to it.