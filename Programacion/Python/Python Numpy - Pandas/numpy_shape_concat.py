import numpy as np 

a = np.random.randint(1,10,(2,3))
print(a,a.shape)
#shape me indica en una tupla cuales son las dimensiones de mi array

b = np.reshape(a,(1,6),'C')
print(b)
#me reconfigura mi array a la nueva forma que le diga mientras sea multiplos igual
#pueden ser C , F o A - es la manera como rearregla si por columnas o por filas 

numeros = np.random.randint(1,20,9)
matriz = numeros.reshape(3,3)

print(matriz, matriz.max(1), matriz.min(1))
#el max = 0 es busca el valor maximo por columna, el max = 1 busca por fila, sin nada busca global, arroja lista
print(matriz.argmax(),matriz.argmin())
#misma logica pero me indica el indice del valor donde esta el primero que encuentre, cuenta el 0 como primer valor

print(matriz.ptp(0))
#varianza la diferencia entre valor max y minimo

c = np.sort(numeros)
print(c)
#ordena los numeros

media = np.mean(c)
mediana = np.median(c)
desv_estandar = np.std(c)
varianza = np.var(c)
print(media, mediana,desv_estandar, varianza)
#funciones estadisticas

concat1 = np.array([[1,2],[3,4]])
concat2 = np.array([5,6],ndmin=2)

concat3 = np.concatenate((concat1,concat2),axis=0)
#permite anadir una lista a la matriz, para eso ambos deben ser matriz y es como unir ambas
concat2_1 = np.reshape(concat2,(2,1))
#esto se hice para poder concatenar en el eje 1
concat3_1 = np.concatenate((concat1,concat2_1),axis=1)
print(concat3,concat3_1)

concat4 = np.concatenate((concat1,concat2.T),axis=1)
#en estos casos para no reshapear, se multiplica por la transpuesta y es el mismo efecto
print(concat4)
                
                   
                








