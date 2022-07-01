#Nested list ->Data frame
import pandas as pd
mylist=[[12,'bibin','kunju',32,'Engineer',700000],
        [2893,'linu','raju',43,'Manager',89763],
        [123,'denzel','bibin',2,'child',5656565],
        [345,'hyson','MS',34,'Tester',6767262],
        [456,'prince','thayoli',34,'Myru',909090]]
data=pd.DataFrame(mylist,columns=["id",'fname','lname','age','Profession','Salary'])
print(data.columns)
data['gender']=['M','M','F','M','F']  #Field for each row must be given
print(data)