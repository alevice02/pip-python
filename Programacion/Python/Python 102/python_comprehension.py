numbers = []
for i in range(1,11):
    numbers.append(i*2)

print(numbers)

numbers_2 = [i*2 for i in range(1,11)] 
#sintaxis mas corta para hacer un ciclo donde se generan elementos nuevos, 
#la primera parte es la instruccion y lo demas es el encabezado normal del for
print(numbers_2)

numbers_3 = [i for i in range(1,11) if i%2 == 0] 
#residuo, se puede anadir el if despues del for todo en un renglon
print(numbers_3)

dict = {}
for i in range(1,11):
    dict[i] = i * 2

print(dict)

import random

dict_2 = {i: i for i in range(1,11)} 
#sintaxis para hacerlo con un diccionario en una solo renglon
print(dict_2)

countries = ['col', 'mex', 'bra', 'arg']
population = {}
population = {i: random.randint(1,100) for i in countries}
# en el for se pone countries para que sean valores de la lista no un range porque no son numeros
#random.randint significa que haga numeros aleatorios enteros entre 1 y 100
print(population)

names = ['nico', 'santi', 'vale']
ages = [12,15,18]

print(list(zip(names,ages))) #genera una lista con tuplas adentro de dos listas

children = {i:j for (i,j) in zip(names,ages)} 
#a cada valor de names le asocia una llave de valor de ages leyendo el zip
print(children)



