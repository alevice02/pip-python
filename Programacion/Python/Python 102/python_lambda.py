def inc(x):
    return x+1

inc_2 = lambda x : x + 1
#un comprehension para funciones cortas, se pone lambda
#lo que se pide y lo que se retorna
print(inc(10))
print(inc_2(10))

full_name = lambda name,apell: f'Full name es {name.title()} {apell.title()}'
#el modulo title es que la primera va en mayus
nombre = full_name('Alejo','Villar')
#se puede meter el valor de la funcion en una variable 
print(nombre)

def high_order(x,func):
    return x + func(x)
#es una funcion que pide como parametro una funcion y como return tambien
result = high_order(2, inc)
#aqui se usa la funcion inc que suma un valor
# 2 + inc(2) = 2 + 3 = 5
print(result)

high_ord_2 = lambda x,func: x + func(x)
#aqui en lambda
result = high_ord_2(2, lambda x : x + 1)
#la ventaja de lambda es que no hay ni que definir funciones solo ponerlas en lambda y ejecutar
print(result)




