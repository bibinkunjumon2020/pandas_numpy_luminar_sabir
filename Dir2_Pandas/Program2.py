import pandas as pd
import numpy as np
s1=pd.Series([2,3,4])
s2=pd.Series([6,7,8,9])
print(pd.Series([1,2,3],dtype=float))
print(pd.Series([3,4,5],dtype=complex))
#print(s1,"\n",s2)
#s3=s1.append(s2)
#print(s3)
#s4=s1.append(s2,ignore_index=True)   # Append only possible between series s1.appens([2,3]) wrong
#print(s4)
s5=pd.concat([s1,s2])
print(s5)
s5=pd.concat([s1,s2],ignore_index=True)
print(s5)
print('######')
s3=s1.add(2) # Adding 2 with each element in series
print(s3)
print(s3.subtract(1))
print(s3.multiply(2))
print(s3.divide(1))