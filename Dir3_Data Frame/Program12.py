#
#Mean of a column
#Median of a column
#Mode
import pandas as pd
data=pd.read_csv(("/Users/bibinkunjumon/Documents/customer.txt"),names=['id','fname','lname','age','prof','loc'])

x_mean =data['age'].mean()
#------ Here we find out the mean of column age

data['age'].fillna(x_mean,inplace=True)
print(data)

x_median = data['age'].median()  # Median= middle value after sorting if not middle value mean of middle 2 values
data['age'].fillna(x_median,inplace=True)

x_mode=data['age'].mode() # Most repeated values
data['age'].fillna(x_mode,inplace=True)
print(data)