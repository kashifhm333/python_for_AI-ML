class Employee:
    start_time = "9:00"
    end_time = "5:00"
    

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
        

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary
        
        
        

a1 = Accountant(50_000, "Senior Accountant")
print(a1.salary , a1.role)