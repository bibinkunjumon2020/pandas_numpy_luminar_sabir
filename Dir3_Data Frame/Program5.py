import pandas as pd
#dfname=pd.read_csv("path")
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=None)
print(data)
#data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=[['id','fname','lname','age','prof','loc']]) -> Its not Possible

data.columns=['id','fname','lname','age','prof','loc']
print(data)

data_1=data.rename(columns={'lname':'last_Name'})  #Changing the column title
print(data_1)