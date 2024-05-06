import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Programacion\Machine Learning\diabetes.csv")
data.dtypes
data.shape
#filas x columnas
data = data.dropna()

# Ajustar el tamaño de fuente.
plt.rcParams['font.size'] = 15 
f = plt.figure(figsize=(8,4))
ax = f.add_subplot(1,1,1)
# Gráfica tus datos usando 'hist'. Pasa el objeto 'ax' a Pandas. Agrega un borde negro con un groso de 2.
sns.histplot(data=data, x='Outcome')
# Establece los límites en el eje x.
ax.set_xlim([-0.5, 1.5])
# Establece la frecuencia de tick. Tenemos 0 y 1 que corresponden a Sí y No respectivamente.
ax.set_xticks([0, 1])
ax.set_xticklabels(["N", "Y"])
ax.set_title("Diabetes Y/N?")
ax.set_xlabel("Answer")
ax.set_ylabel("Count")
ax.set_ylim([0, 510])
# Mace que las cosas sean bonitas, no es necesario, pero se ajusta al tamaño de la figura.
f.tight_layout()
plt.show()

binvalues = [20, 25, 30, 35, 40, 85]
plt.rcParams['font.size'] = 15 
f = plt.figure(figsize=(8,4))
ax = f.add_subplot(1,1,1)
sns.histplot(data=data, x='Age', bins = binvalues)
ax.set_title("Age range of patients")
ax.set_ylim([0, 510])
ax.set_xlabel("Age")
ax.set_ylabel("Count")
f.tight_layout()
plt.show()