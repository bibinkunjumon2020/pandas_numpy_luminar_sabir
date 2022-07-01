#Nested list ->Data frame
import pandas as pd
mylist=[[12,'bibin','kunju',32,'Engineer',700000],
        [2893,'linu','raju',43,'Manager',89763],
        [123,'denzel','bibin',2,'child',5656565],
        [345,'hyson','MS',34,'Tester',6767262],
        [456,'prince','thayoli',34,'Myru',909090]]

#print(mylist)
s1=pd.Series(mylist) #Here it is 1D array
#print(s1)
data=pd.DataFrame(mylist)  #Here 2D matrix
print(data)
print("&&&&&&&&&")
print(data[1][2])  #Here the order is [Column] , [Row]
#print(data.iloc[1])
print(data.iloc[1][2]) #Here [row] [column]


data=pd.DataFrame(mylist,columns=["id",'fname','lname','age','Profession','Salary'])  #Here 2D matrix
print(data)
print(type(data))
print(data.shape)
print(data.size)
print(data.columns) # Print column titles-if default gives start=0,stop=6
print(data.values) #print values without  index
print("#####")
print(data.iloc[0])
print("$$$$$")
print(data.iloc[2][0]) #row ,column
print("&&&&&&")
print(data.describe()) # Here describe is different than Mysql describe- Only integer.No string
print(data.describe(include='O')) #Here ony string values some extra details given
print(data.describe(include='all'))

