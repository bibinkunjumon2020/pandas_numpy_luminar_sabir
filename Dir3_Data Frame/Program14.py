#Evaluate Fn: Sum,Count,max,min

#Count
import pandas as pd
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",names=['id','fname','lname','age','prof','loc'])
print(data['loc'].isin(['china']).sum())

prof_count=data.groupby('prof') ['prof'].count()
print(prof_count)

print(data.groupby('loc') ['loc'].count())

#--------
#  ireland engineer 3
# africa photographer 5  etc
#means in that location how many profession they group
print(data.value_counts(['loc','prof']))

#-----Single line for counting the location men
print(data.value_counts('loc'))

#-----
print("-------")
print(data["loc"].value_counts())