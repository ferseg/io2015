__author__ = 'fsegovia'

# Testing


import math_utils as leu
import simplex as si


simp = si.Simplex([1], 2)

#mat = [[-1,-1,-2,0,0,0,0],[2,1,1,1,0,0,50], [2,1,0,0,-1,0,36], [1,0,1,0,0,-1,10]]
mat = [[-3, -2, 0, 0, 0, 0], [2, 1, 1, 0, 0, 18], [2, 3, 0, 1, 0, 42], [3, 1, 0, 0, 1, 24]]
simp.set_matrix(mat)
print(simp.start_simplex())
print(simp.get_matrix())




