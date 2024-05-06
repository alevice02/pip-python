import numpy as np 

lista = np.arange(0,10,2)
#inicial, final, step
print(lista)

ceros = np.zeros((10,10))
#genera una matriz de ceros para habilitar uso de memoria
print(ceros)

unos = np.ones((10,10))
print(unos)

equidistantes = np.linspace(0,10,100)
#inicial, final, rango. Esto genera una lista de espacios iguales entre el rango de numeros basado en el step
print(equidistantes)

unitaria = np.eye(4)
#matriz unitaria de 4x4
print(unitaria)

aleatorio = np.random.rand(4,4)
#se crea lista de 4 numeros o matriz de 4 x 4 entre aleatorios entre 1 y 0
print(aleatorio)

alea_enteros = np.random.randint(1,10,(10,10))
#inicial, final, cant y disposicion de datos = uno seria lista con coma seria matriz y cantidad (enteros random)
print(alea_enteros)

