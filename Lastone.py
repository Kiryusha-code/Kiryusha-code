import math
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1,10,500)
y = np.log(x)
plt.plot(x,y, label = 'y = ln(x)')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title('График функции вида: y = ln(x)')
plt.legend()
special_points_x = [1, math.e]
special_points_y = [np.log(i) for i in special_points_x]
plt.plot(special_points_x, special_points_y, 'ro')
for i in range(len(special_points_x)):
    plt.annotate(f"((special_points_x[i]:.1f), (special_points_y[i]:.1f))", (special_points_x[i], special_points_y[i]), 
                 textcoords="offset points", xytext = (5,5), ha = 'left')
    plt.show()