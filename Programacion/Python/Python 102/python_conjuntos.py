set_countries = {'col', 'mex', 'arg', 1, True} #conjuntos, diferente a un diccionario, no acepta elementos duplicados los omite
print(set_countries)
print(type(set_countries))

set_string = set('hola') #solo con strings me genera un conjunto con cada letra como elemento individual
print(set_string)

set_tuples = set(('abc',123,'lo que es')) #genera un conjunto con los elementos de una tupla
print(set_tuples)

set_listas = set([1,2,3,4,5,1,2,3,6,5,4,6]) #genera un conjunto a partir de una lista con solo valores unicow
unicos = list(set_listas) #los vuelve lista
print(unicos)

print('col' in set_countries) #si esta dentro del conjunto

set_countries.add('per') #anadir al conjunto cierto valor
set_countries.update({'bra','chi','per'}) #anadir varios valores al conjunto
set_countries.discard(1) #mejor que remove para eliminar elementos del conjunto
print(set_countries)

set_countries.clear() #resetear el conjunto





