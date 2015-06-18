import math_utils as m_utils

class Voguel:
	"""docstring for Voguel"""

	__ROW = 0
	__COLUMN = 1

	__INDEX = 0
	__VALUE = 1

	def __init__(self, matrix):
		self.matrix = matrix
		len_mat = len(matrix) - 1 
		self.resulting_matrix = m_utils.init_matrix(len_mat, len_mat)

	def solve(self):
		current_indexes = []
		current_indexes += [self.init_indexes(len(self.matrix) - 1)]
		current_indexes += [self.init_indexes(len(self.matrix[0]) - 1)]
		while len(self.matrix) != 1:
			resulting_differences = [[], []]
			resulting_differences[self.__ROW] = self.get_penalization(self.matrix)
			transposed_matrix = m_utils.transposed(self.matrix)
			resulting_differences[self.__COLUMN] = self.get_penalization(transposed_matrix)
			highest_element = m_utils.get_highest_element_in_matrix(resulting_differences)
			highest_element_row = highest_element[self.__INDEX]
			highest_element_col = highest_element[self.__VALUE]
			is_supply = highest_element_row != self.__ROW
			temp_matrix = transposed_matrix if is_supply else self.matrix
			lower_cost = m_utils.get_lowest(temp_matrix[highest_element_col])
			lower_to_choose_last_row = [lower_cost[self.__INDEX], temp_matrix[len(temp_matrix)-1][lower_cost[self.__INDEX]]]
			lower_to_choose_current_row = [highest_element_col, temp_matrix[highest_element_col][len(temp_matrix[self.__ROW])-1]]
			selected = lower_to_choose_last_row if lower_to_choose_last_row[self.__VALUE] < lower_to_choose_current_row[1]  else lower_to_choose_current_row
			temp_matrix[len(temp_matrix)-1][lower_cost[self.__INDEX]] -= selected[self.__VALUE]
			temp_matrix[highest_element_col][len(temp_matrix[self.__ROW])-1] -= selected[self.__VALUE]
			is_normal = lower_to_choose_current_row != selected
			real_row = current_indexes[self.__ROW][lower_cost[self.__INDEX] if is_supply else highest_element_col]
			real_col = current_indexes[self.__COLUMN][highest_element_col if is_supply else lower_cost[self.__INDEX]]
			self.resulting_matrix[real_row][real_col] += lower_cost[self.__VALUE] * selected[self.__VALUE]
			temp_matrix = m_utils.transposed(temp_matrix) if is_normal else temp_matrix
			row_to_be_deleted = lower_to_choose_last_row[self.__INDEX] if is_normal else lower_to_choose_current_row[self.__INDEX]
			current_indexes[is_supply != is_normal] = m_utils.delete_element_in_array(current_indexes[is_supply != is_normal], row_to_be_deleted)
			# Last step, deletes the selected row
			temp_matrix = m_utils.delete_row(temp_matrix, row_to_be_deleted)
			self.matrix = m_utils.transposed(temp_matrix) if (is_supply and not is_normal) or (not is_supply and is_normal) else temp_matrix
			print("MATRIZ ACTUAL")
			m_utils.print_matrix(self.matrix)
			print("MATRIZ DE PESOS")
			m_utils.print_matrix(self.resulting_matrix)
			print("\n==============================================================\n")
		print("Resultado total:", self.get_sum_matrix())

	def get_sum_matrix(self):
		matrix = self.resulting_matrix
		result = 0
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix[i])):
				result += matrix[i][j]
		return result



	def get_penalization(self, matrix):
		penalizations = []
		for row in range(0, len(matrix) - 1):
			actual_row = matrix[row]
			penalizations += [self.get_difference_between_lowers(actual_row[:-1])]
		return penalizations

	def get_difference_between_lowers(self, row):
		first_low = m_utils.get_lowest(row)
		new_row = m_utils.delete_element_in_array(row, first_low[0])
		second_low = m_utils.get_lowest(new_row)
		result = 0
		if second_low != [-1, 99999999]:
			result = second_low[1] - first_low[1]
		return result

	def init_indexes(self, quantity):
		result = []
		for row in range(0, quantity):
			result += [row]
		return result
				