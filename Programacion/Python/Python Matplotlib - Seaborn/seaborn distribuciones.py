import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.histplot(data=tips, x='tip', hue='sex', stat='frequency', multiple='stack')
#genera un histograma
#stat me habla del eje y, si me muestra count, frequency, probability, percent
#multiple es la visualizacion de las barras, stack es las series del hue que todas se ven, layer es una detras de otra,
#dodge es una al lado de la otra
plt.show()

sns.kdeplot(data=tips, x='tip', hue='sex', cumulative=False, shade=True, bw_adjust=1)
#diagrama de densidad o de lineas
#cumulative=True es que hace un diagrama acumulado
#shade muestra la sombra de la curva debajo
#bw_adjust ajusta automatico los ejes
plt.show()

