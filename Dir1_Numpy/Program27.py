import numpy as np
matrix1=np.reshape(np.arange(10,19),[3,3])
matrix2=np.reshape(np.arange(20,29),[3,3])
matrix3=np.reshape(np.arange(80,89),[3,3])
print(matrix1,"\n ","******\n",matrix2,"\n*******\n",matrix3)
#Order must be same
matrix4=np.subtract(matrix1,matrix2)
print("Substraction M1- M2 ::::: \n",matrix4)
print("Substraction M2- M1 ::::: \n",np.subtract(matrix2,matrix1))