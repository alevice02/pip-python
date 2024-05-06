file = open('./Python 102/texto.txt')
print(file.read())
#abrir un archivo de texto, cvs, tipo de lectura completo
print(file.readline())
#lees el archivo linea por linea

for i in file:
    print(i)
    
#leerlo todo con menos memoria ya que es linea por linea
file.close()
#cerrar el archivo para liberar memoria

#los permisos pueden ser de r = read, w = write sobre 0, 
# r+ = ambos sin cambiarlo, w+ = write desde 0 sobreescribe

#la manera correcta de abrirlo y leerlo es:
with open('./Python 102/texto.txt','r+') as file:
    for i in file:
        print(i)     
#aqui lo abre, lo lee y lo cierra de una, pero lo lee 
#por lineas entonces el formato cambia a interlineado mayor
    file.write('\nnuevas cosas en este archivo\n')
    file.write('vamos a probar si sirve\n')
#se escriben cosas en este archivo , el \n es para saltar linea
#se pone al comienzo o al final donde se necesite


    
        




