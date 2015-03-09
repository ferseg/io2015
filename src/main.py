__author__ = 'fsegovia'

# Testing


import math_utils as leu
import simplex as si


#res = leu.intersections([[2, 5], [7, -3], [3, 3]])

#mult_vector = leu.multiplicar_numero_x_vector(2, [1, 1/2, 1/2, 1/2, 0, 0, 0, 90])
#print(mult_vector)
#res2 = leu.restar_vectores([2,1,2,0,0,1,0,240], mult_vector)

simp = si.Simplex([1])

mat = [[-1,-1,-2,0,0,0,0],[2,1,1,1,0,0,50], [2,1,0,0,-1,0,36], [1,0,1,0,0,-1,10]]
simp.set_matrix(mat)
print(simp.modify_pivot_row(mat[simp.get_pivot_row_index()]))




