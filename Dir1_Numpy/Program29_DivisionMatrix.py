import numpy as np
matrix1=np.reshape(np.arange(10,19),[3,3])
matrix2=np.reshape(np.arange(20,29),[3,3])
matrix3=np.reshape(np.arange(80,89),[3,3])
print(matrix1,"\n ","******\n",matrix2,"\n*******\n",matrix3)

# Division 2 matrix
print("Result = ",np.divide(matrix1,matrix2))

# Division 1 matrix by a specific number
print(np.divide(matrix1,2))

# True Division of 2 matrix - It gives clear value that is float.
print(np.true_divide(matrix2,matrix1))
# True Division 1 matrix by a specific number- It gives clear value that is float.
print(np.true_divide(matrix1,2))
# Floor Division of 2 matrix - It gives integer values..decimal part gone
print(np.floor_divide(matrix2,matrix1))

# Floor Division 1 matrix by a specific number-- It gives integer values..decimal part gone
print(np.floor_divide(matrix2,4))
