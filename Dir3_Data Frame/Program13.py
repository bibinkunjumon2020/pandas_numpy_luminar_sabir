import pandas as pd
data=pd.read_csv("/Users/bibinkunjumon/Documents/customer.txt",names=['id','fname','lname','age','prof','loc'])
#print(data)

#----------------------
data1=data.drop_duplicates()  # Here all rows and columns compared for removing duplicates : so no actual removal of single row item
#print(data1)

#-----------------
x=data.isin(['ireland']).sum() # irelnd is searched in al columns and list count of each column
#print(x)

#----------------------
data2=data['loc'].drop_duplicates() #Here it works bcs only loc column is checked and many places removed due to epetition
x=data2.isin(['ireland']).sum()
#print("####",x)
#print(data2)

#--------------------
y=data2.isin(['india','china','ireland']).sum() #Each loc only once so sum=3 i an give many places as a list
 #print("@@@@@",y)
#------------
#print(data.isin(['ireland']).sum()) #here 77 & 0s bcs no replacement happened in data & all columns output
#print(data['loc'].isin(['ireland']).sum())  #Here only loc col analysed so 77 only

#-------
data['loc'].drop_duplicates(inplace=True)# Here inplace wont work bcs it returns only one column of locs without duplicates
#but our actual DF is different - so DF is immutable

print(data['loc'].isin(['ireland']).sum())
print(data)  # We ger the oroginal DF as output here.

print("-------------")
data=data['loc'].drop_duplicates(inplace=True) #here null return so no o/p
print(data)

