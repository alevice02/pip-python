import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
#lista de 11 numeros del 0 al 5
y = x**2

plt.plot(x,y,'bo')
plt.show()
#plotea x contra y, r es rojo y o o x es el icono

plt.hist(x,bins=10)
plt.show()
#histograma, bins la cantidad de bloques o separaciones

plt.pie(x)
plt.show()
#diagrama de torta

plt.scatter(x,y)
plt.show()
#diagrama de dispersion

plt.boxplot(x)
plt.show()
#diagrama de cajas y bigotes

plt.bar(x,y)
plt.show()
#diagrma de barras y el otro es la altura

'''
character	description
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
'8'	octagon marker
's'	square marker
'p'	pentagon marker
'P'	plus (filled) marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'X'	x (filled) marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker
Line Styles
character	description
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style
Colors
character	color
'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white
'''




