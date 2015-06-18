import math_utils as m_utils
import math

class Bag:
	"""docstring for Bag"""

	__STEPS = 0
	__WEIGHT = 1
	__INCOME = 2

	__INDEX = 1
	__VALUE = 0

	def __init__(self, info, max_capacity):
		self.info = m_utils.transposed(info)
		self.max_capacity = max_capacity + 1
		self.last_maximun_column = m_utils.init_matrix(2, self.max_capacity)
		self.result = []

	def solve(self):
		for step in range(0, len(self.info)):
			actual_step = len(self.info) - 1 - step
			current_element_weight = self.info[self.__WEIGHT][actual_step]
			current_element_income = self.info[self.__INCOME][actual_step]
			max_amount_of_elements = math.floor((self.max_capacity-1) / current_element_weight) + 1
			resulting_matrix = m_utils.init_matrix(max_amount_of_elements, self.max_capacity)
			# --> Transposed the main matrix
			resulting_matrix = m_utils.transposed(resulting_matrix)
			resulting_matrix = self.fill_matrix(resulting_matrix, max_amount_of_elements, current_element_income, current_element_weight)
			resulting_matrix = m_utils.transposed(resulting_matrix)
			self.set_last_maximun_column(resulting_matrix)
			self.fuse_matrix_with_results(resulting_matrix)
			self.result += [resulting_matrix]
			

	def get_initial_resulting_matrix(self, actual_step):
		current_element_weight = self.info[__WEIGHT][actual_step]
		max_amount_of_elements = max_capacity / current_element_weight
		resulting_matrix = m_utils.init_matrix(max_amount_of_elements, max_capacity)
		return resulting_matrix

	def fill_matrix(self, matrix, max_amount_of_elements, current_element_income, current_element_weight):
		for current_element_quantity in range(0, max_amount_of_elements):
			current_max_position = 0
			for current_container_capacity in range(0, self.max_capacity):
				if current_element_quantity*current_element_weight <= current_container_capacity:
					matrix[current_element_quantity][current_container_capacity] = current_element_income * current_element_quantity + self.last_maximun_column[current_max_position][self.__VALUE]
					current_max_position += 1
		return matrix

	def set_last_maximun_column(self, matrix):
		for row in range(0, len(matrix)):
			max_value = max(matrix[row])
			self.last_maximun_column[row][self.__VALUE] = max_value
			value_index = matrix[row].index(max_value)
			self.last_maximun_column[row][self.__INDEX] = value_index


	def fuse_matrix_with_results(self, matrix):
		for row in range(0, len(matrix)):
			matrix[row] += self.last_maximun_column[row]

	def get_result_detail(self):
		amount_of_tables = len(self.result) - 1
		current_table = self.result[amount_of_tables]
		current_xi = m_utils.get_maximun_element_from_column(current_table, len(current_table[0])-2)
		current_element_quantity = current_table[current_xi[0]][len(current_table[0])-1]
		result = [current_element_quantity]
		current_xi_index = current_xi[0]
		for actual_index in range(1, (amount_of_tables + 1)):
			current_table_index = amount_of_tables - actual_index
			current_table = self.result[current_table_index]
			current_xi_index = self.get_xi(current_xi_index, result[actual_index-1], actual_index)
			current_element_quantity = current_table[current_xi_index][len(current_table[0])-1]
			result += [current_element_quantity]
		return result


	def get_xi(self, current_xi, current_mi, current_element):
		current_element_weight = self.info[self.__WEIGHT][current_element-1]
		return current_xi - current_element_weight * current_mi

	def print_pretty_result(self):
		amount_of_tables = len(self.result) - 1
		for suggested_table_index in range(0, amount_of_tables + 1):
			current_table_index = amount_of_tables - suggested_table_index
			current_table = self.result[current_table_index]
			#print("CT", current_table)
			self.print_table_header(len(current_table[0])-2, suggested_table_index + 1)
			m_utils.print_matrix(current_table)
		print("Resultado:")
		result = self.get_result_detail()
		for actual in range(0, len(result)):
			print("Del artículo", actual+1, "coloque:", result[actual])

	def print_table_header(self, m_quantity, actual_index):
		for element_index in range(0, m_quantity):
			print("|\tm", element_index, end="\t")
		print("|   f",actual_index, "( x",actual_index,")", "|\tm",actual_index,"*\t|")



