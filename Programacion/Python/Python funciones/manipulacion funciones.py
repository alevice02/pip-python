import numpy as np
import matplotlib.pyplot as plt

n = 100
c = 5

def f(x):
    return np.sin(x)

def g(x):
    return np.sqrt(x)

x = np.linspace(-10,10,n)
y = f(x)
y1 = f(x+c)
#desplazamiento a la izquierda de la funcion
y2 = f(x)*(c)
#alarga en la vertical
y3 = f(x*c)
#comprime en la horizontal
y4 = f(x*(1/c))
#alarga en la horizontal

y5 = g(-x)
#se refleja la funcion en el eje y
y6 = -g(x)
#se refleja la funcion en el eje x
y7 = g(x)


fig, ax = plt.subplots()
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
'''
ax.plot(x,y,'b',label='f(x)')
ax.plot(x,y1,'r',label='f(x+c)')
ax.plot(x,y2,'g',label='f(x)*(c)')
ax.plot(x,y3,'y',label='f(x*c)')
ax.plot(x,y4,'m',label='f(x*(1/c))')
'''
ax.plot(x,y5,'k',label='f(-x)')
ax.plot(x,y6,'c',label='-f(x)')
ax.plot(x,y7,'b',label='f(x)')
ax.legend()
plt.show()