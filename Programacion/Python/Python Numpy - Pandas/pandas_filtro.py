import pandas as pd 

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)
print(bestsellers.head(2))

print(bestsellers[bestsellers['Year'] > 2016].head(5))
#imprime el filtro ya hecho en la condicion

bestsellers['Genre'] == 'Fiction'
print(bestsellers[(bestsellers['Genre'] == 'Fiction') & (bestsellers['Year'] > 2016)].head(5))
#realiza dos filtros con el & 

mayor = bestsellers['Year'] > 2016
ficcion = bestsellers['Genre'] == 'Fiction'

print(bestsellers[~mayor & ficcion].head(5))
#el simbolo ~ sirve para negar la condicion

print(bestsellers[bestsellers['Author'].str.contains('Martin')].head(5))
#filtra una columna de texto que contenga tal palabra