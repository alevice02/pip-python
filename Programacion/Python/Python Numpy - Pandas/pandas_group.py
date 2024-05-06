import pandas as pd 

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)
print(bestsellers.head(2))

print(bestsellers.groupby('Author').count())
#agrupados por autor cuenteme los valores en las columnas

print(bestsellers.groupby('Author').sum().loc['William Davis'])
#agrupados por autor sumeme los valores de las columnas que tengan a William Davis

print(bestsellers.groupby(['Author','Genre']).agg({'Reviews':['min','max'],'User Rating':'mean','Year':'max'}))
#agrupelos por autor y genero, muestreme los reviews min y maximos, y la suma de los user rating, y el anio mayor




