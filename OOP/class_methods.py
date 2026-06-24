class laptop:
    storage_type = "SSD"  # class attribute
    count = 0
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        laptop.count += 1
    
    # @classmethod 
    # def get_storage_type(cls):
    #     print("The storage type of the laptop is:", cls.storage_type)

    def get_ram(self):
        print("The ram of the laptop is:", self.ram)
        
        
    @staticmethod
    def discount(price, discount):
        discounted_price = price - (price * discount / 100)
        print("The discounted price of the laptop is:", discounted_price)
        
        
    
    def get_storage(self):
        print("The storage of the laptop is:", self.storage)
        
    @classmethod
    def count_laptops(cls):
        return cls.count

l1 = laptop("16GB", "512GB")  # creating an object of the class laptop
l2 = laptop("8GB", "256GB")  # creating another object of the class laptop
# l1.get_storage_type()  # calling the class method using the object of the class
# laptop.get_ram()  # calling the class method using the class name



print(l1.ram)  # accessing the instance attribute using the object of the class
print(l1.storage)  # accessing the instance attribute using the object of the class
laptop.discount(1000, 10)  # calling the static method using the class name


print("total laptops:", laptop.count_laptops())  # calling the class method using the class name


# for the count
