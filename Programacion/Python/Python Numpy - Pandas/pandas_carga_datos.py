import pandas as pd 

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)#,names = ['Nombre','Apellido]
#le puedo cambiar el nombre al encabezado con el names
print(bestsellers.columns)

hp_characters = pd.read_json('hpcharactersdataraw.json',typ='Series')
#para leer archivos json

print(bestsellers[0:4])
#print(bestsellers[['Name','Author']])

print(bestsellers.loc[0:4,['Name','Author']])
#filtra del 0 al 4 y solo pone nombre y autor o lo que quiera
print(bestsellers.loc[:,['Reviews']] * -1 )
#filtra en todos la columna reviews y a esa le resta -1 ya que esta afuera de los corchetes

print(bestsellers.iloc[:2,:2])
#filtre hasta la fila 2, pero de columnas hasta la 3, trabaja con indices

print(bestsellers.iloc[1,3] * -1)
#coja el valor de la fila 1 y columna 3 y multipliquelo por -1

