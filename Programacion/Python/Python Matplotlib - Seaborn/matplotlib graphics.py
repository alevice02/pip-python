import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1,50,100)
#una lista de 100 numeros aleatorios enteros de 1 a 50 

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30* np.random.rand(n)) **2
color = np.random.rand(n)

plt.subplot(2,2,1)
plt.hist(data,bins=10,histtype='step')
#el histype step me muestra el contorno sin relleno del histograma
plt.subplot(2,2,2)
plt.boxplot(data, vert=False, patch_artist=True, notch=True, showfliers=False)
#vert es la orientacion en este caso horizontal, patch artist es el relleno de la caja
#el notch le pone una correa en la mediana a la caja
#el showfliers muestra o no los outliers o los puntos anomalos en la distribucion
plt.subplot(2,2,3)
plt.scatter(x,y, s=area, c=color, marker='o', alpha=0.5)
#x y y, area y color
plt.subplot(2,2,4)
plt.plot(data)
plt.tight_layout()
plt.show()