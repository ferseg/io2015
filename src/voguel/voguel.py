import math_utils as m_utils

class Voguel:
	"""docstring for Voguel"""

	__ROW = 0
	__COLUMN = 1

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
			resulting_differences[0] = self.get_penalization(self.matrix)
			transposed_matrix = m_utils.transposed(self.matrix)
			resulting_differences[1] = self.get_penalization(transposed_matrix)
			highest_element = m_utils.get_highest_element_in_matrix(resulting_differences)
			highest_element_row = highest_element[0]
			highest_element_col = highest_element[1]
			is_supply = highest_element_row != self.__ROW
			temp_matrix = transposed_matrix if is_supply else self.matrix
			lower_cost = m_utils.get_lowest(temp_matrix[highest_element_col])
			lower_to_choose_last_row = [lower_cost[0], temp_matrix[len(temp_matrix)-1][lower_cost[0]]]
			lower_to_choose_current_row = [highest_element_col, temp_matrix[highest_element_col][len(temp_matrix[0])-1]]
			selected = lower_to_choose_last_row if lower_to_choose_last_row[1] < lower_to_choose_current_row[1]  else lower_to_choose_current_row
			temp_matrix[len(temp_matrix)-1][lower_cost[0]] -= selected[1]
			temp_matrix[highest_element_col][len(temp_matrix[0])-1] -= selected[1]
			is_normal = lower_to_choose_current_row != selected
			if is_supply:
				real_row = current_indexes[1][lower_cost[0]]
				real_col = current_indexes[1][highest_element_col]
			else:
				real_row = current_indexes[0][highest_element_col]
				real_col = lower_cost[0]
			self.resulting_matrix[real_row][real_col] += lower_cost[1] * selected[1]
			current_indexes[highest_element_row != is_normal] = m_utils.delete_element_in_array(current_indexes[highest_element_row != is_normal], highest_element_col)
			temp_matrix = m_utils.transposed(temp_matrix) if is_normal else temp_matrix
			row_to_be_deleted = lower_to_choose_last_row[0] if is_normal else lower_to_choose_current_row[0]
			# Last step, deletes the selected row
			temp_matrix = m_utils.delete_row(temp_matrix, row_to_be_deleted)
			self.matrix = m_utils.transposed(temp_matrix) if (is_supply and not is_normal) or (not is_supply and is_normal) else temp_matrix
			m_utils.print_matrix(self.matrix)


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
				