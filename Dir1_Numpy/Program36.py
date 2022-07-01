import numpy as np

matrix=np.array([[3,2,5],[6,9,3],[7,5,2]])
#print(matrix)
sum1=np.sum(matrix)
#print(sum1)
"""
3 2 5
6 9 3
7 5 2

axis=0 Column
axis=1 Row

"""
b=np.sum(matrix,axis=0) # We get o/p an array of sums of each column
print(b)

c=np.sum(matrix,axis=1) # We get o/p an array of sums of each row
print(c)
