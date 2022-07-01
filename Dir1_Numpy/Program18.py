#Order(shape) of an array change -> (3,4) to (4,3) ->reshape
import numpy as np
matrix=np.array([[1,2,3,4],[2,3,4,5],[4,6,7,8]])
print(matrix)
print(matrix.shape)
print(matrix.ndim)

print("*"*100)
new_metrix=np.reshape(matrix,[4,3])
print(new_metrix)

# SIze of matrix must be same (6,2)(3,4)

print("*"*100)
new_metrix=np.reshape(matrix,[2,6])
print(new_metrix)

print("*"*100)
new_metrix=np.reshape(matrix,[6,2])
print(new_metrix)


#new_metrix=np.reshape(matrix,[2,5])  --> Error size not same

new_metrix=np.reshape(matrix,12)  # its for creating a single row matrix..so here only 12 works
print(new_metrix)

#flatten  # flatten - to convert any array into a 1 D array
print("*"*100)
new_metrix=matrix.flatten()
print(new_metrix)