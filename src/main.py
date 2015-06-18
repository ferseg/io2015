__author__ = 'fsegovia'

# Testing

# import graphicalMethod as gm
# import transport as trns
# import shortestPath as sp
#from userInterface.plotter import plot_graph
#from userInterface.plotter import matrix_to_inequation

import math_utils as leu
import simplex as si
import northwest_corner as nwc
import voguel as vg
import bag as b
import replacement as rpl

# CORNER
#corner = nwc.NorthwestCorner([[3,5,8,10],[8,3,5,3],[4,3,10,7],[7,5,8,20]])
#corner.solve()
#corner.print_pretty_result()

#voguel = vg.Voguel([[5,2,7,3,80],[3,6,6,1,30],[6,1,2,4,60],[4,3,6,6,45],[70,40,70,35,215]])
#voguel.solve()

#bag = b.Bag([[1,2,31],[2,3,47],[3,1,14]], 4)
#bag.solve()
#bag.print_pretty_result()

# REPLACE
# data, actual usage years, years of the politics, min replacement year, max replacement year, cost of the machine
#replace = rpl.Replacement([[20000,200,0],[19000,600,80000],[18500,1200,60000],[17200,1500,50000],[15500,1700,30000],[14,1800,10000],[12200,2200,5000]], 3, 4, 0, 6, 100000)
#replace.solve()
#replace.print_pretty_result()


# SIMPLEX
#simp = si.Simplex([[-2, -1, 0, 0, 0], [1, -1, 1, 0, 10], [2, 0, 0, 1, 42]], 2)\
#Ejemplo 1
#mat = [[-1,-1,-2,0,0,0,0],[2,1,1,1,0,0,50], [2,1,0,0,-1,0,36], [1,0,1,0,0,-1,10]]
#Ejemplo 2 (VISTO EN CLASES)
mat = [[-3, -2, 0, 0, 0, 0], [2, 1, 1, 0, 0, 18], [2, 3, 0, 1, 0, 42], [3, 1, 0, 0, 1, 24]]
simp.set_matrix(mat)
simp.start_simplex()
#print(simp.get_matrix())


"""
#metodo grafico
y = gm.GraphicalMethod([0.75,1,0],[[1,3,"<=",15],[5,1,"<=",20],[3,4,"<=",24]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([0.75,1,0],[[0,1,"<=",5],[0,1,">=",10],[1,0,"<=",5]],1)
print(y.get_advice())
y.plot()


y = gm.GraphicalMethod([0.75,1,0],[[0,1,"<=",4]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([0.75,1,0],[[1,0,"<=",4]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([6,10,0],
	[[1,0,"<=",1000],
	[0,1,"<=",700],
	[1,1,"<=",800],
	[1,1,">=",200]],0)
print(y.get_advice())
y.plot()



y = gm.GraphicalMethod([1,1,0],
	[[2,-1,">=",0],
	[1,1,"<=",150],
	[1,0,">=",40],
	[0,1,">=",20]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([1500,1000,0],
	[[1,1,"<=",3000],
	[1,0,"<=",2000],
	[0,1,"<=",2000]],1)
print(y.get_advice())
y.plot()


y = gm.GraphicalMethod([4,2,0],
	[[2,1,"<=",4],
	[1,-1,"<=",1]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([1,1,0],
	[[2,-1,">=",0],
	[1/2,-1,"<=",0]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([1,1,0],
	[[2,-1,">=",0],
	[1/2,-1,"<=",0]],0)
print(y.get_advice())
y.plot()
"""



"""
#Transporte
a = trns.Transport([[3,7,1],[2,2,6]],[800,1500],[1000,700,600])

a = trns.Transport([[50,60,10],[25,40,20]],[500,400],[200,300,400])

a = trns.Transport([[100,150,200],[150,120,180]],[4000,5000],[2000,3000,4000])

a = trns.Transport([[3,2.5,3.5],[2.25,3.75,4]],[5000,7000],[3500,4000,4500])
"""


#Ruta mas corta
# a = sp.ShortestPath([
# 	[-1, 5, 9, 8,-1,-1,-1], # nodo 1
# 	[-1,-1,-1,-1,10,17,-1], # nodo 2
# 	[-1,-1,-1,-1, 4,10,-1], # nodo 3
# 	[-1,-1,-1,-1, 9, 9,-1], # nodo 4
# 	[-1,-1,-1,-1,-1,-1, 8], # nodo 5
# 	[-1,-1,-1,-1,-1,-1, 9], # nodo 6
# 	[-1,-1,-1,-1,-1,-1,-1]  # nodo 7
# 	])

# # 1
# # 2 3 4
# # 5 6 7
# # 7

# #a.to_string()
# a.get_shortest_path()

