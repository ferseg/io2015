import graphicalMethod as gm
import numpy as np
import operator
import math_utils as mu


MAX = '>'
MIN = '<'
OPERATORS = {
            MAX: operator.gt,
            MIN: operator.lt,
            }

MAX_NUM = 99999

X_AXIS_FUNCTION = [1,0,">=",0]
Y_AXIS_FUNCTION = [0,1,">=",0]
X_MAX_AXIS = [1,0,"<=",MAX_NUM]
Y_MAX_AXIS = [0,1,"<=",MAX_NUM]

START = 0
X_VALUE = 0
Y_VALUE = 1
Z_VALUE = 3

class GraphicalMethod:
	"""
	Solves the Graphical Method Algorithm
	"""
	def __init__(self, objective_function, inequations_matrix,max_min):
		if max_min == 0:
			self.max_min = MIN
		else:
			self.max_min = MAX
		self.objective_function = objective_function
		self.inequations_matrix = inequations_matrix + [X_AXIS_FUNCTION] + [Y_AXIS_FUNCTION] + [X_MAX_AXIS] + [Y_MAX_AXIS]
		self.intersections = get_intersections(self.inequations_matrix)

		temp = inequations_matrix + [X_AXIS_FUNCTION] + [Y_AXIS_FUNCTION]
		temp = get_intersections(temp)
		self.max_intersections = get_Max(temp)

	def matrix_to_inequation(self):
	    inequations = []
	    matrix = self.inequations_matrix
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
		gm.plot_graph(inequations,intersections,maxAxis)
	
	def get_advice(self):
		result = self.get_solution()
		text = "Puntos:\n"
		for element in result[1]:
			text += "X: " + ('%10s' % str(element[X_VALUE])) + ". Y: " + ('%10s' % str(element[Y_VALUE])) + ". Con un valor de: " + ('%10s' % str(element[2])) + ".\n"
		text += "Recomendación:"
		if len(result[0]) == 0:
			text += "El problema posee solución no acotada.\n"
		elif len(result[0]) == 1:
			text += "El problema posee solución única.\n"
		else:
			text += "El problema posee soluciónes multiples.\n"
		for element in result[0]:
			text += "X: " + ('%10s' % str(element[X_VALUE])) + ". Y: " + ('%10s' % str(element[Y_VALUE])) + ". Con un valor de: " + ('%10s' % str(element[2])) + ".\n"
		return text

	def get_solution(self):
		inequations = self.matrix_to_inequation()
		intersections = mu.eval_intersections(self.inequations_matrix, self.intersections)
		maxAxis = self.max_intersections
		result = get_FO(intersections,self.objective_function,self.max_min)
		return result

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
	return make_unique(result)

def get_FO(intersections,objective_function,max_min):
	result = [[],[]]
	ofX = objective_function[X_VALUE]
	ofY = objective_function[Y_VALUE]
	ofZ = objective_function[2]
	flag = True
	if intersections == []:
		return result
	else:
		varX = intersections[START][X_VALUE]
		varY = intersections[START][Y_VALUE]
		value = varX * ofX + varY * ofY
		result[0] += [[varX,varY,value]]
		result[1] += [[varX,varY,value]]
		intersections = intersections[1:]
		for element in intersections:
			varX = intersections[START][X_VALUE]
			varY = intersections[START][Y_VALUE]
			if varX != MAX_NUM and varY != MAX_NUM and flag:
				value = varX * ofX + varY * ofY + ofZ
				if OPERATORS[max_min](value, result[0][START][2]):
					result[0] = [[varX,varY,value]]
				elif value == result[0][START][2]:
					result[0] += [[varX,varY,value]]
				result[1] += [[varX,varY,value]]
			elif varX != MAX_NUM and varY != MAX_NUM:
				value = varX * ofX + varY * ofY + ofZ
				result[1] += [[varX,varY,value]]
			elif (varX == MAX_NUM or varY == MAX_NUM) and max_min == MAX:
				result[0] = []
				flag = False
			intersections = intersections[1:]
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

