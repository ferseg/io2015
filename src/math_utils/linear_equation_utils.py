import operator

OPERATORS = {
            '<=': operator.le,
            '>=': operator.ge,
            '=': operator.eq,
            }
X_VALUE = 0
Y_VALUE = 1
ROUND_VALUE = 9
LAST_VALUE = -1
OPERATOR_VALUE = 2

def eval_intersections(inequations,intersections):
    temp=[]
    for i in intersections:
        x = i[X_VALUE]
        y = i[Y_VALUE]
        validity = True
        for j in inequations:
            value = (x * j[X_VALUE]) + (y * j[Y_VALUE])
            validity = eval_expression(j[OPERATOR_VALUE],value,j[LAST_VALUE])
            if validity == False:
                break
        if validity:
            temp += [i]
    return temp

def eval_expression(op,val1,val2):
    return get_operator(op)(round(val1,ROUND_VALUE),round(val2,ROUND_VALUE))

def get_operator(op):
    return OPERATORS[op]


SLOPE_INDEX = 0
CONSTANT_INDEX = 1


# Returns the intersection in x between two straights
def intersection_in_x(m1, b1, m2, b2):
    difference_between_slopes = m1 - m2
    if difference_between_slopes != 0:
        return (b2 - b1) / difference_between_slopes
    else:
        return -1


# Returns the value of "y" given a specified "x"
def intersection_in_y(m, x, b):
    return m*x+b


# Calculates all the intersections between straights
# @param list_of_straights A list of straights
# @return all the intersections between the straights. e.j. [[2.0, 4.0], [2.4, 5.3]]
# @details The form of the parameter is [[m1,b1], [m2,b2], ... ,[mn, bn]]
def intersections(list_of_straights):
    result = []
    while len(list_of_straights) > 1:
        reference_pair = list_of_straights[0]
        # The reference pair must evaluate its intersections with the other pairs
        # but not with himself
        list_of_straights = list_of_straights[1:]
        reference_pair_intersections = get_intersections_of_a_straight(reference_pair, list_of_straights)
        result += reference_pair_intersections
    return result


# Calculates the intersection of a straight with an array of other straights
# @param reference_pair the pair that needs to know their intersections
# @param list_of_straights a list of straights
# @return the intersections between the reference_pair with the list_of_straights
def get_intersections_of_a_straight(reference_pair, list_of_straights):
    result = []
    reference_slope = reference_pair[SLOPE_INDEX]
    reference_constant = reference_pair[CONSTANT_INDEX]
    for pair_index in range(0, len(list_of_straights)):
        actual_pair = list_of_straights[pair_index]
        actual_slope = actual_pair[SLOPE_INDEX]
        actual_constant = actual_pair[CONSTANT_INDEX]
        x_intersect = intersection_in_x(reference_slope, reference_constant, actual_slope, actual_constant)
        y_intersect = intersection_in_y(reference_slope, x_intersect, reference_constant)
        result.append([x_intersect, y_intersect])
    return result
