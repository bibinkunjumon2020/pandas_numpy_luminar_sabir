import numpy as np
matrix=np.reshape(np.arange(0,15),[5,3])
print(matrix)

#sum of each row                    # Remember we use sum from np library...otherwise wrong output
print("Row Sum = ",np.sum(matrix,axis=1))
#Sum 0f column
print("Column Sum= ",np.sum(matrix,axis=0))

#SUm of Whole matrix

print("Sum Matrix=",np.sum(matrix))