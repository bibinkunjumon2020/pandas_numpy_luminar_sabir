import numpy as np
matrix=np.array([[5,4,3],[4,1,6],[6,3,9],[1,7,4]])
print("Source Matrix\n",matrix)
print("Row wise Sorting\n",np.sort(matrix))
print("Sort Axis=1\n",np.sort(matrix,axis=1))
print("Sort Axis=0/Column sorting\n",np.sort(matrix,axis=0))

print("Sort Axis=0/Column sorting\n",np.sort(matrix,0)) #Here axis missing but no error


print("Sort Axis=None/Output 1 D array in ascending order\n",np.sort(matrix,axis=None))