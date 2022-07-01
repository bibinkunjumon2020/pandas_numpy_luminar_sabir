import pandas as pd
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=None)
data.columns=['id','fname','lname','age','prof','loc']
#print(data)
data2=data.loc[(data['age'] > 50) | (data['loc'] == 'us')]    #Very careful loc and iloc different
#print(data2)

data3=data.loc[(data['prof'] == 'Actor') & (data['age']>45)] [['fname','lname','age','loc']]
print(data3)