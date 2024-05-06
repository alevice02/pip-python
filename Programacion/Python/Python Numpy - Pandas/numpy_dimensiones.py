import numpy as np 

scalar = np.array(42)
vector = np.array([1,2,3])
matriz = np.array([[1,2,3],[1,2,3]])
tensor = np.array([[[[[[[[[1,2,3]]]]]]]]])
#el numero de dimensiones se ve con .ndim y pueden ser las que se quiera

print(scalar.ndim, vector.ndim, matriz.ndim,tensor.ndim)

a = np.array([1,2,3],ndmin=10)
#ndim permite definir el numero de dimensiones del inicio
print(a)

a = np.expand_dims(np.array([1,2,3]),axis=0)
#aumenta una dimension mas al array, en eje 0 es en filas y en eje 1 es en columnas
print(a)
a = np.expand_dims(np.array([1,2,3]),axis=1)
print(a)

b = np.squeeze(np.array(a))
#lo lleva al numero de dimensiones donde tiene informacion, elimina vacias
print(b)

c = np.array([1,2,3],ndmin=5)
print(c,c.ndim)
c = np.expand_dims(c,axis=1)
print(c,c.ndim)
c = np.squeeze(c)
print(c,c.ndim)