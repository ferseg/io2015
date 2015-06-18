import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from matplotlib.font_manager import FontProperties
from pylab import *


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
ROUND_NUMBER = 2

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
    if intersections != []:
        hull = ConvexHull(intersections)

        font0 = FontProperties()
        font0.set_size('small')
        alignment = {'horizontalalignment':'center', 'verticalalignment':'baseline'}
        text = ""
        varX = 0
        varY = 0
        for i in hull.vertices:
            varX = intersections[i][X_VALUE]
            varY = intersections[i][Y_VALUE]
            region[X_VALUE].append(varX)
            region[Y_VALUE].append(varY)
            text = "(" + str(round(varX,ROUND_NUMBER)) + "," + str(round(varY,ROUND_NUMBER)) + ")"
            plt.text(varX,varY,text,fontproperties=font0,**alignment)
        plt.fill(region[X_VALUE],region[Y_VALUE],REGION_COLOR)

    #view set-up
    plt.xlim(START-abs(axis[X_VALUE])*LEFT_VIEW,abs(axis[X_VALUE])*RIGHT_VIEW)
    plt.ylim(START-abs(axis[Y_VALUE])*LEFT_VIEW,abs(axis[Y_VALUE])*RIGHT_VIEW)
    plt.grid(GRID)
    plt.show()

def change_sign(number):
    return -1*number

