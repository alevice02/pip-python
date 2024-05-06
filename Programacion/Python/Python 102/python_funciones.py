def firma(text):
    return print('Firmado por '+text)

firma('AV')

def sumatoria(min,max):
    sum = 0
    for i in range(min, max):
        sum += i
    print(sum)
    return sum
#funcion que suma los numeros dentro de un rango dado,
#recordar siempre poner return al final por buenas practicas

result = sumatoria(1,100)
result2 = sumatoria(result,result+10)

def find_volume(length=1, width=1, depth=1):
    #se pueden poner valores por defecto
    volume = length * width * depth
    return (volume,width)

print(find_volume(width=10)) 
#al haber valores por defecto se puede solo poner uno
print(find_volume(1,2,3))


