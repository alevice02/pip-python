import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

#sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', kind='hist', marginal_ticks=True, 
              #marginal_kws= dict(bins=15, multiple='dodge'))
#es un diagrama de dispersion y a los lados tiene histogramas
#el marginal ticks son los ejes de los histogramas la label
#el marginal kws es para hablar de los histogramas como el multiple o las bins
#plt.show()

#sns.pairplot(data=tips, hue='sex', palette='dark')
#es un scatter matrix compuesto que es el que se usaba para los litotipos entre variables numericas
#el corner=True es para mostrar los valores de la diagonal inferior
#plt.show()

print(tips.corr(numeric_only=True))
#saca la tabla de correlacion entre variables

sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=5, linecolor='black',
            vmin=0.5, vmax=1)
plt.show()
#genera un mapa de calor basado en los datos
#annots son las labels, cmap es el tema o paleta
#linewidth pone separado en la rejilla, line color el color del separado 
#vmin y max es para la leyenda del color