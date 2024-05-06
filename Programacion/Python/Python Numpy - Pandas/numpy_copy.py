import numpy as np 

a = np.arange(0,11)
b = a[0:6]
b[:] = 0 
#esta funcion dice que coja todos los valores de la lista y reemplazelos por 0

print(a,b)
#aqui a se ve afectada porque b usa informacion de a, es por esto que se debe hacer una copia para no danar el archivo original

a = np.arange(0,11)
b = np.copy(a[0:6])
b[:] = 0

print(a,b)
#esta es la diferencia ahora b es la que se afecta ya que a no es la misma referencia

c = np.linspace(1,10,10,dtype='int8')
#la mejor manera de hacer una lista del 1 al 10, porque linspace les pone un . al final entonces es mejor decir que sea int8
indices_cond = c>5
#me genera un array con un bool diciendo si se cumple o no la condicion
print(c[(c>5) & (c<9)], c[indices_cond == False]) 
#se puede hacer el filtro desde el array solo poniendo la condicion como slicing....brain exploted

matriz1 = np.arange(1,11)
matriz2 = np.arange(11,21)
concat_list = np.concatenate((matriz1,matriz2))
#me genera una sola lista con ambas
concat_mat = np.vstack((matriz1,matriz2))
#me genera una matriz de listas stackadas verticalmente
filtro = concat_mat[concat_mat % 2 == 0]
#hacer un filtro de valores pares en la matriz
print(concat_list, concat_mat,filtro)

unitaria = np.where(concat_mat % 2 == 0, 1, 0)
#genereme una matriz donde (condicion, cumple, no cumple)
print(unitaria)





