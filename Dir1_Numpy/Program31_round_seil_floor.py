import numpy
import numpy as np

my_array=numpy.array([[1.2,3.5,5.6],[5.7,3.4,8.9],[4.3,6.8,9.7]])
print(my_array)

#Floor Ceil Round

#Floor - number made as integer -decimal left : No rounding decimal disappeared

#9.7->9 , 6.8->6

print(np.floor(my_array))

# Ceil - number made as integer -decimal left : ecimal disappeared  and mapped to next integer Its not rounding

#9.7->10 , 6.8->7 2.1 -> 3
print(np.ceil(my_array))

# Here actual rounding happens : Decimal disappears - Rounding : Above >2.5 - 3(HIGH)  <2.5 - 2(LOW)
#2.5 mapped to nearest even number ie: 3.5 ->4 / 4.5->4
print(np.round(my_array))