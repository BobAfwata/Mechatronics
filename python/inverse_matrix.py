#!/usr/bin/env python 

# wap to  a) calculate the determinant of the matrix
matrix_a = [[3,1],
            [4,2]]

matrix_b = [[3,2],
            [6,4]]

"""
    [0][0] =a  [0][1] = b
    [1][0] =c   [1][1] = d
"""

det_a = (matrix_a[0][0] * matrix_a[1][1]) -  (matrix_a[0][1] * matrix_a[1][0])  

det_b = (matrix_b[0][0] * matrix_b[1][1]) - (matrix_b[0][1] * matrix_b[1][0])  

#(3*2) - ( 4* 1)
print(det_a)

#b calculate the inverse of the matrix 

inv_a = [[0,0],
         [0,0]]



inv_a[0][0] = 1/det_a * matrix_a[1][1]
inv_a[0][1] = -1/det_a * matrix_a[0][1]
inv_a[1][0] = -1/det_a * matrix_a[1][0]
inv_a[1][1] = 1/det_a * matrix_a[0][0]


inv_b = [[0,0],[0,0]]

"""
inv_b[0][0] = 1/det_b * matrix_b[1][1]
inv_b[0][1] = -1/det_b * matrix_b[0][1]
inv_b[1][0] = -1/det_b * matrix_b[1][0]
inv_b[1][1] = 1/det_b * matrix_b[0][0]

"""




print(inv_a)
print(inv_b) # no inverse 

