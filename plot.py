#Функция  y=x^3 + 3*x^2 + 9x + 7
import matplotlib.pyplot as plt
import matplotlib as mlt
import numpy as np
def f(x):
    return x**3 + 3*x**2 + 9*x + 7
x = np.arange(1,30,1)
y = f(x)
plt.plot(x,y)
plt.show()