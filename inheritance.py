# Single Inheritance
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Multiple Inheritance
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

# Multilevel Inheritance
class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    def honk(self):
        return "Honk!"

class ElectricCar(Car):
    def charge(self):
        return "Charging"

# Hierarchical Inheritance
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def area(self):
        return "Circle area"

class Square(Shape):
    def area(self):
        return "Square area"

# Hybrid Inheritance
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def rotate(self):
        return "Wheels rotating"

class Automobile(Engine, Wheels):
    pass

class Truck(Automobile):
    def load(self):
        return "Loading cargo"

# Testing
if __name__ == "__main__":
    dog = Dog()
    print(dog.speak())
    
    duck = Duck()
    print(duck.fly(), duck.swim())
    
    e_car = ElectricCar()
    print(e_car.honk(), e_car.charge())
    
    circle = Circle()
    print(circle.area())
    
    truck = Truck()
    print(truck.start(), truck.rotate())