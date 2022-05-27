#OOP
#Defining a class and its attributes
#Creating instances (objects) of a class
#Class methods (functions belonging to a class)
#Inheritance & polymorphism
#Method overriding

class Dog:
    def __init__(self, no_of_eyes, colour):
        self.no_of_eyes = no_of_eyes
        self.colour = colour
    def bark(self):
        print("Woof woof!")
    def walk(self):
        print("limp")

german_shepherd = Dog(no_of_eyes=2, colour='Grey')
dodger = Dog(no_of_eyes=1, colour='white') 
dobberman = Dog(2, 'brown')

print(german_shepherd.colour, german_shepherd.no_of_eyes)
print(dodger.colour, dodger.no_of_eyes)
print(dobberman.colour)

dobberman.colour = 'dark-brown'
print(dobberman.colour)
dobberman.bark()
dobberman.walk()
dodger.walk()