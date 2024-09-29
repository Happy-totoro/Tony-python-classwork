#By value
def proc1(x:int, y:int) ->None:
    x = x-2
    y = 0
#end procedure
m = 8
n = 10
proc1(m, n)
print(m, n)

#By reference

def proc2(x:int, y:list) ->None:
    x = x-2
    y[0] = 0
#end procedure
j = 8
k = [10]
proc2(j, k)
print(j, k)