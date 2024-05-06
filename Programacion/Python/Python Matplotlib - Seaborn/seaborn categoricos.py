import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.countplot(data=tips, x='day', hue='sex')
#graficos de barras para variables categoricas
plt.show()

sns.stripplot(data=tips, x='day', y='total_bill', dodge=True, hue='sex')
#es como un diagrama de dispersion pero hacia la vertical por categoria
plt.show()

sns.swarmplot(data=tips, x='day', y='total_bill', dodge=True, hue='sex')
#es como un diagrama de dispersion pero hacia la vertical por categoria
plt.show()

sns.boxplot(data=tips, x='day', y='total_bill', dodge=True, hue='sex')
sns.swarmplot(data=tips, x='day', y='total_bill', dodge=True, hue='sex')
#la mezcla entre estos stripplots con el boxplot se ven chimbas
plt.show()

sns.violinplot(data=tips, x='day', y='total_bill',split=True, hue='sex')
# es como el boxplot pero alargado como un violin y donde esta la barriga es donde hay mas datos
#el split los une para que se puedan comparar no al lado del otro sino como medio
plt.show()

sns.catplot(data=tips, x='day', y='total_bill', hue='sex', col='time')
#es como el displot el elige automatico cual es el que mas se ajusta pero se puede editar con kind
#col es para mostar dos graficos filtrados por la variable
plt.show()

