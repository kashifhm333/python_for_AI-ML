class footballer:
    def __init__(self,name, country, position):  # self means the object that called the constructor
        self.name = name
        self.country = country
        self.position = position
        print("This is a constructor", self.name, self.country, self.position)
        

f1= footballer("Ronaldo","Portugal", "Forward")
f2= footballer("Messi","Argentina", "Forward")




# another example of constructor

class students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
s1 = students("Alice", 20, "A")

print(s1.get_grade())
s2 = students("Bob", 22, "B")
print(s2.get_grade())




# There are two types of constructors in python

# 1. default constructor: it is only one parameter which is self and it does not take any arguments, it is used to initialize the attributes of the class with default values
# 2. parameterized constructor: it is a constructor that takes parameters and it is used to initialize the attributes of the class with the values passed as arguments
