
INVALID_PATH = -1
LAST_ELEMENT = -1

class ShortestPath:
	"""
	Solves the Transport Algorithm
	"""
	def __init__(self, cost_matrix):
		self.cost_matrix = cost_matrix

	def get_shortest_path(self):
		costo = 0
		result = [[[len(self.cost_matrix)-1,0]]]
		while True:
			newPath = [get_next_table(self.cost_matrix,result[LAST_ELEMENT])]
			if search_path(result[LAST_ELEMENT],0):
				break
			result += newPath


		index = len(result)
		text = "Etapa " + str(index) + ".\n"
		text += "Punto de partida: " + str(len(self.cost_matrix)) + ".\n"
		text += "Costo: " + str(costo) + ".\n"


		"""
		past = result[0]
		result = result[1:]
		index = len(result)
		text += "\nEtapa "+ str(index) + ".\n"
		temp = []

		
		pos = 0
		for element in result[0]:
			temp += [[(element[0] + 1)]]
			minimal_path = 0
			minimal_cost = 0
			for node in past:
				if ((element[1] + node[1]) < minimal_cost) or minimal_cost == 0:
					minimal_cost = element[1] + node[1]
					minimal_path = node[0]
				temp[pos] += [element[1] + node[1]]
				#node[0] tiene el nodo que se utilizó
				#node[1] tiene el costo dl viaje
				#element[1] tiene el costo dl viaje anterior
			temp[pos] += [minimal_cost,minimal_path]
			pos += 1
		
		print(temp)
		#print(text)
		print(result)
		"""


		past = result[0]
		result = result[1:]
		index = len(result)
		text += "\nEtapa "+ str(index) + ".\n"
		temp = []

		pos = 0
		for element in result[0]:
			temp += [[(element[0] + 1)]]
			minimal_path = 0
			minimal_cost = 0
			for node in past:
				if ((element[1] + node[1]) < minimal_cost) or minimal_cost == 0:
					minimal_cost = element[1] + node[1]
					minimal_path = node[0]
				temp[pos] += [element[1] + node[1]]
				#node[0] tiene el nodo que se utilizó
				#node[1] tiene el costo dl viaje
				#element[1] tiene el costo dl viaje anterior
			temp[pos] += [minimal_cost,minimal_path]
			pos += 1
		
		print(temp)
		print(result)

	

	def to_string(self):
		text = ""
		for element in self.cost_matrix:
			for entry in element:
				text += ('%3s' % entry)
			text += "\n"
		print(text)

def get_next_table(matrix,index):
	result = []
	rowIndex = 0
	for element in index:
		while rowIndex < len(matrix):
			if matrix[rowIndex][element[0]] != INVALID_PATH:
				result += [[rowIndex,matrix[rowIndex][element[0]]]]
			rowIndex += 1
	return result

def search_path(matrix,reference):
	for element in matrix:
		if element[0] == reference:
			return True
	return False