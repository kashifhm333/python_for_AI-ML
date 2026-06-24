class employee:
    start_time= "9:00"
    end_time = "5:00"
        

class teachers(employee):
    def __init__(self,subeject):
        self.subeject = subeject
        


        
        

t1 = teachers("maths")

print(t1.subeject )
print(t1.start_time) # it will give an error because the start_time attribute is not defined in the teachers class
print(t1.end_time) # it will give an error because the end_time attribute is not defined in the teachers class