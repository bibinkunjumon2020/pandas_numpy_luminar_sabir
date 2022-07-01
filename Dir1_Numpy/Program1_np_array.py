#Numpy in array - (ML class 4 March Batch)

#Create array using numpy

import numpy as np

a=np.array([1,2,3])
print(a)

print(type(a))  #  ---- Class in an 'n' dimentional array Class 'ndarray'



#Order of a Matrix
#[1,2,3]
#[5,6,7]  Order of this matrix is - 2*3 (2 rows and 3 colmns)

#Dimention - in numpy dimentions are called axes
#ndim - to print dimention

print(a.ndim)

b=np.array([[1,2,3],[4,5,6]]) # or np.array(([1,2,3],[4,5,6]))

#here the order of array is 2*3 and Dimention is 2(2 outer brackets)

print(b)
print(b.ndim)

c=np.array(([1,2,3],[4,5,6],[7,8,9]))  # Here also oder is 3*3 but dimention is 2
print(c)
print(c.ndim)
print("size = ",c.size)