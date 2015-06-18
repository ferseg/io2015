__author__ = 'fsegovia'


def multiply_number_by_vector(n, vector):
    """

    :param n:
    :param vector:
    :return:
    """
    result = []
    for index in range(0, len(vector)):
        result.append(vector[index] * n)
    return result


def add(a, b):
    return a + b


def deduct(a, b):
    return a - b


# MODIFIED TO USE WITH SIMPLEX
def division(a, b):
    if b > 0:
        return a / b
    return 99999999


def count_appearences_in_array(number, array):
    appearences = 0
    for index in range(0, len(array)):
        if array[index] == number:
            appearences += 1
    return appearences


def exec_function_in_each_position(vector1, vector2, function):
    """

    :param vector1: The first vector
    :param vector2: The second vector
    :param function: Function that will be applied to each index of both vectors
    :return:
    """
    result = []
    for index in range(0, len(vector1)):
        actual_vector_1 = vector1[index]
        actual_vector_2 = vector2[index]
        result.append(function(actual_vector_1, actual_vector_2))
    return result


def add_vectors(vector1, vector2):
    """

    :param vector1:
    :param vector2:
    :return: the sum of the vectors
    """
    sum = add
    return exec_function_in_each_position(vector1, vector2, sum)


def subtract_vectors(vector1, vector2):
    """

    :param vector1:
    :param vector2:
    :return: the subtraction of the vectors
    """
    ded = deduct
    return exec_function_in_each_position(vector1, vector2, ded)


# Matrix
def init_matrix(col_quantity, row_quantity):
        actual_quantity = 0
        result = []
        while actual_quantity < row_quantity:
            new_row = [[0]*col_quantity]
            result += new_row
            actual_quantity+=1
        return result


def transposed(matrix):
    row_len = len(matrix[0])
    col_len = len(matrix)
    result = init_matrix(col_len, row_len)
    for row in range(0, row_len):
        for col in range(0, col_len):
            result[row][col] = matrix[col][row]
    return result

# Deletes a row in a matrix.
# Deletes an element in an array
def delete_row(matrix, rowToBeDeleted):
    return matrix[:rowToBeDeleted] + matrix[rowToBeDeleted+1:]

def delete_element_in_array(array, elementToBeDeleted):
    left = array[:elementToBeDeleted]
    right = array[elementToBeDeleted+1:]
    result = []
    if left != []:
        result += left
    if right != []:
        result += right
    return result

def get_lowest(row):
    result = [-1, 99999999]
    for element in range(0, len(row)):
        actual = row[element]
        if(result[1] > actual):
            result[0] = element
            result[1] = actual
    return result

def get_highest_element_in_matrix(matrix):
    result = [0, 0]
    highest_element = -1
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            actual = matrix[row][col]
            if highest_element < actual:
                highest_element = actual
                result[0] = row
                result[1] = col
    return result

def get_maximun_element_from_column(matrix, column):
    result = [0, 0]
    for row in range(0, len(matrix)):
        current_number = matrix[row][column]
        if result[1] < current_number:
            result[0] = row
            result[1] = current_number
    return result

def get_maximun_element_from_array(array):
    result = [[], 0]
    for index in range(0, len(array)):
        actual = array[index]
        if actual > result[1]:
            result[0] = [index]
            result[1] = actual
        elif actual == result[1]:
            result[0] += [index]
    return result

def find_index_row_of_element_in_matrix(matrix, col, element):
    for index in range(0, len(matrix)):
        current_row = matrix[index]
        if current_row[col] == element:
            return index
    return -1

def print_matrix(matrix):
    for row in range(0, len(matrix)):
        print("|", end="\t")
        for col in range(0, len(matrix[0])):
            print(matrix[row][col], end="\t|\t")
        print("")
    print("\n\t\t---------- END ----------\n")