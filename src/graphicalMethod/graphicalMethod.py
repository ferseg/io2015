import graphicalMethod as gm
import numpy as np
import math_utils as mu

MAX_NUM = 99999

X_AXIS_FUNCTION = [1,0,">=",0]
Y_AXIS_FUNCTION = [0,1,">=",0]
X_MAX_AXIS = [1,0,"<=",MAX_NUM]
Y_MAX_AXIS = [0,1,"<=",MAX_NUM]

X_VALUE = 0
Y_VALUE = 1
Z_VALUE = 3

class GraphicalMethod:
	"""
	Solves the Graphical Method Algorithm
	"""
	def __init__(self, objective_function, inequations_matrix,max_min):
		self.max_min = max_min
		self.objective_function = objective_function
		self.inequations_matrix = inequations_matrix + [X_AXIS_FUNCTION] + [Y_AXIS_FUNCTION] + [X_MAX_AXIS] + [Y_MAX_AXIS]
		self.intersections = get_intersections(self.inequations_matrix)
		self.max_intersections = get_Max(mu.eval_intersections(self.inequations_matrix, self.intersections))

	def matrix_to_inequation(self):
	    inequations = []
	    matrix = self.inequations_matrix
	    #matrix.remove(X_MAX_AXIS)
	    #matrix.remove(Y_MAX_AXIS)
	    #matrix.remove(X_AXIS_FUNCTION)
	    #matrix.remove(Y_AXIS_FUNCTION)
	    for element in matrix:
	        if element[X_VALUE] == 0:
	            inequations += ["x*0+"+str(element[Z_VALUE]/element[Y_VALUE])]
	        elif element[Y_VALUE] == 0:
	            inequations += [str(element[Z_VALUE]/element[X_VALUE])]
	        else:
	        	inequations += [str(element[Z_VALUE]/element[Y_VALUE]) +"+x*"+str(-element[X_VALUE]/element[Y_VALUE])]
	    return inequations

	def plot(self):
		inequations = self.matrix_to_inequation()
		intersections = mu.eval_intersections(self.inequations_matrix, self.intersections)
		maxAxis = self.max_intersections
		
		#print(self.intersections)
		#print("\n\n")
		#print(intersections)
		
		#print(inequations)
		#print(make_unique(intersections))
		#print(maxAxis)
		gm.plot_graph(inequations,intersections,maxAxis)

def get_intersections(inequations_matrix):
	result = []
	while len(inequations_matrix) > 1:
		current_eq = inequations_matrix[0]
		inequations_matrix = inequations_matrix[1:]
		for element in inequations_matrix:
			variables = [current_eq[:2]] + [element[:2]]
			solves = [current_eq[-1]] + [element[-1]]
			temp = solve_eq(variables,solves)
			if temp != []:
				result += [temp]
	return result

def solve_eq(variables,results):
	try:
		a = np.array(variables)
		b = np.array(results)
		x = np.linalg.solve(a, b)
		return [x[X_VALUE],x[Y_VALUE]]
	except:
		return []

def get_Max(intersections_list):
	maxX = intersections_list[0][X_VALUE]
	maxY = intersections_list[0][Y_VALUE]
	intersections_list = intersections_list[1:]
	for element in intersections_list:
		if element[X_VALUE] > maxX and element[X_VALUE] != MAX_NUM:
			maxX = element[X_VALUE]
		if element[Y_VALUE] > maxY and element[Y_VALUE] != MAX_NUM:
			maxY = element[Y_VALUE]
	if maxX == 0 and maxY == 0:
		maxX = maxY = 1
	elif maxX == 0:
		maxX = maxY
	elif maxY == 0:
		maxY = maxX
	return [maxX,maxY]

def make_unique(original_list):
    unique_list = []
    [unique_list.append(obj) for obj in original_list if obj not in unique_list]
    return unique_list

