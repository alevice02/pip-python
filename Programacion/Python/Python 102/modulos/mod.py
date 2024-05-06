def get_pop():
    keys = ['col','arg']
    values = [100,200]
    return keys,values

A = 'hola'

def pop_by_country(data,country):
    result = list(filter(lambda i:i['Country'] == country, data))
    return result
#hace un filtro para el valor de pais que corresponda al 
# pedido