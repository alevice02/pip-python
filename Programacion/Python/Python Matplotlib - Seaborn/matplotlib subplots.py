import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots(nrows=2, ncols=4)
#genera una figura y la cantidad de graficas que se indique en filas y columnas, en una sola linea de codigo
axes[0,0].plot(x,np.cos(x),'b.-')
axes[0,1].plot(x,np.tan(x),'ro--')
axes[1,0].plot(x,y,'kx-.')
axes[1,1].plot(x,np.exp(x),'y>:')
axes[0,2].plot(x,np.arccos(x),'c*-')
axes[0,3].plot(x,np.arctan(x),'kD--')
axes[1,2].plot(x,y**2,'gv-.')
axes[1,3].plot(x,np.log10(x),'mo:')
#cada posicion en la red de figuras, debe ponerse como [fila, columna]
fig.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(8,5))
#fisgsize es el tamanio del lienzo
axes[0].plot(x,y,'bo-',label="$sin(x)$")
#con el label, se le pone leyenda a la serie
axes[0].set_title('Relacion x-sin(x)')
#pone titulo a la grafica
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
#etiqueta los ejes
axes[0].legend()
#genera leyenda siempre que se haya definido en el eje
axes[1].plot(x,np.cos(x),'ro-', label="$cos(x)$")
axes[1].set_title('Relacion x-cos(x)')
axes[1].set_ylabel('y')
axes[1].set_xlabel('x')
axes[1].legend()
fig.tight_layout()
plt.show()


#asi es directo en pyplot
plt.plot(x,y,'bo-',label="$sin(x)$")
plt.title('Relacion x - sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right',bbox_to_anchor=(1,0.5))
#loc es location de la leyenda, bbox es x y y
plt.show()


#con el orientado a objetos se puede graficar graficas usando ciclos for
row = 3
cols = 3
fig, axes = plt.subplots(row, cols, figsize=(8,5))
for i in range(row):
    for j in range(cols):
        axes[i,j].plot(x,y,'bo-',label="$sin(x)$")
        axes[i,j].set_title('Relacion x-sin(x)')
        axes[i,j].legend()
#se generan un ciclo for para autogenerar gaficas por filas y columnas
fig.tight_layout()
#es una verga autoacomoda las graficas
plt.show()
        
        
        
        
    