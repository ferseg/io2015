__author__ = 'fsegovia'

import math_utils as m_utils

class Simplex:
    """
    Solves Simplex Algorithm
    """

    _OBJECTIVE_FUNCTION_INDEX = 0
    _FIRST_INDEX = 0

    def __init__(self, objective_function):
        self.matrix = [[1] + objective_function]

    def set_matrix(self, matrix):
        self.matrix = matrix

    def get_pivot_row_index(self):
        """
        gets the pivot row
        :return: the pivot row
        """
        # Gets the pivot column index to get the pivot column
        pivot_column_index = self._get_pivot_column_index()
        pivot_column = self.get_column(pivot_column_index)
        result_values = self._get_values()
        division = m_utils.division
        values_with_division = m_utils.exec_function_in_each_position(result_values, pivot_column, division)
        row_index = self._get_index_of_min_value(values_with_division) + 1
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

    def modify_pivot_row(self, array):
        pivot_column_index = self._get_pivot_column_index()
        reference_value = array[pivot_column_index]
        for index in range(0, len(array)):
            array[index] /= reference_value
        return array


    def _get_pivot_column_index(self):
        """
        gets the index of the pivot column
        :return: the index of the pivot column
        """
        fo = self.matrix[self._OBJECTIVE_FUNCTION_INDEX]
        return self._get_index_of_min_value(fo)

    def _get_index_of_min_value(self, array):
        """
        Gets index of the minimum value in an array
        :param array:
        :return: the index of the minimum value
        """
        low = array[self._FIRST_INDEX]
        pivot_index = 0
        for index in range(1, len(array)):
            actual = array[index]
            if actual < low:
                low = actual
                pivot_index = index
        return pivot_index

    def _get_values(self):
        index = len(self.matrix[self._FIRST_INDEX]) - 1
        return self.get_column(index)
