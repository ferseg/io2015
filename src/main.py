__author__ = 'fsegovia'

# Testing

#from userInterface.plotter import plot_graph
#from userInterface.plotter import matrix_to_inequation



#examples

import math_utils as leu
import simplex as si
import northwest_corner as nwc
import voguel as vg
import bag as b

simp = si.Simplex([[-2, -1, 0, 0, 0], [1, -1, 1, 0, 10], [2, 0, 0, 1, 42]], 2)

corner = nwc.NorthwestCorner([[3,5,8,10],[8,3,5,3],[4,3,10,7],[7,5,8,20]])
#corner.solve()
#corner.print_pretty_result()

#voguel = vg.Voguel([[5,2,7,3,80],[3,6,6,1,30],[6,1,2,4,60],[4,3,6,6,45],[70,40,70,35,215]])
#voguel.solve()

bag = b.Bag([[1,2,31],[2,3,47],[3,1,14]], 4)
bag.solve()
bag.print_pretty_result()

#Ejemplo 1
#mat = [[-1,-1,-2,0,0,0,0],[2,1,1,1,0,0,50], [2,1,0,0,-1,0,36], [1,0,1,0,0,-1,10]]
#Ejemplo 2 (VISTO EN CLASES)
#mat = [[-3, -2, 0, 0, 0, 0], [2, 1, 1, 0, 0, 18], [2, 3, 0, 1, 0, 42], [3, 1, 0, 0, 1, 24]]
#simp.set_matrix(mat)
#print(simp.start_simplex())
#print(simp.get_matrix())
#print(simp.solution_type)



#matrix_to_inequation([[1,0,"<=",8],[0,1,"<=",4]])


#plot_graph(["8","x*0+4"],[[0,4],[8,4],[0,0],[8,0]],[8,4])

"""plot_graph(["x","8-x"],[[0,0],[0,8],[4,4]],[8,8])
plot_graph(["10-x","20-x"],[[20,0],[0,20],[10,0],[0,10]],[20,20])
plot_graph(["10000-x"],[[0,0],[10000,0],[0,10000]],[10000,10000])
plot_graph(["9-x","8","x*0+8","2-x","x"],[[4.5,4.5],[0,2],[0,8],[1,8],[1,1]],[9,9])
plot_graph(["18-2*x","(42-2*x)/3","24-3*x"],[[0,0],[8,0],[3,12],[0,14],[6,6]],[20,20])
plot_graph(["(24-6*x)/4","(6-x)/2","1+x","2+0*x"],[[4,0],[3,1.5],[0,0],[2,2],[1,2],[0,1]],[6,6])"""
