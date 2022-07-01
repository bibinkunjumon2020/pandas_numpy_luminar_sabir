#Dict to data frame
import pandas as pd
myDict={'emp1':[12,'bibin','kunju',32,'Engineer',700000],
        'emp2':[2893,'linu','raju',43,'Manager',89763],
        'emp3':[123,'denzel','bibin',2,'child',5656565],
        'emp4':[345,'hyson','MS',34,'Tester',6767262],
        }
#print(myDict)
data=pd.DataFrame(myDict)
#print(data)
data['location']=['Kollam','TVM','Koz','Kazar','kan','alepy']
print(data)
print("*******")
print(data.iloc[0] [['emp1','emp4']])
print(data.iloc[2] [['emp1','emp2']])