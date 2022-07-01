#Nested list ->Data frame
import pandas as pd
mylist=[[12,'bibin','kunju',32,'Engineer',700000],
        [2893,'linu','raju',43,'Manager',89763],
        [123,'denzel','bibin',2,'child',5656565],
        [345,'hyson','MS',34,'Tester',6767262],
        [456,'prince','thayoli',34,'Myru',909090]]

data=pd.DataFrame(mylist,columns=["id",'fname','lname','age','Profession','Salary'])  #Here 2D matrix
print(data)
print(data.head(2)) # Like in series head & tail works in Data frame
print(data.tail(3))
print(data.dtypes) # to know datatype of each column
#To collect partiular data from column
print(data['fname'])
print(data[['fname','age']]) #to collect multiple values give '[['
print(data.iloc[0])
print(data.iloc[3][1])

print(data[2:3])
print(data.iloc[2])
print(data.iloc[1:3])
print("******")
print(data.iloc[0:5:2]) #step 2
print(data.iloc[2:5] [['fname','Salary']])
