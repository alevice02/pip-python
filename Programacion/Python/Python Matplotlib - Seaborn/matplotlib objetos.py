import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.2,0.2])
#genera un lienzo con ejes (x,y(posicion en el lienzo)  , x,y (tamanio de los axes))
#se puede generar un subplot basado en proporciones numericas con esto
axes.plot(x,y)
axes2.plot(y,x,'r')
axes2.set_facecolor('gray')
#sirve para poner un fondo detras de la imagen
plt.show()




