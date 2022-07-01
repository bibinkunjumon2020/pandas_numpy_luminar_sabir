import pandas as pd

file=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=None)
file.columns=['id','fname','lname','age','prof','loc']
#print(file)

#Filtering data
data1=file.loc[file['age']==25] # prints all details of persons with age = 25
#print(data1)
print("#####")
#print(file['age']) # Success prints all ages
# print(file.loc['age']) - Not possible error

data2=file.loc[file['loc']=='india'] # Filter all works in india
#print(data2)

data3=file.loc[file['loc']=='india'] [['fname','lname','age','prof']]# Filter all works in india but only their given Key values
#print(data3)
data4=file.loc[(file['age'] > 40) & (file['loc']=='india')] # To apply 2 condition use '(' - It is must
print(data4)
