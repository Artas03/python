from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Mammal(Animal):
    def eat(self):
        print("nom nom")

# @abstractmethod decorator is used so any subclass created must have its own implementation.

