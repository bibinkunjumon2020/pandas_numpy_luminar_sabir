import pandas as pd

file=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=None)

file3=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=None,sep=',') #how we are seperating data may be space,comma..etc
file.columns=['id','fname','lname','age','prof','loc']
print(file.iloc[5:151:5] [['fname','lname','age','loc']])

print(file.isna().sum()) # To find sum of missing values in any columns ' is null?'

file1=file.fillna(0)#Can give any value in the null place
print(file1.isna().sum())
