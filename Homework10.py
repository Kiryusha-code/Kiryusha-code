class Animal:
    def speak(self):
        return "издает звук"


class MixinSwim:
    def swim(self):
        return "плавает"


class MixinFly:
    def fly(self):
        return "летает"


class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "кря-кря"


class Penguin(Animal, MixinSwim):
    def speak(self):
        return "буль-буль"


animals = [Duck(), Penguin()]

for animal in animals:
    print(f"{animal.__class__.__name__}:")
    print(f"- {animal.speak()}")
    print(f"- {animal.swim()}")
    if isinstance(animal, MixinFly):
        print(f"- {animal.fly()}")
    print()
