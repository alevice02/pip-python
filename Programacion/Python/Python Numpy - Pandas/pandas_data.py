import pandas as pd
import numpy as np

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)
print(bestsellers.head(2))

print(bestsellers.drop('Genre',axis=1).head(2))
#funcion drop borra una columna o fila, en este caso del encabezado de 2, pero de la salida no del dato original

besti = bestsellers.copy()
print(besti.drop('Genre',axis=1,inplace=True))
#aqui en besti si se borro completamente del archivo
besti = besti.drop('Price',axis=1)
#es la misma manera de borrar archivo reemplazandolo en la misma variable
print(besti.head(2))

print(bestsellers.drop(range(0,10),axis=0).head(2))
#borreme en un rango en una lista de indices

index_author = besti[besti['Author']=='Steve Harvey'].index
#sirve para encontrar el indice donde el autor es Steve Harvey
besti.drop(index_author,axis=0,inplace=True)
#borra la fila donde estaba el autor 

besti['Nueva Columna'] = np.nan
#agrega una nueva columna y los valores son Nan o sea nulos
print(besti.shape[0])
#me indica la cantidad de filas

data = np.arange(0,besti.shape[0])
#metame en data una lista que vaya de 0 a la cantidad de filas 
besti['Range'] = data
#genereme una columna y llenemela de los valores de la lista
print(besti.head(2))





