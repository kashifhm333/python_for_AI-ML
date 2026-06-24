class bank_account:
    def __init__ (self,name, balance):
        self.name = name
        # self._balance= balance  # protected attribute
        self.__balance = balance  # private attribute
        # to access the private attribute we can use getter and setter methods
        
    def get_balance(self):  # getter method
        return self.__balance
    
    def set_balance(self, new_balance):  # setter method
        self.__balance = new_balance



a1 = bank_account("kashif",100_000)

a1.set_balance(200_000)  # updating the private attribute using setter method


# print(a1.name, a1._balance)  # accessing the protected attribute
# print(a1.name, a1.__balance)  # accessing the private attribute


print(a1.name, a1.get_balance())  # accessing the private attribute using getter method