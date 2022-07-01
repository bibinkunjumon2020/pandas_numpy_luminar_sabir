import numpy as np
# 2 *2 matrix dot product
matrix=np.arange(0,4).reshape([2,2])
matrix2=np.array([[7,8],[10,11]])
print(matrix,"\n",matrix2)

"""
0 1        7   8
2 3       10  11  

dot product = 0*7 + 1*10     0*8 + 1*11   --->   10   11
              2*7 + 3*10     2*8 + 3*11          44   49
"""


print(np.dot(matrix,matrix2))