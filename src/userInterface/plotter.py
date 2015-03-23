import numpy as np
import math
import matplotlib.pyplot as plt


#Constant definition
GRID=True
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
    plt.grid(GRID)
    plt.show()

def change_sign(number):
    return -1*number

def sort_intersections(point,intersections):
    temp = get_distances(point,intersections)
    temp2 = [get_min_index(temp)[:-1]]
    temp.remove(get_min_index(temp))
    while temp != []:
        temp2 += [get_min_index(temp)[:-1]]
        temp.remove(get_min_index(temp))
        temp = get_distances(temp2[-1],temp)
    return temp2

def get_distances(point,intersections):
    j = []
    for i in intersections:
        x_point = abs(point[0] - i[0])
        y_point = abs(point[1] - i[1])
        if len(i)==2:
            j += [i + [math.sqrt(x_point**2+y_point**2)]]
        else:
            j += [i]
            j[-1][2] = math.sqrt(x_point**2+y_point**2)
    return j

def get_min_index(intersections):
    temp = intersections[0][2]
    index = 0
    cont = 0
    for i in intersections:
        if i[2]<temp:
            temp = i[2]
            index = cont
        cont += 1
    return intersections[index]
#######################################################
def sort2(intersections):
    return split_list(intersections)
    

def split_list(intersections):
    temp = get_max(intersections)
    mins = []
    maxs = []
    for i in intersections:
        if i[0] < temp[0]:
            mins += [i]
        elif i[0] >= temp[0]:
            maxs += [i]
    #return sort(mins)+(sort(maxs).reverse())
    mins=sort_intersec(mins)
    mins.reverse()
    return mins+sort_intersec(maxs)

def sort_intersec(intersections):
    temp = []
    temp2 = intersections
    while temp2 != []:
        max_intersection = get_max(temp2)
        temp += [max_intersection]
        temp2.remove(max_intersection)
    return temp

def get_max(intersections):
    temp = intersections[0]
    for i in intersections:
        if i[1] > temp[1]:
            temp = i
        elif i[1] == temp[1]:
            if i[0] > temp[0]:
                temp = i
    return temp

#examples
##plot_graph(["4","x*0+4"],[[0,0],[0,4],[4,4],[4,0]],[4,4],3)
##plot_graph(["x","8-x"],[[0,0],[0,8],[4,4]],[8,8],3)
##plot_graph(["10-x","20-x"],[[10,0],[20,0],[0,20],[0,10]],[20,20],3)
##plot_graph(["10000-x"],[[0,0],[10000,0],[0,10000]],[10000,10000],3)
##plot_graph(["9-x","8","x*0+8","2-x","x"],[[0,2],[0,8],[1,8],[4.5,4.5],[1,1]],[9,9],3)
##plot_graph(["18-2*x","(42-2*x)/3","24-3*x"],[[0,0],[8,0],[6,6],[3,12],[0,14]],[20,20],3)
##plot_graph(["(24-6*x)/4","(6-x)/2","1+x","2+0*x"],[[0,0],[4,0],[3,1.5],[2,2],[1,2],[0,1]],[6,6],3)


import itertools

intersections = [[0,2],[0,8],[1,8],[4.5,4.5],[1,1]]
for i in itertools.permutations(intersections):
    plot_graph(["9-x","8","x*0+8","2-x","x"],sort2(i),[9,9],3)
####    plot_graph(["(24-6*x)/4","(6-x)/2","1+x","2+0*x"],sort_intersections([0,0],i),[6,6],3)

#print(sort_intersections([0,0],intersections))
#intersections = [[0,4],[0,0],[4,4],[4,0]]
#print(split_list(intersections))
