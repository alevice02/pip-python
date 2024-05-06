import pandas as pd 

psg_players = pd.Series(['Navas','Ney','Leo','Mbappe'], index=[1,10,30,7])
#es una manera mas facil de trabajar con diccionarios ya que esto es lo mismo

print(psg_players[10])
#aqui el no muestra por posicion en el diccionario sino por index

psg_dict = {'Jugador':['Navas','Ney','Leo','Mbappe'],
            'Goles':[0,300,500,200],
            'Salario':[5,30,40,25]}

psg_df = pd.DataFrame(psg_dict,index = [1,10,30,7])
#genera un data frame quiere decir hacer una tabla a partir de un diccionario, el index es el id es opcional
print(psg_df)

print(psg_df.columns,psg_df.index)
#imprime las columnas y las filas, los encabezados


