# Задача 1
class Car:
   

    def __init__(self, make, model):
       
        self.make = make
        self.model = model

    def __getattr__(self, item):
       
        return "This attribute is not available"


# Пример использования
c = Car("Toyota", "Corolla")
print(c.make)
print(c.model)
print(c.color)

# Задача 2
class Rectangle:
    

    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        
        if name not in self.__dict__:
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(name, value)

# Пример использования
r = Rectangle(10, 5)
print(r.width)
print(r.height)

try:
    r.color = 'red' 
except AttributeError as e:
    print(e) 

r.width = 20 
print(r.width)