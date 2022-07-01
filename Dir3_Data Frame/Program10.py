import pandas as pd
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt")
data.columns=['id','fname','lname','age','prof','loc']

#1.
data2=data.loc[data['age']>50] [['fname','lname','loc','age']]
print("Q1. ",data2)
#2.
data3=data.loc[data['loc']=='china'] [['fname','lname','age','loc']]
print("Q2. ",data3)
#3.
data4=data.sort_values(by='age',ascending=True)
#print(data4)
print("Q3. Age Min 2 Employees")
print(data4.head(2) [['fname','lname','age','loc']])
print("Q4 . Age Max 1 Employee")
print(data4.tail(1) [['fname','lname','age','loc']])
# Can do all operations by giving '.' in between -first filter,then sort,then print
print(data.loc[data['loc']=='china'].sort_values(by='age').head(4) [['fname','loc','age']])