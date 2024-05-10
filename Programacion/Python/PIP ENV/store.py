import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)       
    #esta funcion trae la informacion de esa pagina y muestra stauts code y text
    categories = r.json() # convierte el string en un json que puede leer pytthon como lista de diccionarios
    for i in categories:
        print(i['name'])
    #genera la lista de nombres de las categorias

'''
#script para ambientes virtuales 
python3 -m venv env
source env/bin/activate
pip3 freeze > requirements.txt
'''