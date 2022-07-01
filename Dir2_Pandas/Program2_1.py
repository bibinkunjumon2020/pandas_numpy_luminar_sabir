import pandas as pd
s1=pd.Series({'name':'bibin','age':34,'salary':34567}) #dict and series created in a line
print(s1)
dict1={'id':123,'age':34,'name':'denzel'}
s2=pd.Series(dict1,index=['name','age','id'])  #Here series created in the order of index i am giving
print(s2)
myDic={'name':'bibin','age':30,'salary':78675}
s3=pd.Series(myDic,index=['age']) #Its not possible to give less index in list
s4=pd.Series(myDic,index=['age','salary','name'])
print(s3)
print(s4)
# Here dic key became indexes insted of 0,1,2,3