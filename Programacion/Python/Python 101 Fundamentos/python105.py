# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:31:44 2023

@author: alevi
"""
import random

tupla = (1,2,3,4)
print(tupla.index(2))
print(tupla.count(1))

lista = list(tupla)
#generar una copia en lista de la tupla

#piedra papel o tijera
opciones = ('piedra','papel','tijera')
rounds = 1
comp_wins = 0
user_wins = 0
fin = False

while fin==False:
    print('*'*10)
    print('Round',rounds)
    print('*'*10)
    print(comp_wins, user_wins)
    
    opcion = input('escoge piedra, papel o tijera ')
    opcion = opcion.lower()
    comp = random.choice(opciones)
    #genera opcion random de la tupla
    print(comp)
    if not opcion in opciones:
        print('la opcion no es valida')
        continue
    else:    
        if opcion == comp:
            print('empate')
        elif opcion == 'tijera':
            if comp == 'papel':
                print('ganas')
                user_wins +=1
            else:
                print('pierdes')
                comp_wins +=1
        elif opcion == 'piedra':
            if comp == 'papel':
                print('ganas')
                user_wins +=1
            else:
                print('pierdes')
                comp_wins +=1
        elif opcion == 'papel':
            if comp == 'piedra':
                print('ganas')
                user_wins +=1
            else:
                print('pierdes')
                comp_wins +=1
                
    if comp_wins == 2:
        print('gana comp')
        fin = True
        
    if user_wins == 2:
        print('gana user')
        fin = True
    rounds +=1
    