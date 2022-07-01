import numpy as np

matrix=np.ones([4],dtype=int)  #1D
print(matrix)
print(matrix.ndim,"D")
print(matrix.shape)

print("*****")
matrix=np.ones([3,4],dtype=int) #2D
print(matrix)

print(matrix.ndim,"D")
print(matrix.shape)
print("--------------")
matrix=np.ones([2,3,4],dtype=int) #3D
print(matrix)

print(matrix.ndim,"D")
print(matrix.shape)