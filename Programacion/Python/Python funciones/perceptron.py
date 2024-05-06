import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.2, 2, 3.2, 2.5, 5, 6, 4, 8])
y = np.array([2, 3, 3.4, 3.1, 4, 4.7, 3.8, 7])

coefficients = np.polyfit(x,y,1)
#genera pendiente e intercepto con una funcion llamada polyfit 
m, b =  coefficients

def f(x):
    return m * x + b

y_calc = f(x)
#renombrar para evitar errores

error = np.sum((y-y_calc)**2)
#calcular el error cuadratico
cov = np.cov(x,y)
#calcular covarianza es que es obtener varianza de ambos datasets
variance_X = cov[0, 0]
variance_y = cov[1, 1]
#varianza para cada variable

fig, ax = plt.subplots()
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
ax.plot(x, y_calc, 'b', label='f(x)')
ax.scatter(x, y, color='red', label='Puntos dados')
ax.legend()
plt.show()
print(error, variance_X, variance_y)
#si el error es mucho mas bajo que la varianza esta bien


