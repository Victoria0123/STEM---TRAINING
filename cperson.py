class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def details(self):
        print("My name is{self.name} and my age is {self.age}")    
p1=Person("Felix", 22)
p1.details()

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary
p2=Employee("Felix",22,5000)
p2.details()

class Person:
    def __init__(self, name,date of birth, weight, height):
        self.name=name
        self.age
