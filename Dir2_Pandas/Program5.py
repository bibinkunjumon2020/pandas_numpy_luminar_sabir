import pandas as pd

data={'name':['A','B','C'],'qual':['MBA','BA','BTech'],'job':['Engineer','Police','Manager'],'salary':[1000,3456,65432]}
df=pd.DataFrame(data)
print(df)
print(df.iloc[::3])