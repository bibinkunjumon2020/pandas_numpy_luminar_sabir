import pandas as pd
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",header=None)
data.columns=['id','fname','lname','age','prof','loc']
#print(data)

#Order - Ascending/Descending

data1=data.sort_values(by='age') # Ordering dataframe values in age increasing order
print(data1)
data2=data.sort_values(by='age',ascending=False)
print(data2)