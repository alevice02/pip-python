# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:09:04 2023

@author: alevi
"""

diccionario = {
    'nombre':'Alejo',
    'apellido':'Alejin',
    'lenguajes':['Python','JS'],
    'edad':28
    }

print(diccionario.get('nombre'))
#para obtener el valor de la llave escrita
print(diccionario.get('Alejo'))
#None

diccionario['apellido'] = 'Villar'
diccionario['edad'] -= 5
#editar valores en el diccionario
diccionario['lenguajes'].append('Java')
print(diccionario)
del diccionario['apellido'] 

print(diccionario.items())
#me bota la pareja en forma de tupla
print(diccionario.keys())
#bota las llaves en una lista
print(diccionario.values())
#los valores en una lista
