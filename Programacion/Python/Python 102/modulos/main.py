import mod

keys, values = mod.get_pop()
#se pueden importar modulos hechos en otro script con el nombre del script
print(keys,values)

print(mod.A)
#cualquier archivo en python es un modulo, hasta variables4

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country':'Argentina',
        'Population':400
    }
]

pop = mod.pop_by_country(data,input('Que pais desea buscar: '))
print(pop)
#usa la funcion de mostrar poblacion de pais dado, en este caso por un input dado


