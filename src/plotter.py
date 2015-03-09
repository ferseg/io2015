import numpy as np
import matplotlib.pyplot as plt

def plot_graph(inequalities,intersections,axis,view):
    """
    
    :param inequalities: list with inequalities.
    :param intersections: list with intersections of the inecualities.
    :param axis: list containing the maximum values of the intersections
    on the inequalities and the X and Y axis. Format: [maxX,maxY].
    :param view: will determine the length of the plotted graphs.

    """
    plt.title("Graficador")
    plt.axhline(y=0,color="k")
    plt.axvline(x=0,color="k")
    x = np.arange(view*max(axis)*-1,view*max(axis),0.1)
    
    #plotting inequalities
    for i in inequalities:
        try:#plots functions
            plt.plot(x,eval(i),"k--")
        except:#draws vertical lines
            plt.axvline(x=int(eval(i)),color="k",linestyle="dashed")

    #draws intersections
    for i in intersections:
        plt.plot(i[0],i[1],"go",markersize=10)

    #paints feasible region
    region=[[],[]]
    for i in intersections:
        region[0].append(i[0])
        region[1].append(i[1])
    plt.fill(region[0],region[1],"red")

    #view set-up
    plt.xlim(0-abs(axis[0])*0.1,abs(axis[0])*1.1)
    plt.ylim(0-abs(axis[1])*0.1,abs(axis[1])*1.1)
    plt.grid(True)
    plt.show()

#examples
plot_graph(["4","x*0+4"],[[0,0],[0,4],[4,4],[4,0]],[4,4],3)
plot_graph(["x","8-x"],[[0,0],[0,8],[4,4]],[8,8],3)
plot_graph(["10-x","20-x"],[[10,0],[20,0],[0,20],[0,10]],[20,20],3)
plot_graph(["10000-x"],[[0,0],[10000,0],[0,10000]],[10000,10000],3)
plot_graph(["9-x","8","x*0+8","2-x","x"],[[0,2],[0,8],[1,8],[4.5,4.5],[1,1]],[9,9],3)




