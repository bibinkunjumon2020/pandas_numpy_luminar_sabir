import pandas as pd
import numpy as np

#mylist=[]
#for i in range(3,31,3):
    #mylist.append(i)
#print(mylist)


mylist1=np.arange(3,15,3)
#print(mylist1)
s1=pd.Series(mylist1)
print(s1)
s2=pd.Series(mylist1,index=[3,1,2,0])
print(s2)
print(s1[0],s1.iloc[0],s2[0],s2.iloc[0]) #iloc prints value in correct order index eventhough we update index NO CHANGE
#Value of s1[0],s1.iloc[0] - Same bcs default index // s2[0],s2.iloc[0] - different bcs assigned index