class bankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
a1 = bankAccount("Ronaldo", 1000)
print(a1.get_balance())   #it will give the balance of the account because we are