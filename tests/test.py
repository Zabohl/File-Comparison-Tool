import pandas as pd
from src.file_compare import file_compare

df1=pd.DataFrame({'a':[1,2,3,4,5],'b':[1,2,3,4,5]})
df2=pd.DataFrame({'a':[6,7,8,9,10],'b':[1,2,3,4,5]})

print(file_compare(df1=df1,df2=df2,keys='a',matching_cols='b',field_map1={'c':'B'}))