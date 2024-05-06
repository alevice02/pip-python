import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

markers={'Lunch':'X', 'Dinner':'o'}
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day',style='time', size='size', markers=markers)
#diagramas de dispersion
plt.legend(loc='center', bbox_to_anchor=(1.12,0.5))
plt.tight_layout()
plt.show()

sns.lineplot(data=tips, x='total_bill', y='tip', hue='day',style='time', size='size', markers=markers)
#diagramas de dispersion de lineas
plt.legend(loc='center', bbox_to_anchor=(1.12,0.5))
plt.tight_layout()
plt.show()

sns.relplot(data=tips, x='total_bill', y='tip', hue='day',style='time', size='size', markers=markers, col='time')
#se adapta al que mejor represente
plt.show()

