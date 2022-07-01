import pandas as pd
data=pd.read_csv(("/Users/bibinkunjumon/Documents/customer.txt"),names=['id','fname','lname','age','prof','loc'])
print(data.isna().sum()) #Counting missing fields

#To fill empty fields with our content
data2=data.fillna('Null')
print(data2.isna().sum())

#To drop empty fielded items
data3=data.dropna()
print(data3.isna().sum())

data.dropna(inplace=True)  # To replace a dataframe by leaving nulls
data.fillna(20,inplace=True)

print(data.isna().sum())

data['loc'].fillna('Kerala',inplace=True)  # To fill a particular column missing value with our choice
print(data)
data['prof'].fillna('OOmb',inplace=True)
print(data)