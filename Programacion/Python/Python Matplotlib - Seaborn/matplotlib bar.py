import matplotlib.pyplot as plt
import numpy as np

country = ['India','Japan','Colombia', 'Germany', 'Brazil', 'Argentina']
population = [1000, 800, 900, 1000, 300, 500]

plt.bar(country, population, width=0.5, color=['red','blue','green','black','magenta','yellow'])
#las barras usan dos valores el x y el y, se puede cuadrar el ancho, y los colores de las barras
plt.xticks(np.arange(6),('Ind','Jap','Col', 'Ger', 'Bra', 'Arg'), rotation=45)
#se puede cuadrar los labels de cada barra y rotarla
plt.title('World Cup stats')
plt.xlabel('Countries')
plt.ylabel('Goals in world cups')
plt.tight_layout()
plt.show()