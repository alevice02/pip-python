# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:29:50 2023

@author: alevi
"""

counter = 0

while counter < 10:
    counter += 1
    if counter == 5:
        break
    print(counter)
    
#el break es para romper de manera forzada

while counter < 10:
    counter += 1
    if counter == 5:
        continue
    print(counter)
    
#el continue es para que omita los pasos para una condicion dada

for i in range(1,20):
    print(i)
    
#genera iteraciones hasta un numero o en un rango entre numeros

lista = [1,2,3,4,5,5,6]

for i in lista:
    print(i)
    
#recorre cada elemento de la lista

diccionario = {
    'nombre':'Alejo',
    'apellido':'Alejin',
    'lenguajes':['Python','JS'],
    'edad':28
    }

for i in diccionario:
    print(i)
#imprime las llaves
for i in diccionario:
    print(diccionario[i])
#imprime los valores
for i,j in diccionario.items():
    print(i,'-',j)
#pone las llaves y valores como i y j


    




    
    