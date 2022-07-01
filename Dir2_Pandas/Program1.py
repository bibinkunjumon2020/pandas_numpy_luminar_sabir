
import pandas as pd


#Series
s=pd.Series(["hai",12,56,5,4,4,4,3,6,8,23,56,78]) # data type is :object(since string is there)
#print(s)
print(type(s))  #type is panda series
print(s.shape)
print(s.size)
print(s.head())  #First 5 elements/rows
print(s.tail())  # Last 5 elements/rows

print(s.head(3))  #First n elements/rows
print(s.tail(10))  # Last n elements/rows