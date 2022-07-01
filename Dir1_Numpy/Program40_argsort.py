import numpy as np

arra1=np.array([6,3,8,9,1,7,2])
print(np.sort(arra1))
print(np.argsort(arra1))

matrix=np.array([[1,2,3],[4,2,6],[6,7,9]])
print(matrix)
print(np.sort(matrix,axis=1)) #Sort elements in row wise
print(np.argsort(matrix,axis=1))  #Index of sorted elements