class person:
    def __init__(self, name, date_of_birth, weight, height):
        self.name=name
        self.date_of_birth=date_of_birth
        self.height=height
        self.weight=weight
    def print_age ()
    def details ():
        print(f"my name is {self.name}", "my date_of_birth is{self.date_of_birth}", "my weight is {self.weight}" and "my height is {self.height}")    
parent1=parent("Sylvester","6th March 2021", 5.7, 67)
parent1.details()

class student:
    def __init__(self, stream, favsubject):
        self.stream=stream
        self.favsubject=favsubject
    def details(self):
        print(f"my stream is{self.stream} and my favsubject is {self.favsubject}") 
student1=student("form two Red", "Mathematics")
student1.details()

class teacher:
    def __init__(self, subject, salary):
        self.subject=subject
        self.salary=salary
    def details(self):
        print(f"my subject is {self.subject}, my salary is{self.salary}") 
teacher1=teacher("English", 68000)  
teacher1.details()         