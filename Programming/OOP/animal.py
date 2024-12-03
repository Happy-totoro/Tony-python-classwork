class Animal:
    def __init__(self,type, name,colour) -> None:
        self.type = type
        self.name = name
        self.colour = colour
    #end constructor method


    def eat(self):
        pass
    #end public procedure

    def makeNoise(self):
        print("Meow")
    #end public procedure

    def move(self):
        pass
    #end public procedure
#end class

my_animal = Animal("Unknown","Adam","Yellow")
print(f"type {my_animal.type} name {my_animal.name} colour {my_animal.colour}")
my_animal.makeNoise()



class Dog(Animal):
    pass
#end class

my_dog = Dog("mammal","fido","Black")
print(f"type {my_dog.type} name {my_dog.name} colour {my_dog.colour}")
print("End")

"""
inheritance class contains all the methods and attributes of its parent class.
polymorphism is the ability to process objects differently based on its class
"""