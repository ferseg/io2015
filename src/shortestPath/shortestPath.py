
INVALID_PATH = -1
LAST_ELEMENT = -1

class ShortestPath:
	"""
	Solves the Transport Algorithm
	"""
	def __init__(self, cost_matrix):
		self.cost_matrix = cost_matrix
		self.paths = []
		self.result = []

	def get_shortest_path(self):
		costo = 0
		result = [[len(self.cost_matrix)-1]]
		final_result = []
		while True:
			newPath = [get_next_table(self.cost_matrix,result[LAST_ELEMENT])]
			if any(x == 0 for x in result[LAST_ELEMENT]):
				break
			result += newPath		
		
		self.reference = []
		for i in range(len(self.cost_matrix)):
			self.reference += [-1]
		self.reference[-1] = 0

		self.index = len(result)-1
		index = len(result)
		self.text = "Etapa " + str(index) + ".\n"
		self.text += "Punto de partida: " + str(len(self.cost_matrix)) + ".\n"
		self.text += "Costo: " + str(costo) + ".\n"

		past = result[0]
		result = result[1:]
		while result != []:
			index = len(result)
			temp = []
			temp += [['x' + str(index)]]
			for x in past:
				temp[0] += ["x=" + str(x+1)]
			temp[0] += ["Total","x"+ str(index+1)]
			for element in result[0]:
				temp += [[(element + 1)]]
				minimal_path = []
				minimal_cost = -1
				for node in past:
					cost = self.get_cost(element,node)
					rest_of_travel = self.reference[node]
					#print(cost,rest_of_travel,element)
					
					if (cost != INVALID_PATH and ((cost + rest_of_travel) < minimal_cost)) or (minimal_cost == -1 and cost != INVALID_PATH):
						minimal_cost = cost + rest_of_travel
						minimal_path = [node + 1]
						self.reference[element] = minimal_cost
					
					elif (cost+rest_of_travel) == minimal_cost:
						minimal_path += [node + 1]

					if cost != INVALID_PATH:#si existe el camino
						temp[LAST_ELEMENT] += [cost+rest_of_travel]
					else:#si no existe el camino
						temp[LAST_ELEMENT] += ['-']
				#node contiene el nodo pasado
				#cost = costo dl viaje de element a node
				temp[LAST_ELEMENT] += [minimal_cost,minimal_path]
			self.result += [temp]
			self.paths += temp
			past = result[0]
			result = result[1:]
		self.solve_path()

	def solve_path(self):
		index = self.index
		self.text += "\n"
		for element in self.result:
			self.text += "Etapa " + str(index) + ".\n"
			for row in element:
				for entry in row:
					self.text += '|%8s' % str(entry)
				self.text += "|\n"
			self.text += "\n"
			index -= 1
		print(self.text)
		path = "Ruta:\n1"
		index = [0]
		result = [1]
		while index[0] != len(self.cost_matrix):
			index = self.get_next_node(index[0]+1)
			#if len(index) == 0:
			result += [index][0]
			path += " -> " + str(index[0])
			#else:
				#temp = self.get_path(index,path)
				#print(temp)
		#print(result)
		print(path + "\nCon un costo de: " +str(self.reference[0]))
		return

	def get_path(self,index,path):
		result = []
		for i in self.get_next_node(index):
			result += self.get_next_node(index[0]+1)
			path += " -> " + str(index)

	def get_cost(self,pos1,pos2):
		result = self.cost_matrix[pos1][pos2]
		if result < 0:
			return INVALID_PATH
		return result

	def to_string(self):
		text = ""
		for element in self.cost_matrix:
			for entry in element:
				text += ('%3s' % entry)
			text += "\n"
		print(text)
	
	def get_next_node(self,nextNode):
		for element in self.paths:
			if element[0] == nextNode:
				return element[LAST_ELEMENT]
		return [INVALID_PATH]


def get_next_table(matrix,index):
	result = []
	rowIndex = 0
	for element in index:
		while rowIndex < len(matrix):
			if matrix[rowIndex][element] != INVALID_PATH:
				result += [rowIndex]
			rowIndex += 1
	return result
