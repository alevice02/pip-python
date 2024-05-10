import os
import pyprojroot
import pyhere

cur_dir = os.getcwd()
#mirar la ubicacion de los archivos
data_dir = os.path.join(cur_dir, os.pardir, 'Programacion', 'Python', 'PIP ENV')
#el path.join sirve para unir y generar la ruta, el pardir es decir la carpeta anterior de la que esta
#sirve para generar la ruta sin importar el sistema operativa
os.path.exists(data_dir)
#revisa si existe o si no

'''os.mkdir(os.path.join(data_dir, 'os'))'''
#genera una carpeta con mkdir en la ruta dada

pyprojroot.here('Python').joinpath('PIP ENV')
#acceder a la ruta Python/PIP ENV

pyhere.here().resolve() / 'Python' / 'PIP ENV'
#otra manera de hacer lo mismo
#esto sirve para mirar rutas y abrir archivos que esten en path relativos 

def make_dir (dir_name):
    
    def dir_function(*args):
        return pyprojroot.here().joinpath(dir_name, *args)

    return dir_function
#esta funcion busca automatizar que cada vez que le ponga el nombre del directorio que quiero y las subcarpetas genere la ruta

data_dir1 = make_dir('Programacion')
data_dir1('Python','PIP ENV').exists()
#lo que haces esto es solo poner las carpetas y subcarpetas con comas y archivos como .filename sin escribir el resto



