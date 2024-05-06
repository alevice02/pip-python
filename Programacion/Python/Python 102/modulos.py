import sys
#print(sys.path)
#donde estamos ubicados

import re
text = ' Mi numero es 123, el codigo es 57, lo que sea 23'
result = re.findall('[0-9]+',text)
#extension re de reference, y findall es para encontrar caracteres de numeros en el texto
print(result)

import time
local = time.localtime()
time = time.asctime(local)
#para mostar la hora y fecha actuales
print(time)

import collections
num = [1,1,1,1,3,3,3,5,5,5,4,8,2]
counter = collections.Counter(num)
#en mayus, es un modulo para frecuencias absolutas de una serie de numeros
print(counter)
