import numpy as np
import matplotlib.pyplot as plt


#Constant definition
LIMIT=0.1
LEFT_VIEW=0.1
RIGHT_VIEW=1.1
X_VALUE=0
Y_VALUE=1
START=0
DOTS_SIZE=10
DOTS_CONFIG="go"
LINE_COLOR="k"
LINE_STYLE="dashed"
REGION_COLOR="red"
TITLE="Graficador"

def plot_graph(inequalities,intersections,axis,view):
    """
    
    :param inequalities: list with inequalities.
    :param intersections: list with intersections of the inecualities.
    :param axis: list containing the maximum values of the intersections
    on the inequalities and the X and Y axis. Format: [maxX,maxY].
    :param view: will determine the length of the plotted graphs.

    """
    plt.title(TITLE)
    plt.axhline(y=START,color=LINE_COLOR)
    plt.axvline(x=START,color=LINE_COLOR)
    x = np.arange(change_sign(view*max(axis)),view*max(axis),LIMIT)
    
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
    region=[[],[]]
    for i in intersections:
        region[X_VALUE].append(i[X_VALUE])
        region[Y_VALUE].append(i[Y_VALUE])
    plt.fill(region[X_VALUE],region[Y_VALUE],REGION_COLOR)

    #view set-up
    plt.xlim(START-abs(axis[X_VALUE])*LEFT_VIEW,abs(axis[X_VALUE])*RIGHT_VIEW)
    plt.ylim(START-abs(axis[Y_VALUE])*LEFT_VIEW,abs(axis[Y_VALUE])*RIGHT_VIEW)
    plt.grid(True)
    plt.show()

def change_sign(number):
    return -1*number


#examples
plot_graph(["4","x*0+4"],[[0,0],[0,4],[4,4],[4,0]],[4,4],3)
plot_graph(["x","8-x"],[[0,0],[0,8],[4,4]],[8,8],3)
plot_graph(["10-x","20-x"],[[10,0],[20,0],[0,20],[0,10]],[20,20],3)
plot_graph(["10000-x"],[[0,0],[10000,0],[0,10000]],[10000,10000],3)
plot_graph(["9-x","8","x*0+8","2-x","x"],[[0,2],[0,8],[1,8],[4.5,4.5],[1,1]],[9,9],3)




