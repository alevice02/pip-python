import random

countries = ['col', 'mex', 'bra', 'arg']

population_2 = {i:random.randint(1,100) for i in countries}
print(population_2)

result = {i:j for (i,j) in population_2.items() if j >50}
#escoge un i y un j que serian llave y valor que toma del diccionario population
#ya que la opcion items() le hace tomar ambos valores y usarlos como i y j, adicional le aplica el condicional
print(result)

text = 'Hola Soy nico'
unique = {i:text.count(i) for i in text if i in 'aeiou'}
#toma el texto y cada caracter busca cuantas veces esta en el texto y mete la vocal con la frencuencia como llave
print(unique)

# lista = mutable, ordenada, slicing, duplicar
# tupla = lista no mutable
# conjunto(set) = mutable pero no ordenado ni slicing ni duplicado

