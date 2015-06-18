__author__ = 'fsegovia'

# Testing

import graphicalMethod as gm
import transport as trns
import shortestPath as sp
#from userInterface.plotter import plot_graph
#from userInterface.plotter import matrix_to_inequation

import math_utils as leu
import simplex as si
import northwest_corner as nwc
import voguel as vg
import bag as b
import replacement as rpl
import os

# CORNER
#corner = nwc.NorthwestCorner([[3,5,8,10],[8,3,5,3],[4,3,10,7],[7,5,8,20]])
#corner.solve()
#corner.print_pretty_result()

# VOGUEL

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
# mat = [[-3, -2, 0, 0, 0, 0], [2, 1, 1, 0, 0, 18], [2, 3, 0, 1, 0, 42], [3, 1, 0, 0, 1, 24]]
# simp.set_matrix(mat)
# simp.start_simplex()
#print(simp.get_matrix())
#
EXIT = 9

running = True
PL = 1
TRANS = 2
VOGUEL = 3
CORNER = 4
BAG = 5
REPLACE = 6
SIMPLEX = 7
SHORTEST_PATH = 8

while running:
	print("\n---------- MENU ----------")
	print("[1] Programación lineal")
	print("[2] Transporte")
	print("[3] Voguel")
	print("[4] Esquina noroeste")
	print("[5] Mochila")
	print("[6] Reemplazo")
	print("[7] Simplex")
	print("[8] Camino mas corto")
	print("[9] Salir")
	option = int(input("Seleccione una opcion: "))
	if option == PL:
		matrix = eval(input("Digite la matriz con las inequaciones: "))
		objective_function = eval(input("Digite el vector de la funcion objetivo: "))
		max_min = eval(input("Digite 1 para maximizar y 0 para minimizar: "))
		y = gm.GraphicalMethod(objective_function,matrix,1)
		print(y.get_advice())
		y.plot()
	elif option == TRANS:
		cost_matrix = eval(input("Digite la matriz de costos: "))
		product_matrix = eval(input("Digite la matriz de plantas: "))
		need_matrix = eval(input("Digite la matriz de demandas: "))
		a = trns.Transport(cost_matrix,product_matrix,need_matrix)
	elif option == VOGUEL:
		matrix = eval(input("Digite la matriz con oferta y demanda: "))
		voguel = vg.Voguel(matrix)
		voguel.solve()
	elif option == CORNER:
		matrix = eval(input("Digite la matriz: "))
		corner = nwc.NorthwestCorner(matrix)
		corner.solve()
		corner.print_pretty_result()
	elif option == BAG:
		matrix = eval(input("Digite la informacion de los articulos: "))
		peso = int(input("Digite el peso: "))
		bag = b.Bag(matrix, peso)
		bag.solve()
		bag.print_pretty_result()
	elif option == REPLACE:
		matrix = eval(input("Digite el detalle de las utilidades: "))
		actual_usage_years = int(input("Digite la cantidad actual de años de la máquina: "))
		politics_years = int(input("Digite la cantidad de años de la política: "))
		min_years = int(input("Digite la cantidad mínima de años en la cual la maquina puede ser reemplazada: "))
		max_years = int(input("Digite la cantidad máxima de años en la cual la maquina puede ser reemplazada: "))
		machine_value = int(input("Digite el valor de la máquina: "))
		replace = rpl.Replacement(matrix, actual_usage_years, politics_years, min_years, max_years, machine_value)
		replace.solve()
		replace.print_pretty_result()
	elif option == SIMPLEX:
		matrix = eval(input("Digite la matriz de simplex: "))
		var_quantity = int(input("Digite la cantidad de variables: "))
		simp = si.Simplex(matrix, var_quantity)
		simp.start_simplex()
	elif option == SHORTEST_PATH:
		matrix = eval(input("Digite la matriz de costos: "))
		a = sp.ShortestPath(matrix)
		a.get_shortest_path()
	if option != EXIT:
		option = int(input("Desea continuar si [1] no [2]: "))
	elif option == EXIT:
		option = 2
	if option == 2:
		running = False
	else:
		clear = lambda: os.system('clear')
		clear()





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


"""
a = sp.ShortestPath([
	[-1, 2, 2,-1],
	[-1,-1,-1, 2],
	[-1,-1,-1, 2],
	[-1,-1,-1,-1]])
a.get_shortest_path()
"""
"""
#Ruta mas corta
a = sp.ShortestPath([
 	[-1, 5, 9, 8,-1,-1,-1], # nodo 1
 	[-1,-1,-1,-1,10,17,-1], # nodo 2
 	[-1,-1,-1,-1, 4,10,-1], # nodo 3
 	[-1,-1,-1,-1, 9, 9,-1], # nodo 4
 	[-1,-1,-1,-1,-1,-1, 8], # nodo 5
 	[-1,-1,-1,-1,-1,-1, 9], # nodo 6
 	[-1,-1,-1,-1,-1,-1,-1]  # nodo 7
 	])
[[-1, 5, 9, 8,-1,-1,-1],[-1,-1,-1,-1,10,17,-1],[-1,-1,-1,-1, 4,10,-1],[-1,-1,-1,-1, 9, 9,-1],[-1,-1,-1,-1,-1,-1, 8],[-1,-1,-1,-1,-1,-1, 9],[-1,-1,-1,-1,-1,-1,-1]]
# # 1
# # 2 3 4
# # 5 6 7
# # 7
a.get_shortest_path()

"""
