import pandas as pd 
import numpy as np 

df1 = pd.DataFrame({'a':['a1','a2','a3'],
 'b':['b1','b2','b3'],
 'c':['c1','c2','c3'],
 'd':['d1','d2','d3']})

df2 = pd.DataFrame({'a':['a4','a5','a6'],
 'b':['b4','b5','b6'],
 'c':['c4','c5','c6'],
 'd':['d4','d5','d6']})

print(pd.concat([df1,df2],ignore_index=True))
#concatena los dos data frames y pone los index consecutivos

izq = pd.DataFrame({'a':['a1','a2','a3'],
 'b':['b1','b2','b3'],
 'c':['c1','c2','c3']})

der = pd.DataFrame({'a':['a1','a2','a3'],
 'd':['d1','d2','d3'],
 'e':['e1','e2','e3']})

print(izq)
print(der)
print(izq.merge(der,on= 'a'))
#left join pega lo de la derecha en la izquierda,teniendo como base comun el a
print(der.merge(izq))
#right join pega lo de la izquierda en la derecha, teniendo como base comune el a

izq = pd.DataFrame({'a':['a1','a2','a3'],
 'b':['b1','b2','b3'],
 'c':['c1','c2','c3']})

der = pd.DataFrame({'az':['a1','a2','a3'],
 'd':['d1','d2','d3'],
 'e':['e1','e2','e3']})

print(izq.merge(der,left_on='a',right_on='az'))
#cuando la columna en comun no tiene el mismo nombre hay que especificar

izq = pd.DataFrame({'a':['a1','a2','a3'],
 'b':['b1','b2','b3'],
 'c':['c1','c2','c3']})

der = pd.DataFrame({'az':['a1','a2','a4'],
 'd':['d1',np.nan,'d3'],
 'e':['e1','e2','e3']})

print(izq.merge(der,left_on='a',right_on='az',how='left'))
#cuando tengo valores nulos o valores no coincidentes en la columna en comun, con el how me dice que tipo de join en este caso left
join_i = pd.DataFrame({'a':['a1','a2','a3'],
 'b':['b1','b2','b3']},index=['k1','k2','k3'])

join_d = pd.DataFrame({'c':['c1','c2','c3'],
 'd':['d1','d2','d3']},index=['k0','k2','k3'])

print(join_i.join(join_d,how='inner'))
#lo mismo que el merge pero con menos parametros





