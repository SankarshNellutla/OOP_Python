# Creating class

class Car():
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You're driving the {self.color} {self.model}")
        
    def stop(self):
        print(f"You stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


## Class Variable

class Student():

    class_grad_year = 2023
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


## Inheritance

class Animal():
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animal):
    def speak(self):
        print("Bow!")

class Cat(Animal):
    def speak(self):
        print("Meeyaam!")

class Mouse(Animal):
    def speak(self):
        print("chuu chuuu!")