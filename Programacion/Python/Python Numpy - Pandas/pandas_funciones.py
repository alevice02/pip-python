import pandas as pd

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)
print(bestsellers.tail(2))
#los ultimos registros
print(bestsellers.info())
#que tipo de datos son en cada columna
print(bestsellers.describe())
#saca estadistica basica de cada columna numerica
print(bestsellers.memory_usage(deep=True))
#uso de memoria de cada parametro

print(bestsellers['Author'].value_counts())
#cuenta valores unicos de la columna

bestsellers = bestsellers._append(bestsellers.iloc[0])
#para agregar al final el valor de la fila 0, asi queda duplicado
bestsellers = bestsellers.drop_duplicates(keep='last')
#borra duplicados, con el keep last dice deje el ultimo en aparecer
print(bestsellers.sort_values('Year',ascending=False).tail(2))
#ordena los valores por ano, ascendente o descendente

print(bestsellers['User Rating'].skew())
#mayores a 0 es positiva quiere decir hacia la derecha, menores a 0 es negativa hacia la izquierda



