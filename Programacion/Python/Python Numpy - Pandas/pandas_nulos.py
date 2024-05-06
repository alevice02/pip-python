import pandas as pd 
import numpy as np 

a = {'col1':[1,2,3,np.nan],
 'col2':[4,5,6,np.nan],
 'col3':[np.nan,8,9,None]
 }
b = pd.DataFrame(a)

filtro = b.isnull()*1
#sirve para que los booleanos se vuelvan 0 y 1, es buena practica para trabajarlos mas facil
print(b,filtro)

c = b.fillna(b.mean())
#rellena los valores nulos por el promedio de cada columna
print(c)

d = b.interpolate()
#hacen como una interpolacion dependiendo de los datos
print(d)

e = b.dropna()
#elimineme las filas donde tengo valores nulos
print(e)










