def find_elements_by_index(values, indices):
    result = []
    for index in indices:
        try:
            result.append(values[index])
        except IndexError:
            return f"Ошибка: индекс {index} выходит за границы списка"
    return result

# Примеры использования
numbers = [10, 20, 30, 40, 50]
good_indices = [0, 2, 4]
bad_indices = [1, 3, 5]

print(find_elements_by_index(numbers, good_indices))  # [10, 30, 50]
print(find_elements_by_index(numbers, bad_indices))    # Ошибка: индекс 5 выходит за границы списка




# Nomer 2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

# Пример использования
circle = Circle(5)
print(f"Радиус: {circle.radius}")
print(f"Диаметр: {circle.diameter}")
print(f"Площадь: {circle.area():.2f}")
