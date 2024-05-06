print('hola mundo')

my_name = 'Alejandro'
print(my_name)

print('Me llamo',my_name)

my_name = input('Cual es tu nombre? ') # propiedad input y lo que sea que este es tipo string
print('Hola',my_name,'que se dice') #la coma deja espacio entre variables

print(type(my_name)) #definir el tipo de variable

single = False
print('Hola',my_name,'eres',single)

name = 'Alejo'
surname = 'Duran'
full = 'mi nombre es '+name + ' y mi apellido es ' +surname
print(full)

template = 'Hola a todos, {} de los {} de Malta'.format(full, surname)
print(template)
# el format sirve resto para no poner los + sino dejar el espacio y el entiende en el orden en el que es puesto

template = f'Hola, mi nombre es {name} y mi apellido es {surname}, de los {surname} de Malta'
print(template)
# formato correcto de los format

a = 1
b = 1
b += 1
print(a,b)

enero = int(input('Presupuesto de enero'))
febrero = int(input('Presupuesto de febrero'))
marzo = int(input('Presupuesto de marzo'))
# se puede cambiar el tipo de dato de forma dinamica poniendo atras el tipo esperado
promedio = (enero + febrero + marzo) / 3
print('El promedio es',promedio)

edad = input('Escribe tu edad')
print(f'Tu edad en 10 anios sera {int(edad)+10}')
#el formato es dinamico, lo que esta entre corchetes se puede editar normal y lo lee segun todo

print('Hola'*3) #multiplicador de strings




