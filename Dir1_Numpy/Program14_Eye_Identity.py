#Complex numbers
# 2+i5 -> Here 2: real part,i5 imaginary part

#identity matrix - DIAGONAL ELEMENTS MUST BE 1 & No.of rows and columns same ex:3*3,4*4

# [1,0,0]
# [0,1,0]
# [0,0,1]

import numpy as np
matrix=np.eye(3,dtype=int)
print(matrix)

matrix=np.eye(3,3,dtype=int)  #eye
print(matrix)

matrix=np.identity(2,dtype=int)   #identity
print(matrix)