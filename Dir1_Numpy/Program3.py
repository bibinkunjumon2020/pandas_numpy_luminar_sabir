#creating 3D array

import numpy as np
my_array=np.array([[[1,2,3],[3,4,5],[4,6,7]]])   # We must use [ to get 3D matrix if '(' given only 2D possible
print(my_array)
print(my_array.ndim)  #ANS= 3D
print("Order",my_array.shape) # Ans= (1,3,3) = (z,x,y)
print("Size = ",my_array.size)