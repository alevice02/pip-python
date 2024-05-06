import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

plt.subplot(1,2,1)
plt.plot(x,y,'ro--')
plt.plot(y,x,'bo--')
#si se ponen dos graficos en el mismo subplot salen ploteadas como dos series
plt.subplot(1,2,2)
plt.pie(y)
plt.show()
#el subplot permite tener varios graficos en una sola ventana, (fila, columna, posicion)

plt.subplot(2,2,1)
plt.plot(x,y,'ro--')
plt.plot(y,x,'bo--')
plt.subplot(2,2,2)
#si se pone numero de filas y columnas arma un cuadro y lsa ordena de izquierda a derecha
plt.pie(y)
plt.show()
