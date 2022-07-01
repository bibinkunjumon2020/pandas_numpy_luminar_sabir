import numpy as np
# 2 *2 matrix dot product
matrix=np.arange(0,4).reshape([2,2])
matrix2=np.array([7,8])
print(matrix,"\n",matrix2)

"""
             0 1         --->  7*0+8*2     7*1+8*3      --> [ 16 31 ]      
[7,8]        2 3                

"""

# Very careful about the order --- Answer is different

print(np.dot(matrix2,matrix))

"""
0 1                     0*7+1*7    0*8+1*8    ---> [ 7  8 ]  It wont use 2nd row since no 2nd row in 2nd matrix
2 3      7 8   -->  

"""
print(np.dot(matrix,matrix2))