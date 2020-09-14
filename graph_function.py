import matplotlib.pyplot as plt
import sympy
import numpy as np

figure = plt.figure()
axis = figure.add_subplot(1, 1, 1)

axis.spines['left'].set_position('center'); axis.spines['bottom'].set_position('zero')
axis.spines['right'].set_color('none'); axis.spines['top'].set_color('none')
axis.xaxis.set_ticks_position('bottom'); axis.yaxis.set_ticks_position('left')

def plot_quad(y_expr):
    x = np.linspace(-100,100,100)
    y = x**2 + 5*x + 6
    plt.plot(x,y, 'r')
    plt.show()