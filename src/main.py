__author__ = 'fsegovia'

# Testing

from userInterface.plotter import plot_graph
from userInterface.plotter import matrix_to_inequation



#examples

import math_utils as leu
import simplex as si


simp = si.Simplex([1], 2)

#Ejemplo 1
#mat = [[-1,-1,-2,0,0,0,0],[2,1,1,1,0,0,50], [2,1,0,0,-1,0,36], [1,0,1,0,0,-1,10]]
#Ejemplo 2 (VISTO EN CLASES)
mat = [[-3, -2, 0, 0, 0, 0], [2, 1, 1, 0, 0, 18], [2, 3, 0, 1, 0, 42], [3, 1, 0, 0, 1, 24]]
simp.set_matrix(mat)
print(simp.start_simplex())
print(simp.get_matrix())



matrix_to_inequation([[1,0,"<=",8],[0,1,"<=",4]])


#plot_graph(["8","x*0+4"],[[0,4],[8,4],[0,0],[8,0]],[8,4])

"""plot_graph(["x","8-x"],[[0,0],[0,8],[4,4]],[8,8])
plot_graph(["10-x","20-x"],[[20,0],[0,20],[10,0],[0,10]],[20,20])
plot_graph(["10000-x"],[[0,0],[10000,0],[0,10000]],[10000,10000])
plot_graph(["9-x","8","x*0+8","2-x","x"],[[4.5,4.5],[0,2],[0,8],[1,8],[1,1]],[9,9])
plot_graph(["18-2*x","(42-2*x)/3","24-3*x"],[[0,0],[8,0],[3,12],[0,14],[6,6]],[20,20])
plot_graph(["(24-6*x)/4","(6-x)/2","1+x","2+0*x"],[[4,0],[3,1.5],[0,0],[2,2],[1,2],[0,1]],[6,6])"""