#max fn


import pandas as pd
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",names=['id','fname','lname','age','prof','loc'])

#in each profession max age is searched and printed

age_max=data.groupby('prof') ['age'].max()
print('max = ....\n',age_max)

#min age in each profession
age_min=data.groupby('prof') ['age'].min()
print("age min=\n",age_min)


#sum

sum_age=data.groupby('prof') ['age'].sum()
print("Sum of Ages.......",sum_age)

#Average/mean age by location

avg_age=data.groupby('loc') ['age'].mean()
print("Average by Location = ....\n ",avg_age)