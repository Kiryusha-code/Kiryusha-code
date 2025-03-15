import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def f1(x):
    return x**3 - x
def f2(x):
    return 2*x-1
def diff(x):
   return f1(x) - f2(x)
x_roots = fsolve(diff, [-2,0,2])
y_roots = f1(x_roots)
x = np.linspace(-3,3,500)
y1 = f1(x)
y2 = f2(x)
plt.figure(figsize=(6,10))
plt.plot(x, y1, label='y1 = x^3 - x')
plt.plot(x, y2, label='y2 = 2x - 1')
plt.plot(x_roots, y_roots, 'ro', label='Точки пересечения')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций y1 = x^3 - x и y2 = 2x - 1')
plt.legend()
plt.grid(True)
plt.show()
for i in range(len(x_roots)):
   print('Точка пересечения  {i+1}: x = {x_roots[i]:.4f}, y = {y_roots[i]:.4f}')       

   