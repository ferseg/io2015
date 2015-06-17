import math_utils as m_utils

class Replacement:
	"""docstring for Replacement"""

	__INCOME = 0
	__OPERATION_COST = 1
	__RETURNIG_VALUE = 2

	def __init__(self, data_table, actual_usage_years, years_of_politics, 
		min_replacement_years, max_replacement_years, machine_total_cost):
		self.data_table = data_table
		self.actual_usage_years = actual_usage_years
		self.years_of_politics = years_of_politics
		self.min_replacement_years = min_replacement_years
		self.max_replacement_years = max_replacement_years
		self.machine_total_cost = machine_total_cost
		self.result = []

	def solve(self):
		stages = self.get_stages()
		for index in range(0, self.years_of_politics):
			actual_stage = self.years_of_politics - (index + 1)
			times_in_stage = self.get_times_in_stage(stages, actual_stage)

			result = []
			if index != 0:
				result = self.get_first_keep_and_replace_value_for_all_times(times_in_stage, index)
			else:
				result = self.get_first_keep_and_replace_value_for_all_times_first(times_in_stage)
			self.result += [result]
			print("RES", result)

	def get_stages(self):
		stages = self.get_stages_aux(self.min_replacement_years, self.max_replacement_years, self.years_of_politics, self.actual_usage_years)
		stages = self.delete_repeated_elements(stages)
		return sorted(stages)
		
	def get_stages_aux(self, min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years):
		if years_of_politics == 0:
			return []
		elif actual_usage_years >= min_replacement_years and actual_usage_years < max_replacement_years:
			return self.keep(min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years) + self.replace(
				min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years)
		elif actual_usage_years < max_replacement_years:
			return self.keep(min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years)
		else:
			return self.replace(min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years)

	def keep(self, min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years):
		return [[self.years_of_politics - years_of_politics, actual_usage_years]] + self.get_stages_aux(
			min_replacement_years, max_replacement_years, years_of_politics - 1, actual_usage_years + 1)

	def replace(self, min_replacement_years, max_replacement_years, years_of_politics, actual_usage_years):
		return [[self.years_of_politics - years_of_politics, actual_usage_years]] + self.get_stages_aux(
			min_replacement_years, max_replacement_years, years_of_politics - 1, 1)

	def delete_repeated_elements(self, array):
		result = []
		while array != []:
			actual_element = array[0]
			if actual_element not in result:
				result += [actual_element]
			array = array[1:]
		return result

	def get_times_in_stage(self, stages, current_stage):
		result = []
		for actual in range(0, len(stages)):
			actual_stage = stages[actual]
			if actual_stage[0] == current_stage:
				result += [[actual_stage[1]]]
		return result

	def get_first_keep_and_replace_value_for_all_times(self, times_in_stage, actual_stage):
		res_bef = self.result[actual_stage - 1]
		r0 = self.data_table[0][self.__INCOME]
		c0 = self.data_table[0][self.__OPERATION_COST]
		f1 = res_bef[0][len(res_bef[0])-1]
		for actual in range(0, len(times_in_stage)):
			current_time = times_in_stage[actual]
			times_in_stage[actual] += [self.get_normal_keep_value(current_time, res_bef)]
			times_in_stage[actual] += [self.get_normal_replace_value(current_time, r0, c0, f1)]
			times_in_stage[actual] += m_utils.get_maximun_element_from_array(times_in_stage[actual])
		return times_in_stage

	def get_first_keep_and_replace_value_for_all_times_first(self, times_in_stage):
		for actual in range(0, len(times_in_stage)):
			current_time = times_in_stage[actual]
			times_in_stage[actual] += [self.get_first_keep_value(current_time)]
			times_in_stage[actual] += [self.get_first_replace_value(current_time)]
			times_in_stage[actual] += m_utils.get_maximun_element_from_array(times_in_stage[actual])
		return times_in_stage

	def get_first_keep_value(self, time):
		current_time = time[0]
		if current_time < self.max_replacement_years:
			current_data_row = self.data_table[current_time]
			return current_data_row[self.__INCOME] + self.data_table[current_time + 1][self.__RETURNIG_VALUE] - current_data_row[self.__OPERATION_COST]
		else:
			return 0

	def get_first_replace_value(self, time):
		current_time = time[0]
		if current_time >= self.min_replacement_years:
			current_data_row = self.data_table[current_time]
			return self.data_table[0][self.__INCOME] + current_data_row[self.__RETURNIG_VALUE] + self.data_table[
				1][self.__RETURNIG_VALUE] - self.data_table[0][self.__OPERATION_COST] - self.machine_total_cost
		else:
			return 0

	def get_normal_keep_value(self, time, res_bef):
		current_time = time[0]
		if current_time < self.max_replacement_years:
			real_index = m_utils.find_index_row_of_element_in_matrix(res_bef, 0, current_time)
			current_data_row = self.data_table[current_time]
			rt = current_data_row[self.__INCOME]
			ct = current_data_row[self.__OPERATION_COST]
			real_index = m_utils.find_index_row_of_element_in_matrix(res_bef, 0, current_time + 1)
			ft1 = res_bef[real_index][len(res_bef[0])-1]
			return rt - ct + ft1

	def get_normal_replace_value(self, time, r0, c0, f1):
		current_time = time[0]
		if current_time >= self.min_replacement_years:
			current_data_row = self.data_table[current_time]
			st = current_data_row[self.__RETURNIG_VALUE]
			return r0 + st - c0 - self.machine_total_cost + f1

