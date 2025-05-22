class Animal:
    def sound(self):
        return "Звук животного"


class Dog(Animal):
    def sound(self):
        return "Гав-гав"


class Cat(Animal):
    def sound(self):
        return "Мяу"


class Cow(Animal):
    def sound(self):
        return "Муу"


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.sound())
