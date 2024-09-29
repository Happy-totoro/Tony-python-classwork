a = 10
print(a)
a = 15
print(a)
while a>0:
    a = a-1
    myvalue = a
#endwhile
print(myvalue)
total = 0
for n in range(5):
    total = total+n
#next n
print(total//n)

def mySub():
    #global a -> This line would make the interpreter take the 'a' value outside the scope
    a = 54  #This 'a' is different from the global 'a', it is local
    print(a)
#end procedure
print("a:", a)
mySub()
print("a", a)

#pros of local variables
#independent of a particular program and can be reused in diferent programs
#pros of modular programming
""" -> modular programming means to seperate different tasks into modules
easily and quickly written:
large prgrams are broken down into subtasks that are eaiser to program and manage
each module can be individually tested
modules can be reused several times in a program
large programs are much easier t o debug and maintain
"""