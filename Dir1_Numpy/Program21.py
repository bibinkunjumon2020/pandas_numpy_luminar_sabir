import numpy as np

my_array=np.arange(1,51)  #An array of 1,50
#Method 1
matrix=my_array.reshape([1,10,5]) # reshape into a matrix 10,5
print(matrix)
print(matrix.ndim)

#Method 2
matrix2=np.reshape(my_array,[1,10,5])   # Its 3D  we cannot increase z axis to more than 1
print(matrix2)
print(matrix2.ndim)