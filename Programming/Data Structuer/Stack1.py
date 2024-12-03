#class
class MyStrStack():
    #constructor
    def __init__(self, size) -> None:
        self.sp = -1
        self.max = size
        self.data = ["" for _ in range(size)] #array created in python (since array cant be changed once it is created)
    def is_empty(self) -> bool:
        # if self.sp == -1:
        #     return True
        # else:
        #     return False
        return self.sp == -1
    #end procedure
    def is_full(self) -> bool:
        # if self.sp + 1 == self.max:
        #     return True
        # else:
        #     return False
        return self.sp + 1 == self.max
    #end procedure
    def pop(self):
        #if not empty
        if not self.is_empty():
            temp = self.data[self.sp]
            self.data[self.sp] = ""
            self.sp = self.sp - 1
            return temp
        else:
            print("Stack is empty")
            return ""
        #end if
    #end procedure
    def push(self, item):
        #if not full
        if not self.is_full():
            self.sp = self.sp +1
            self.data[self.sp] = item
        else:
            print("Stack is full")
        #end if
    #end procedure
    def peek(self):
        #if not empty
        if not self.is_full():
            return self.data[self.sp]
        else:
            print("Stack is empty")
            return ""
        #end if
    #end procedure
    # def __repr__(self) -> str:
    #     return ":".join(self.data())
#end class
stack1 = MyStrStack(3)

for c in "abcde":
    stack1.push(c)
for _ in range(5):
    print(stack1.pop())