import numpy as np
import matplotlib.pyplot as plt

n = 100

def g(x):
    return x**2

def f(x):
    return np.sin(x)

x = np.linspace(-10,10,n)

f_g = f(g(x))
#son funciones dentro de otra

fig, ax = plt.subplots()
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
#genera los ejes de color rojo con la grilla
ax.plot(x,f_g)
plt.show()
