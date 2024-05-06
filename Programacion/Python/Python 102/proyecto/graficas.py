import matplotlib.pyplot as plt


def bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

#se genera una grafica de barras con eje, 
#donde los ejes tienen labels en x y values en y

def pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels =labels)
    #este tiene sintaxis opuesta a las barras
    ax.axis('equal')
    plt.show()

if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [1, 2, 3]
    bar_chart(labels, values)
    pie_chart(labels, values)
