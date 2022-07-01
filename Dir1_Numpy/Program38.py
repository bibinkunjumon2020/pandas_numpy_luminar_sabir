import numpy as np

arra1=np.array([6,3,8,9,1,7,2])
print("Original Array",arra1)
print("Sorted Aray",np.sort(arra1))  # Sorting an 1D array ascending order


print("Descending Array",np.sort(arra1)[::-1])  # Descending array
print(" Array Flipped",np.flip(np.sort(arra1)))  # Descending array


