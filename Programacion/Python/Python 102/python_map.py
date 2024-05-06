num = [1,2,3,4]
num_2 = list(map(lambda i: i+1, num))
#map itera funciones a unos datos
#es un ciclo for para transformar datos sin agregar en una linea
# seria como hacer for i in numbers: 
#                   num_2.append(i+1)
print(num,num_2)

num2 = [2,3,4]
result = list(map(lambda i,j: i +j, num,num2 ))
#en suma de listas se hace del tamanio mas pequenio
print(result)

#map con diccionarios
items = [
    {
        'product':'camisa',
        'price':100
    },
    {
        'product':'pantalon',
        'price':200
    },
    {
        'product':'guante',
        'price':10
    }
]

prices = list(map(lambda i:i['price'],items))
#genera una lista de la llave price en la lista items
#extrae los valores de un diccionario
print(prices)

def taxes(items):
    new_item = items.copy()
    #se hace copia para trabajar con dataset para no alterarlo
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_value = list(map(taxes,items))
#aqui no va lambda porque taxes ya e suna funcion y map itera funciones
#map no cambia el dataset inicial
print(new_value)
print(items)


