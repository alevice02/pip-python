# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:57:28 2023

@author: alevi
"""

text = 'ella sabe programar en Python'
print('python' in text)
# para indicar si una cadena tal cual esta en el texto

size = len(text) #longitud caracteres
print(size)

print(text.upper())
print(text.lower())
print(text.count('a')) #contar caracteres en texto
print(text.swapcase()) #mayusculas a minusculas
 
print(text.startswith('Ella')) #si empieza
print(text.endswith('n'))
print(text.replace('Ella','El'))

print(text.capitalize()) #primera letra en mayuscula
print(text.title()) #primera letra de cada palabra mayus

a = '123'
print(a.isdigit()) #comprobar si el caracter es un digito

print(text[1:3]) #slicing strings
print(text[1:len(text)])
print(text[:3])
print(text[-1]) #primera letra al reves
print(text[:-3])

print(text[1:15:2]) #el tercero es para el salto 

