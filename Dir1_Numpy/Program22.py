import numpy
matrix1=numpy.arange(20,61,4) # Increment
print(matrix1)
matrix=numpy.arange(100,61,-4) # Decrement
# arange arg1- start range/2nd arg-upper range-1/arg3-increment
print(matrix)

# 10 to 60 array - even numbers -> matrix of 13*2
array2 = numpy.arange(10, 61, 2) #Increment
print(array2)

matrix3 = numpy.reshape(array2, [13, 2])
print(matrix3)
