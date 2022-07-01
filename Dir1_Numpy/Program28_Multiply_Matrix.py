import numpy as np
matrix1=np.reshape(np.arange(10,19),[3,3])
matrix2=np.reshape(np.arange(20,29),[3,3])
matrix3=np.reshape(np.arange(80,89),[3,3])
print(matrix1,"\n ","******\n",matrix2,"\n*******\n",matrix3)
#Multiply 2 matrix
print("Result = ",np.multiply(matrix1,matrix2))
#Multiply element with matrix
print(np.multiply(matrix1,2))
# We get element by element mult
print(matrix1*matrix2)