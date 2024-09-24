#Subroutine
def multiply(x:int, y:int) ->None:
    print("Product:")
    print(x*y) #->end procedure
multiply(2, 5)

#Function
def multiply2(x:int, y:int) ->int:
    product = x*y
    return product #->end function
answ = multiply2(2, 5)
print("Product:", answ)

""" #Variable Scope
A global variable can be seen throughout the whole program
A local variable can be only seen in part of the program
"""