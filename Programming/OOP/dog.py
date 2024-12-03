class Dog:
    def __init__ (self, myName, myColor):
        self.name = myName
        self.color = myColor
    #endProcedure


    def bark(self, barkTimes):
        for _ in range(barkTimes):
            print("woof!")
            #next _
    #endMethod

    def setColor(self, color):
       self.color = color
    
    def getColor(self):
        return self.color
#endClass

my_dog = Dog("Fido", "Black")
my_dog.bark(2)
print(my_dog.name)
print(my_dog.getColor())
my_dog.setColor("Blue")
print(my_dog.getColor())
print("Program Over")

"""
Arrtibutes are normally declared as pivate
Encapsulation wraps the attributes and methods in the class definition, hiding details of the implementation from the user
Eg. names.sort()
Don't know how names are sorted or what attributes are defined in the class List, of which names is an object
"""
"""
Setter and getter methods:
needs a means to set an attribute, or to find out the value of an attribute
OOP shares a characteristic of data hiding, which means cannot directly access or change an attribute of the object
This has to be done via a getter or setter method
"""