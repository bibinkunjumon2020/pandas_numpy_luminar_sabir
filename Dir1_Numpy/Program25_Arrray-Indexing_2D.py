import numpy as np
#matrix=np.array([[1,2,3,4],[5,6,7,8],[8,3,5,7]])
#print(matrix)
#print(matrix.shape,matrix.ndim)

#matrix=np.arange(4,16).reshape(3,4) # This also right
matrix1=np.reshape(np.arange(4,16),[3,4]) #this is also right
print(matrix1,"\n",matrix1.size,matrix1.shape)

print(matrix1[1,2]) # print element in index [1][2] row -2 column 3
print(matrix1[0,0]) #print element of [0][0] or the first element
print(matrix1[:2,:3])
print("*"*100)
print(matrix1[0:2,1:3]) #row from 0 to 2 column from 1 to 3-1
print(matrix1[0:3,0:3]) # Rows & column from 0 to 3-1

print(matrix1[:,:3])#all rows,column 0 to 3-1
print(matrix1[:,0])#entire 1st column
print(matrix1[0,:])#Entire 1st row

print(matrix1[-1,-3]) # negative index
