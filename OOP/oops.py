class Student:
    subject= "python"
    univeristy = "oxford"
    year= "4th year"
    
std1= Student() # it will create an object std1 of the class Student

# print(std1)     it whill print the memory address of the object std1

print(std1.subject, std1.univeristy, std1.year) # it will print the values of the attributes of the object std1



#now how to store in the list datatype
std2= Student() # it will create an object std2 of the class Student
std3= Student() # it will create an object std3 of the class Student

students = [std1, std2, std3] # it will create a list of student objects


for student in students:
    print(student.subject, student.univeristy, student.year) # it will print the values of the attributes of each student object in the list students   