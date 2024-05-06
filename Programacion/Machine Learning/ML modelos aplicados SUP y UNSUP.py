import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from sklearn.metrics import confusion_matrix

plt.rcParams['font.size']=15

iris = datasets.load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
target = pd.DataFrame(data=iris.target, columns=['species'])
data = pd.concat([data, target], axis=1)
#une los valores de las propiedades con el nombre de la especie, que estaba en otra tabla 

data = data.sample(frac=1, random_state=1234)
#obtener una muestra del dataset

#REGRESION LINEAL
#definir datos de entrenamiento y datos de testing, generalmente 80/20
ntraining = int(data.shape[0] * 0.8)
#divide los datos con el iloc basado en el ntraining que es el 80%
training = data.iloc[:ntraining, :]
testing = data.iloc[ntraining:, :]

#escogemos las variables para el modelo
plength = data['petal length (cm)']
pwidth = data['petal width (cm)']

'''fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1)
sns.scatterplot(data=data, x=plength, y=pwidth)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
ax.set_title('Petal Width v. Length')
fig.tight_layout()
plt.show()'''
#esto muestra una relacion lineal, por tanto se puede hacer un modelo de regresion lineal

model1 = linear_model.LinearRegression()
model1.fit(pd.DataFrame(training.iloc[:, 2]), training.iloc[:, 3])
#ajustamos el modelo a la columna 2 y 3 que son los length y width
print(model1.coef_, model1.intercept_)
#coef es la m = 0.41 y intercept es la b = -0.36

xvals = np.arange(plength.min(), plength.max()+1, 0.5)
#un arreglo del valor minimo al maxumo de plength
yvals = 0.41 * xvals - 0.36
#ecuacion de la recta

'''fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1)
sns.scatterplot(data=data, x=plength, y=pwidth)
ax.plot(xvals, yvals, 'k', linewidth =3)
#esta es la linea de la recta
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
ax.set_title('Petal Width v. Length')
fig.tight_layout()
plt.show()'''
#muestra un buen ajuste

#calculemos ahora el rendimiento con MSE y r2, primero hagamos la prediccion con el modelo basado en los datos de la variable x dada 
ypredict = model1.predict(pd.DataFrame(testing.iloc[:, 2]))
MSE = mean_squared_error(pd.DataFrame(testing.iloc[:, 3]), ypredict) #compara yreal con ypredict
R2 = r2_score(pd.DataFrame(testing.iloc[:, 3]), ypredict) #lo mismo con r2
'''print(MSE, R2)'''
#MSE = 0.04, R2 = 0.94, buena correlacion, ya tendriamos el modelo de regresion lineal

#ahora para predecir un valor de pwidth basado en un plength
plength_p = 6.0
pwidth_p = model1.predict([[plength_p]])
'''print(pwidth_p[0])'''


#REGRESION LOGISTICA
#vamos a dar datos de entrenamiento y test y la etiqueta
xtrain = training.iloc[:, :-1]#la ultima columna es especie, todo lo demas excepto esa
ytrain = training.iloc[:, -1]#la especie es la etiqueta de entrenamiento
xtest = testing.iloc[:, :-1]
ytest = testing.iloc[:, -1]

#modelo de regresion logistica para clasificar la especie
model2 = linear_model.LogisticRegression()
model2.fit(xtrain, ytrain)

#vamos a testear el modelo
ypred = model2.predict(xtest)
#calculamos la accuracy
accuracy_score(ytest, ypred)
#fue de 1.0 quiere decir que tuvo una eficacia del 100%

#aplicamos una matriz de confusion
confusion_matrix(ytest, ypred)
#como vemos la diagonal principal tienen todos los valores correctos y no hay datos en otra parte de la matriz


#RANDOM FOREST O DECISION TREE
#aplicamos el modelo de random forest
clf =RandomForestClassifier(n_estimators=3)
clf.fit(xtrain, ytrain)
#predecimos el valor
y_pred = clf.predict(xtest)
accuracy_score(ytest, y_pred)
#igual da 1 entonces bien


#KMEANS CLUSTERING
#aplicamos el modelo 
k2model = KMeans(n_clusters=2, random_state=42)
k2model.fit(data[['petal length (cm)', 'petal width (cm)']])
#calculamos inertia y centroides
inertia = k2model.inertia_
centroids = k2model.cluster_centers_
#coordenadas x y y de ambos

fig = plt.figure(figsize=(5,5))
ax=fig.add_subplot(1,1,1)
sns.scatterplot(data=data[data['species'] == 0], x='petal length (cm)', y='petal width (cm)', color='green', ax=ax)
sns.scatterplot(data=data[data['species'] == 1], x='petal length (cm)', y='petal width (cm)', color='blue', ax=ax)
sns.scatterplot(data=data[data['species'] == 2], x='petal length (cm)', y='petal width (cm)', color='red', ax=ax)
ax.plot(centroids[0], centroids[1], 'ko', markersize=20)
ax.legend(['setosa','versicolor', 'virginica'])
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
ax.set_title('Petal Length v. Width')
plt.tight_layout()
plt.show()









