#a range creating an 1 D array of

import numpy
matrix=numpy.arange(10)
print(matrix)
print(matrix.size)

matrix2=matrix.reshape([2,5])
print(matrix2)
print(matrix.ndim)

matrix3=numpy.arange(2,11) # 2- lowe range, 11-1 upper range
print(matrix3)