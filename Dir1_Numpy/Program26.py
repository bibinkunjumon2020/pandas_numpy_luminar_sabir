import numpy as np
# Order of the matrix must be same
matrix1=np.reshape(np.arange(10,19),[3,3])
matrix2=np.reshape(np.arange(20,29),[3,3])
matrix10=np.reshape(np.arange(80,89),[3,3])
print(matrix1,"\n ","*"*100,"\n",matrix2,"\n*******\n",matrix10)

#Addition of 2 matrix

matrix3=matrix1+matrix2
print(matrix3)

matrix4=np.add(matrix1,matrix2)
print(matrix4)

# Adding 3 matrix
print(matrix1+matrix10+matrix2) # Here we get correct output for n number of matrix

# But

print(np.add(matrix1,matrix2,matrix10)) # Here we wont get correct answer-only 2 args are added here.So...

matrix5=np.add(matrix1,matrix2)
matrix6=np.add(matrix5,matrix10)
print(matrix6)
