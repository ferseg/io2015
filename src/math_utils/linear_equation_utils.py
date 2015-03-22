import operator

OPERATORS = {
            '<=': operator.le,
            '>=': operator.ge,
            }
X_VALUE = 0
Y_VALUE = 1
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
    print(temp)
    return temp

def eval_expression(op,val1,val2):
    return get_operator(op)(val1,val2)

def get_operator(op):
    return OPERATORS[op]

eval_intersections([[1.0,0.0,">=",0.0],
                    [0.0,1.0,">=",0.0],
                    [1.0, 0.0, '<=', 4.0],
                    [0.0, 1.0, '<=', 4.0]],
                   [[-1,-2],[0,4],[0,0],[4,0],[5,2],[4,4],[5,-1]])
