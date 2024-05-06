# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:11:11 2023

@author: alevi
"""

10 % 2 # el modulo o residuo
10 // 3 #el entero

x = 3.32524656
x = round(x,1) # redondea numeros decimales

not True # es lo opuesto osea false

a = 1
b = 1
if a == b:
    print('oh my god')
else:
    print('oh yeah')
    
numero = int(input('Digita un numero: '))

if numero % 2 == 0:
    print('par')
elif numero > 10:
    print('no aplica')
else: 
    print('impar')
    
opcion = input('escoge piedra, papel o tijera ')
opcion = opcion.lower()
comp = 'piedra'

#if anidados y elif, ejemplo piedra papel o tijera

if opcion == comp:
    print('empate')
elif opcion == 'tijera':
    if comp == 'papel':
        print('ganas')
    else:
        print('pierdes')
elif opcion == 'piedra':
    if comp == 'papel':
        print('ganas')
    else:
        print('pierdes')
elif opcion == 'papel':
    if comp == 'piedra':
        print('ganas')
    else:
        print('pierdes')
        

        

    
    

    
    
    

