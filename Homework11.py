class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ('_z',)  # Ограничиваем допустимые атрибуты

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        raise AttributeError("Изменение координаты z запрещено")


# Тестовый сценарий
pt3 = Point3D(10, 20, 30)
print(f"x: {pt3.x}, y: {pt3.y}, z: {pt3.z}")  # x: 10, y: 20, z: 30

try:
    pt3.z = 40
except AttributeError as e:
    print(f"Ошибка: {e}")  # Ошибка: Изменение координаты z запрещено

try:
    pt3.extra = 100
except AttributeError as e:
    print(f"Ошибка: {e}")  # Ошибка: 'Point3D' object has no attribute 'extra'

try:
    print(pt3.__dict__)
except AttributeError as e:
    print(f"Ошибка: {e}")  # Ошибка: 'Point3D' object has no attribute '__dict__'







# Nomer 2
import sys
import timeit

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class SlotPoint:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def compare_performance():
    normal_points = [NormalPoint(1, 2) for _ in range(1000)]
    slot_points = [SlotPoint(1, 2) for _ in range(1000)]
    
    normal_time = timeit.timeit(
        'for point in normal_points: point.move(1, 1)',
        globals=globals(),
        number=1000
    )
    
    slot_time = timeit.timeit(
        'for point in slot_points: point.move(1, 1)',
        globals=globals(),
        number=1000
    )
    
    print(f"NormalPoint time: {normal_time:.6f}")
    print(f"SlotPoint time: {slot_time:.6f}")

def compare_memory_usage():
    normal_point = NormalPoint(1, 2)
    slot_point = SlotPoint(1, 2)
    
    print(f"NormalPoint size: {sys.getsizeof(normal_point)}")
    print(f"SlotPoint size: {sys.getsizeof(slot_point)}")

if __name__ == "__main__":
    compare_performance()
    compare_memory_usage()





# Nomer 3
class Student:
    __slots__ = ('name', 'age', 'grade')
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def calculate_average_grade(students):
    total = sum(student.grade for student in students)
    return total / len(students)

students = [
    Student("Иван", 20, 4.5),
    Student("Мария", 19, 5.0),
    Student("Алексей", 21, 3.8),
    Student("Елена", 20, 4.2),
    Student("Дмитрий", 22, 4.7)
]

average_grade = calculate_average_grade(students)
print(f"Средняя оценка: {average_grade:.2f}")







# Nomer 4
class Product:
    __slots__ = ('name', 'price', 'quantity')
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def find_expensive_products(products, threshold):
    return [name for name, product in products.items() if product.price > threshold]

# Создаем словарь товаров
products = {
    "Ноутбук": Product("Ноутбук", 75000, 5),
    "Смартфон": Product("Смартфон", 45000, 10),
    "Планшет": Product("Планшет", 30000, 8),
    "Наушники": Product("Наушники", 5000, 20),
    "Монитор": Product("Монитор", 25000, 7)
}

# Ищем товары дороже 40000
threshold = 40000
expensive_products = find_expensive_products(products, threshold)

print(f"Товары дороже {threshold} руб:")
for product_name in expensive_products:
    print(f"- {product_name} ({products[product_name].price} руб)")
