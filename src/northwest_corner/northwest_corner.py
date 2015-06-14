class NorthwestCorner:
	"""docstring for NorthwestCorner"""

	__ROW_INDEX = 0
	__COLUMN_INDEX = 1
	def __init__(self, matrix):
		self.matrix = matrix
		self.result_index = [len(self.matrix), len(self.matrix[self.__ROW_INDEX])]
		self.resulting_matrix = self.init_matrix(self.result_index[self.__COLUMN_INDEX]-1, self.result_index[self.__ROW_INDEX]-1)

	def solve(self):
		"""
		Solves the NorthwestCorner algorithm
		"""
		# row and column to control the selected corner
		current_positions = [0, 0]
		max_row = self.result_index[self.__ROW_INDEX]-1
		max_col = self.result_index[self.__COLUMN_INDEX]-1
		while self.matrix[max_row][max_col] != 0:
			current_row = current_positions[self.__ROW_INDEX]
			current_column = current_positions[self.__COLUMN_INDEX]
			multiplier_selected = self.get_multiplier_with_index(current_row, current_column)
			actual_weight = self.matrix[current_row][current_column]
			actual_result_weight = multiplier_selected[1]
			self.resulting_matrix[current_row][current_column] = actual_weight * actual_result_weight
			self.matrix[max_row][max_col] -= actual_result_weight
			self.matrix[current_row][max_col] -= actual_result_weight
			self.matrix[max_row][current_column] -= actual_result_weight
			current_positions[multiplier_selected[0]] += 1


	def init_matrix(self, col_quantity, row_quantity):
		actual_quantity = 0
		result = []
		while actual_quantity < row_quantity:
			new_row = [[0]*col_quantity]
			result += new_row
			actual_quantity+=1
		return result


	def get_multiplier_with_index(self, row, column):
		supply = self.matrix[row][self.result_index[self.__COLUMN_INDEX]-1]
		demand = self.matrix[self.result_index[self.__ROW_INDEX]-1][column]
		result = [0, 0]
		result[0] = self.__ROW_INDEX if supply < demand else self.__COLUMN_INDEX
		result[1] = supply if supply < demand else demand
		return result

	def print_pretty_result(self):
		"""
		Prints the result in a prettier way
		"""
		for row in range(0, len(self.resulting_matrix)):
			for col in range(0, len(self.resulting_matrix[self.__ROW_INDEX])):
				actual_number = self.resulting_matrix[row][col]
				if (actual_number != 0):
					print ("A la ciudad ", row+1, " en la fabrica ", col+1, " se envía ", actual_number)

		