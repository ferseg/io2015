__author__ = 'fsegovia'

import math_utils as m_utils

class Simplex:
    """
    Solves Simplex Algorithm
    """

    __OBJECTIVE_FUNCTION_INDEX = 0
    __FIRST_INDEX = 0
    __NONE = -1
    __UNBOUNDED = 0
    __ONE_SOLUTION = 1
    __DEGENERATE = 2
    __SOLUTIONS = ["No acotada", "Una solución", "Degenerada"]

    def __init__(self, matrix, variable_quantity, p_type=True):
        self.matrix = matrix
        self.variable_quantity = variable_quantity
        self.solution_type = self.__NONE
        self.type = p_type

    def set_matrix(self, matrix):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    def start_simplex(self):
        last_selected = []
        last_selected_attempts = 0
        while not self.is_optimus_solution() and not self.is_unbounded_solution() and last_selected_attempts < 5:
            pivot_column_index = self.__get_pivot_column_index()
            pivot_column = self.get_column(pivot_column_index)
            pivot_row_index = self.get_pivot_row_index(pivot_column)
            new_pivot_row = self.modify_pivot_row(self.matrix[pivot_row_index], pivot_column_index)
            if new_pivot_row == last_selected:
                last_selected_attempts += 1
            else:
                last_selected = new_pivot_row
                last_selected_attempts = 0
            self.matrix[pivot_row_index] = new_pivot_row
            self.change_table(pivot_row_index, pivot_column_index)
            m_utils.print_matrix(self.matrix)
        if self.is_unbounded_solution() or last_selected_attempts == 5:
            self.solution_type = self.__UNBOUNDED
        # If not set before, the it's a one solution problem
        elif self.solution_type == self.__NONE or self.is_optimus_solution():
            self.solution_type = self.__ONE_SOLUTION
        #return self.get_result()
        self.print_pretty_result()

    def get_result(self):
        """
        Gets the result of the simplex method evaluation when the solution is not unbounded
        :return:
        """
        result = [0]*self.variable_quantity
        values = self.__get_values()
        for actual_constraint in range(1, len(self.matrix)):
            for index in range(0, self.variable_quantity):
                actual_constraint_variable = self.matrix[actual_constraint][index]
                if actual_constraint_variable == 1:
                    column = self.get_column(index)
                    appearences = m_utils.count_appearences_in_array(1, column)
                    if appearences == 1:
                        result[index] = values[actual_constraint-1]
        fo = self.matrix[self.__OBJECTIVE_FUNCTION_INDEX]
        result += [fo[len(fo)-1]]
        return result


    def get_pivot_row_index(self, pivot_column):
        """
        gets the pivot row
        :return: the pivot row
        """
        result_values = self.__get_values()
        division = m_utils.division
        values_with_division = m_utils.exec_function_in_each_position(result_values, pivot_column, division)
        row_index = self.__get_index_of_min_value(values_with_division) + 1
        return row_index

    def get_column(self, column_index):
        """
        Gets the values in the column_index of a given array
        :param column_index: the index of the column
        :return: the values in the pivot column index, of each restriction
        """
        result = []
        for actual_index in range(1, len(self.matrix)):
            result.append(self.matrix[actual_index][column_index])
        return result

    def modify_pivot_row(self, array, pivot_column_index):
        reference_value = array[pivot_column_index]
        if reference_value != 0:
            for index in range(0, len(array)):
                array[index] /= reference_value
                array[index] = round(array[index], 2)
        return array

    def modify_normal_row(self, column_index, old_row, pivot_row):
        reference_number = old_row[column_index]
        row_to_subtract = m_utils.multiply_number_by_vector(reference_number, pivot_row)
        return m_utils.subtract_vectors(old_row, row_to_subtract)

    def change_table(self, row_index, column_index):
        pivot_row = self.matrix[row_index]
        for index in range(0, len(self.matrix)):
            if index != row_index:
                actual_row = self.matrix[index]
                result_row_after_change = self.modify_normal_row(column_index, actual_row, pivot_row)
                self.matrix[index] = result_row_after_change

    def is_optimus_solution(self):
        """
        Indicates that the actual solution is the optimus
        :return:
        """
        fo = self.matrix[self.__OBJECTIVE_FUNCTION_INDEX]
        multiplier = 1 if self.type else - 1
        for index in range(0, len(fo)):
            if multiplier * fo[index] < 0:
                return False
        return True

    def is_unbounded_solution(self):
        values = self.__get_values()
        for index in range(0, len(values)):
            if values[index] > 0:
                return False
        return True

    def __get_pivot_column_index(self):
        """
        gets the index of the pivot column
        :return: the index of the pivot column
        """
        fo = self.matrix[self.__OBJECTIVE_FUNCTION_INDEX]
        # Gives the priority to the variables
        variables = fo[0:self.variable_quantity]
        min_value_index = self.__get_index_of_min_value(variables)
        if variables[min_value_index] >= 0:
            clearances = fo[self.variable_quantity:]
            # We must add the variable quantity to the index to get the current value in the objective function
            min_value_index = self.__get_index_of_min_value(clearances) + self.variable_quantity
        return min_value_index

    def __get_index_of_min_value(self, array):
        """
        Gets index of the minimum value in an array
        :param array:
        :return: the index of the minimum value
        """
        low = array[self.__FIRST_INDEX]
        pivot_index = 0
        for index in range(1, len(array)):
            actual = array[index]
            if actual < low:
                low = actual
                pivot_index = index
        return pivot_index

    def __get_values(self):
        index = len(self.matrix[self.__FIRST_INDEX]) - 1
        return self.get_column(index)

    def print_pretty_result(self):
        result = self.get_result()
        last_index = len(result)-1
        for i in range(0, last_index):
            print("x", i+1, "=", result[i])
        print("Solución: ", result[last_index], self.__SOLUTIONS[self.solution_type])


