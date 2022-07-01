# flatten - to convert any array into a 1 D array
import numpy

matrix=numpy.array([[1,2,3],[2,3,4],[5,6,7],[8,5,4]])
print(matrix)
print(matrix.ndim)
print(matrix.shape)
new_matrix=matrix.flatten()
print(new_matrix)
print(new_matrix.shape,new_matrix.ndim)

new_matrix2=matrix.reshape(12)
print(new_matrix2)
print("*"*40)
print(new_matrix2.shape,new_matrix2.ndim)