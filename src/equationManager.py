import operator

OPERATORS = {
            '<=': operator.le,
            '>=': operator.ge,
            }

def eval_intersections(functions,intersections):
    temp=[]
    for i in intersections:
        x=i[0]
        y=i[1]
        for j in functions:
            break
        print(":O!")
    return

def eval_function(function,variable):
    return eval(function)

def eval_expression(op,val1,val2):
    return get_operator(op)(val1,val2)

def get_operator(op):
    return OPERATORS[op]

#eval_intersections(["","",""],[[1,1],[1,1]])
