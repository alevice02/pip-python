import csv
import mods
import graficas

data1 = mods.read1_csv("./Python 102/proyecto/world_population.csv")
#leer data
data1 = list(filter(lambda x: x['Continent'] == 'South America',data1))
#filtro por lo que quiera

labels, valores = mods.get_pop1(data1)
print(labels,valores)
#obtener labels and values

graficas.bar_chart(labels,valores)
#graficar

graficas.pie_chart(labels,valores)


