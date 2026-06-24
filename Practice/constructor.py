class student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    
    def name(self):
        return self.name
    
    @classmethod
    def age(cls, age):
        return age








# s1 = student("Ronaldo", 38)
# print(s1.name)

print(student.name("Ronaldo"))   #it will give error because name is not a class method, it is an instance method. we need to create an instance of the class to access the name method.
print(student.age(38))

