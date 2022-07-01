import pandas as pd
data={'Name':['A','B','C','D','E','F'],"Age":[23,56,12,67,45,31],"Course":['MBA','MCA','CS','EC','UTO','uio'],"Mark":[123,678,345,890,234,78]}
df=pd.DataFrame(data)
print(df)
print(df['Mark'])
print(df['Name'],df['Age'])
print(df[['Name','Age']])
print(df[['Name','Age','Course']]) #For accesing
print(df.iloc[2])  # For accessing that index valuein each key->row
print(df[2:3])  #can acess values like this also
print(df[::-1])  # Reversed output
print((df.iloc[::-1])) #Reverse

print(df[:])
print(df.iloc[:])
print("#"*100)
print(df.iloc[::2]) #index jump with 2 increment
print(df[::2])
# print(df[0]) it is wrong bur print(df['key']) is correct