#Using class method for factory method
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return  cls(name,date.today().year - year)

    def display(self):
        print(f'{self.name} is {self.age} years old')

john = Person('John',21) #normal instance of class
john.display()

alex = Person.fromBirthYear('Alex', 2002) #call class method without creating object
alex.display()