import numpy as np 

a = np.arange(0,20,2)     
b = 1/a
c = a**2
d = a + c
print(b,c,d)

ma = a.reshape(2,5)
#manera facil de generar una matriz a partir de un array
mb = ma*2
mc = ma + mb
prod_punto = np.matmul(ma,mb.T)
#producto punto siempre se resuelve con la transpuesta
prod_punto1 = ma @ mb.T
#misma operacion de arriba mas easy

print(ma,mb,mc,prod_punto,prod_punto1)

req = [1,2,3,4,2,5,2,5,6,9,3,2,4,1,5,8,7,5,1,2,4]
req1 = np.unique(req)
#busca valores unicos
print(req1)