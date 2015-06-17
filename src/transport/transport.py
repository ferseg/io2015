import graphicalMethod as gm
#from graphicalMethod import GraphicalMethod

TABLE_LEN = 10

class Transport:
	"""
	Solves the Transport Algorithm
	"""
	def __init__(self, cost_matrix, plants, cities):
		self.cost_matrix = cost_matrix
		self.plants = plants
		self.cities = cities
		self.inequation_matrix = self.get_inequations()
		self.objective_function = self.get_objective_function()
		self.eval_inequations()

	def get_inequations(self):
		temp = []
		temp += [[1,1,"<=",self.plants[0]]]
		temp += [[1,0,"<=",self.cities[0]]]
		temp += [[0,1,"<=",self.cities[1]]]
		temp += [[1,1,">=",-(self.cities[2]-self.plants[0])]]
		return temp

	def get_objective_function(self):
		temp = [self.cost_matrix[0][0],self.cost_matrix[0][1],0]
		index = 2
		cost_index = 0
		for element in self.inequation_matrix:
			if index == 2 and cost_index == 1:
				temp[0] += self.cost_matrix[cost_index][index] * element[0]
				temp[1] += self.cost_matrix[cost_index][index] * element[1]
				temp[2] += self.cost_matrix[cost_index][index] * (-element[3])
				break
			temp[0] += self.cost_matrix[cost_index][index] * (-element[0])
			temp[1] += self.cost_matrix[cost_index][index] * (-element[1])
			temp[2] += self.cost_matrix[cost_index][index] * element[3]
			if index == 2:
				index = 0
				cost_index += 1
			else:
				index += 1
		return temp

	def eval_inequations(self):
		graph = gm.GraphicalMethod(self.objective_function,self.inequation_matrix,0)
		text = self.get_advice(graph)
		print(text)
		graph.plot()

	def get_advice(self,graph):
		text = graph.get_advice()
		result = graph.get_solution()
		x = result[0][0][0]
		y = result[0][0][1]
		text += "\nSolución: X=" + str(x) + ". Y=" + str(y) + ".\n"
		text += "-" * TABLE_LEN * 4 + "-"*5 +"\n"
		text += "|" + ('%10s' % "") + "|" + ('%10s' % "Ciudad1") + "|" + ('%10s' % "Ciudad2") + "|" + ('%10s' % "Ciudad3") + "|\n"
		text += "|" + ('%10s' % "Planta1")
		text += "|" + ('%10s' % str(x))
		text += "|" + ('%10s' % str(y))
		text += "|" + ('%10s' % str(eval(str(self.inequation_matrix[0][3]) + "-x-y")))
		text += "|\n"

		text += "|" + ('%10s' % str("Planta2"))
		text += "|" + ('%10s' % str(eval(str(self.inequation_matrix[1][3]) + "-x")))
		text += "|" + ('%10s' % str(eval(str(self.inequation_matrix[2][3]) + "-y")))
		text += "|" + ('%10s' % str(eval(str(-self.inequation_matrix[3][3]) + "+x+y")))
		text += "|\n"
		text += "-" * 45 + "\n"
		return text

	def to_string(self):
		return [self.cost_matrix] + [self.plants] + [self.cities] + [self.inequation_matrix] + [self.objective_function]

