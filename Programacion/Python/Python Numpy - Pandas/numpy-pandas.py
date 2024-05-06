import numpy as np 
#import pandas as pd 

a = np.array ([0,1,2,3],dtype='int64')
#sirve para guardar arrays o sea listas o matrices
 
matriz = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(matriz)

print(a[::2],b[1,1])

a = np.array (['0','1','2','3'])

a = a.astype(np.int64)
#cambia el tipo de dato a float 64 o straing_, bool_, int64

c = np.arange(0,10)
#crea una lista del rango entre 0 al 10-1 

print(a, a.dtype,c)