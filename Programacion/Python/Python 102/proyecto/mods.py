import csv

def read_csv(path):
    with open(path, 'r+') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        #si to printeo esto en un for, es una lista de los valores de la fila
        header = next(reader)
        data = []
#abra el archivo csv con el lector de csv delimitado por comas
#el header seria la primera linea del archivo que lee 
        for i in reader:
            iterable = zip(header,i)
#una lista de tuplas donde se une el header con el valor en cada fila
            country_dict = dict(iterable)
            #esto sirve para que la lista de tuplas se vuelvan diccionarios asociado el header con la fila
            data.append(country_dict)
            #y asi quede una lista de diccionarios
    return data
            
if __name__ == '__main__':
    data = read_csv('./Python 102/proyecto/world_population.csv')
    #print(data)
#solo ejecutará la función si este script es el script principal

#manera mas sencilla de hacer lo de la lista de diccionarios de un csv, el Dict reader los lee como diccionarios de una vez
def read1_csv(path):
    with open(path, 'r+') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        data = []
        for i in reader:
            data.append(i)
    return data

def get_pop(data1):
    dicti = {}
    pais = input("Digite el nombre del pais: ")
    for i in data1:
        if i["Country/Territory"] == pais and len(i["Country/Territory"]) > 0 :
            dicti = {
                "2022": int(i["2022 Population"]),
                "2020": int(i["2020 Population"]),
                "2015": int(i["2015 Population"]),
                "2010": int(i["2010 Population"]),
                "2000": int(i["2000 Population"]),
                "1990": int(i["1990 Population"]),
                "1980": int(i["1980 Population"]),
                "1970": int(i["1970 Population"]),
            }
        labels = list(dicti.keys())
        axes = list(dicti.values())
    return labels, axes
#sirve para extraer poblacion de anios de un pais determinado

def get_pop1(data1):
    labels = []
    axes = []
    prop = input("Digite la propiedad a graficar: ")

    for i in data1:
        if len(i[prop]) > 0 and len(i[prop]) > 0:
            labels.append(i["Country/Territory"])
            try:
                axes.append(int(i[prop]))
            except (ValueError, TypeError):
                # Si la conversión a entero falla, simplemente agrega el valor como está
                axes.append(i[prop])

    return labels, axes
#sirve para extraer poblacion de anios de un pais determinado
            