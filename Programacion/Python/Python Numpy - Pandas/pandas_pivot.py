import pandas as pd

bestsellers = pd.read_csv('bestsellers.csv',sep=',',header=0)

print(bestsellers.pivot_table(index='Author',columns='Genre',values='User Rating'))
#genera una tabla con autor como indice, por cada genero y con los valores del rating por autor

print(bestsellers.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum'))
#genera una tabla con genero como indice, por anio, con los valores de la suma de los ratings por genero

print(bestsellers[['Name','Genre']].head(5).melt())
#genera una llave-valor por nombre y genero dentro de la tabla

print(bestsellers.melt(id_vars='Year',value_vars='Genre'))
#genera una tabla de llave-valor aplicando el melt a genero, y anio no cambia, idvars no cambia, valuevars si
#el melt es mas como en caso que tengas multiples entradas en columnas y quieras pasarlo a filas