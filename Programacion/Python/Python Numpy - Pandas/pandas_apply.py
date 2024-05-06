import pandas as pd
import numpy as np

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)
print(bestsellers.head(2))

print(bestsellers['User Rating'].apply(lambda x:x*2).head(5))
#apply sirve para aplicar una funcion a las columnas

print(bestsellers.apply(lambda x: x['User Rating'] *2 if x['Genre'] == 'Fiction' else x['User Rating'],axis=1))
#multiplique por 2 el user rating si es genero de fiction sino dejelo igual, apliquelo en las columnas con el axis 1


