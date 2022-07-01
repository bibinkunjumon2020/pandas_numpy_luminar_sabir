import numpy as np

matrix1=np.arange(0,9).reshape((3,3))
print(matrix1)

#Square of each element in matrix

matrix2=np.square(matrix1)
print("Square = \n",matrix2)
#Square Root of each element in matrix
print("Square Root = \n",np.sqrt(matrix1))

"""
sin cos tan exp log

"""

print("Sin :",np.sin(0))
print("Cos :",np.cos(0))
print("Tan :",np.tan(0))
print("Log = ",np.log(1))