#!/usr/bin/env python

# Matrix multiplication using lists

# A * B = 
# A inverse  
# Dot Product ,Cross Product


# list of a list 
numbers = [1,2,3]
matrix_A = [[1,2,3],[4,5,6],[7,8,9]]

# R C 
matrix_a = [[1, 2],  
            [3, 4]]

matrix_b = [[5, 6], 
            [7, 8]]

result = [[0, 0], 
          [0, 0]]


#  [i ,0]      [0,j]

for i in range(2):
    for j in range(2):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j] +
                        matrix_a[i][1] * matrix_b[1][j])

for row in result:
    print(row)

