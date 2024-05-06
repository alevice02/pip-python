import matplotlib.pyplot as plt
import numpy as np

n = 100
m = 1
b = 5

def f(x):
    return m*x + b
#funcion lineal

def f1(x):
    return (2*x**7) - (x**4)+ (3*x**2) + 4
#funcion polinomica

def f2(x):
    return np.tan(x)
#trigonometricas es con np

def f3(x):
    return np.exp(x)
#funcion exponencial

def f4(x):
    return np.log10(x)
#la base es a en a**x y aqui se busca el exponente eso es logaritmo

def h(x):
    return np.where(x <= 0, 0, 1)
#funcion escalonada o seccionada H(x) = {0 , x <= 0 ; 1, x > 0}
#se usa un where con condicion, cuando cumple, cuando no

def f5(x):
    return np.abs(x)
#valor absoluto

x = np.linspace(-10,10,n)
y = f5(x)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()



