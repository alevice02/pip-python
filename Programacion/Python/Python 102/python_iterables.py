for i in range(1,11):
    print(i)
#ese es un for que itera tradicional, de forma manual seria>

itera = iter(range(1,11))
print(next(itera))   
print(next(itera)) 
print(next(itera)) 
#ese es el funcionamiento del for internamente, 
# se define el rango e itera elemento por elemento con next 

suma = lambda x,y: x + y
assert suma(2,2) == 4
#el assert se usa para verificar si una funcion 
# da un resultado esperado si no bota error 

age = 10
if age < 18:
    raise Exception('No se permite la entrada a menores')
#se pueden generar errores a proposito con raise exception
#supongo que es mas para desarrollo web

try:
    print(0/0)
    age = 10
    if age < 18:
        raise Exception('No se permite la entrada a menores')
except Exception as error:
    print('No se permita la entrada  a menores')
except ZeroDivisionError as error:
    print('No se puede dividir por 0')
    
#sirve para capturar errores y que no se pare el programa
        

    
