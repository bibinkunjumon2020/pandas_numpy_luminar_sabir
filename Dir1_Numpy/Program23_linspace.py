#linspace (arg1-starting number/arg2-ending number/arg3-How many equal division - decimal also get as o/p
#default is float. I can covert to int using dtype
import numpy
my_array=numpy.linspace(1,100,10)
print(my_array)

my_array1=numpy.linspace(1,100,11)
print(my_array1)

my_array2=numpy.linspace(1,100,13)
print(my_array2)
print(my_array2.size)

my_array3=numpy.linspace(1,100,13,dtype=int)
print(my_array3)
print("*"*100)
#if no arg3 then default is 50
my_array4=numpy.linspace(1,20)
print(my_array4.size)