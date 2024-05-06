import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='dark', palette='muted', font="Verdana", font_scale=1)
#sirve para indicar estilos, paletas, fuentes, tamanio de fuentes
sns.barplot(x=['A','B','C'], y=[1,2,3])
#plotea un grafico de barras mas easy
plt.show()

tips = sns.load_dataset('tips')
#datasets precargados

sns.displot(data=tips, x='total_bill', y='tip', hue='sex', palette='husl')
#dis es distribucion
#genera un grafico que el autoentiende basado en los datos, con x, y y hue que es como el z o el color o las series
sns.displot(data=tips, x='total_bill', hue='sex', kind='hist', palette='dark', alpha= 0.25)
#aqui con un solo eje el sabe que es un histograma
#en kind esta hist, kde(lineas), ecdf(acumulado)
#palette es la paleta
plt.show()