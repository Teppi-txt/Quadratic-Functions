import matplotlib.pyplot as plt
import sympy
import numpy as np

#setup of graph subplots and size
figure = plt.figure()
axis = figure.add_subplot(1, 1, 1)

#setup of the axis
axis.spines['left'].set_position('center'); axis.spines['bottom'].set_position('zero')
axis.spines['right'].set_color('none'); axis.spines['top'].set_color('none')

#set ticks of graph(axis-based)
axis.xaxis.set_ticks_position('bottom'); axis.yaxis.set_ticks_position('left')

#plotting the graph for the equation
def plot_quad(y_expr):
    #set linespace size for ticks
    x = np.linspace(-10,10,10)
    #set expression
    y = eval(y_expr)

    #plot graph
    plt.plot(x,y, 'r')
    plt.show()
