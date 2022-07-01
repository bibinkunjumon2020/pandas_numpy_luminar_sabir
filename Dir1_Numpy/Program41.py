import numpy as np
matrix=np.array([[1,2,3],[4,2,6],[6,7,9]])
print("Maximum",np.max(matrix))
print("Maximum Row : ",np.max(matrix,axis=1))
print("Maximum Column : ",np.max(matrix,axis=0))

print("Maximum",np.argmax(matrix))
print("Maximum Row : ",np.argmax(matrix,axis=1))
print("Maximum Column : ",np.argmax(matrix,axis=0))

print("Min : ",np.min(matrix))
print("Min Row",np.min(matrix,axis=1))
print("Min Column : ",np.min(matrix,axis=0))

print("Min : ",np.argmin(matrix))
print("Min Row",np.argmin(matrix,axis=1))
print("Min Column : ",np.argmin(matrix,axis=0))

