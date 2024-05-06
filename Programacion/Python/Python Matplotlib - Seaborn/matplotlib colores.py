import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

plt.style.use('dark_background')
#es el tema que usa el grafico, para ver los disponibles usar plt.style.available
#classic, dar+background, grayscale

fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x, x+1, color = 'red', linestyle= 'dotted', marker='v', markersize= 10, markerfacecolor= 'green')
ax.plot(x, x+2, color='#ADD8E6', alpha=0.5, linewidth = 5, linestyle= (0, (1,10)))
#se puede poner como color y el nombre en hex del rgb
#alpha es transparencia
#linewidth ancho de la linea
#linestyle es el brodeado de la linea en la documentacion de plt hay hartas opciones
#marker es el simbolito
#markesize es el tamanio
#markerfacecolor es el color del marker
ax.plot(x, x+3, 'go-')
ax.plot(x, x+4, 'mx-')
ax.set_title('Prueba')
fig.tight_layout()
plt.show()

