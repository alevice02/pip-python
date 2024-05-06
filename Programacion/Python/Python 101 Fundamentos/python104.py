# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:31:23 2023

@author: alevi
"""

numeros = [1,2,3,4]
tasks = ['make a dishes', 'play']
todo = [1, True, 'hola']

print(numeros[1])

print(True in todo)
#mirar si esta en algun componente de la lista

numeros.append(5) 
#al final
numeros.insert(0,'hola')
#agrega en la posicion pero no reemplaza

new = numeros + tasks
#une listas
print(new)

index = new.index(1)
new[index] = 1/2
#pone el index de donde encuentra el valor

new.remove(0.5)
#remueve el primer elemento que coincida

new.pop()#elimina el ultimo elemento
new.pop(3)#elimina el indice 

new.reverse()#invertir el orden
numeros = [1,2,3,4]
numeros.sort()
