# There are two types of polymorphism in Python: compile-time polymorphism and run-time polymorphism.
#1 Compile-time polymorphism is also known as static polymorphism. It is achieved through method overloading and operator overloading. In Python, method overloading is not directly supported, but we can achieve it using default arguments or variable-length arguments.
#2 Run-time polymorphism is also known as dynamic polymorphism. It is achieved through method overriding. In Python, method overriding is supported, and it allows a subclass to provide a specific implementation of a method that is already defined in its superclass.



# overriding     here is an example of run-time polymorphism in Python using method overriding:
class Animal:
    def make_sound(self):
        print("Animal makes a sound")
        

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the make_sound method on each instance
animal.make_sound()
dog.make_sound()
cat.make_sound()






# duck typing     here is an example of run-time polymorphism in Python using duck typing:
class Teacher:
    def get_designation(self):
        print("designation: Teacher")
        
class Accountant:
    def get_designation(self):
        print("designation: Accountant")


# Creating instances of the classes
teacher = Teacher()
accountant = Accountant()

# Calling the get_designation method on each instance
teacher.get_designation()
accountant.get_designation()
