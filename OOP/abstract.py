from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Dog(Animal):
    def make_sound(self):
        print("Woof")


lion = Lion()
lion.make_sound()


dog = Dog()
dog.make_sound()