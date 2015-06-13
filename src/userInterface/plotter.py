import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

#Constant definition
GRID = True
LIMIT = 0.1
VIEW = 3
LEFT_VIEW = 0.1
RIGHT_VIEW = 1.1
X_VALUE = 0
Y_VALUE = 1
Z_VALUE = 3
START = 0
DOTS_SIZE = 10
DOTS_CONFIG = "go"
LINE_COLOR = "k"
LINE_STYLE = "dashed"
REGION_COLOR = "blue"
TITLE = "Graficador"

def plot_graph(inequalities,intersections,axis):
    """
    
    :param inequalities: list with inequalities.
    :param intersections: list with intersections of the inecualities.
    :param axis: list containing the maximum values of the intersections
    on the inequalities and the X and Y axis. Format: [maxX,maxY].

    """
    plt.title(TITLE)
    plt.axhline(y=START,color=LINE_COLOR)
    plt.axvline(x=START,color=LINE_COLOR)
    x = np.arange(change_sign(VIEW*max(axis)),VIEW*max(axis),LIMIT)
    
    #plotting inequalities
    for i in inequalities:
        try:#plots functions
            plt.plot(x,eval(i),color=LINE_COLOR,linestyle=LINE_STYLE)
        except:#draws vertical lines
            plt.axvline(x=int(eval(i)),color=LINE_COLOR,linestyle=LINE_STYLE)

    #draws intersections
    for i in intersections:
        plt.plot(i[X_VALUE],i[Y_VALUE],DOTS_CONFIG,markersize=DOTS_SIZE)

    #paints feasible region
    region = [[],[]]
    hull = ConvexHull(intersections)
    for i in hull.vertices:
        region[X_VALUE].append(intersections[i][X_VALUE])
        region[Y_VALUE].append(intersections[i][Y_VALUE])
    plt.fill(region[X_VALUE],region[Y_VALUE],REGION_COLOR)

    #view set-up
    plt.xlim(START-abs(axis[X_VALUE])*LEFT_VIEW,abs(axis[X_VALUE])*RIGHT_VIEW)
    plt.ylim(START-abs(axis[Y_VALUE])*LEFT_VIEW,abs(axis[Y_VALUE])*RIGHT_VIEW)
    plt.grid(GRID)
    plt.show()

def change_sign(number):
    return -1*number

def matrix_to_inequation(matrix):
    inequations = []
    for element in matrix:
        if element[X_VALUE] == 0:
            inequations += ["x*0+"+str(element[Z_VALUE]/element[Y_VALUE])]
        elif element[Y_VALUE] == 0:
            inequations += [str(element[Z_VALUE]/element[X_VALUE])]
    print(inequations)

