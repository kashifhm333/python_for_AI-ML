# here is the example of multiple inheritance in python

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa
        

class TA (Teacher, Student):
    def __init__(self, salary, gpa, name):
        Teacher.__init__(self, salary)
        Student.__init__(self, gpa)
        self.name = name
        
        
ta1 = TA(30_000, 3.5, "John Doe")
print(ta1.name, ta1.salary, ta1.gpa)