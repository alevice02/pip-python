set_a = {'col','mex','per'}
set_b = {'per','arg','chi'}

set_c = set_a.union(set_b) #unir conjuntos
set_d = set_a.intersection(set_b) #interseccion conjuntos
set_e = set_a.difference(set_b) #A-B
set_f = set_b.difference(set_a) #B-A
set_g = set_a.symmetric_difference(set_b) #AUB-AintB, es decir la suma sin la interseccion
print(set_c,set_d,set_e,set_f,set_g)

