# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from matplotlib import gridspec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    fig = plt.figure()
    fig.suptitle('4 tipo de funciones polinómicas')
    gs = gridspec.GridSpec(2,2)
    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,0])
    ax4 = fig.add_subplot(gs[1,1])

    ax1.plot(y1, color='b', label = 'y1 = x^2', ls = '--')
    ax1.set_facecolor('black')
    ax1.grid('dashed')
    ax1.legend()

    ax2.plot(y2, color='r', label = 'y2 = x**3', ls = '--')
    ax2.set_facecolor('black')
    ax2.grid('solid')
    ax2.legend()

    ax3.plot(y3, color='y', label = 'y3 = x^4', ls = '--')
    ax3.set_facecolor('black')
    ax3.grid('dashed')
    ax3.legend()

    ax4.plot(y4, color='w', label = 'y4 = raiz_cuadrada(X)', ls = '--')
    ax4.set_facecolor('black')
    ax4.grid('solid')
    ax4.legend()

    plt.show()
    














    print("terminamos")
