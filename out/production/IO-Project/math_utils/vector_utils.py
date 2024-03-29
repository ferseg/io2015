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
