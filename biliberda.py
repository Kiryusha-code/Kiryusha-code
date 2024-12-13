import matplotlib.pyplot as plt
import numpy as np

# Определяем функции
def f(x):
    return x**2

def g(x):
    return 2*x + 3

# Создаем массив значений x
x = np.arange(0, 6)  # Целые числа от 0 до 5

# Вычисляем значения функций для каждого x
y_f = f(x)
y_g = g(x)

# Создаем столбчатые графики
width = 0.35  # Ширина столбцов

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, y_f, width, label='f(x) = x²')
rects2 = ax.bar(x + width/2, y_g, width, label='g(x) = 2x + 3')

# Добавляем подписи к столбцам
ax.set_ylabel('Значение функции')
ax.set_xlabel('x')
ax.set_title('Графики функций f(x) = x² и g(x) = 2x + 3')
ax.set_xticks(x)
ax.legend()

# Добавляем подписи значений над столбцами
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom') #исправил ошибку

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()