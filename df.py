import pandas as pd

df=pd.read_csv("./results.csv")
# df1=pd.read_excel("C:\Users\Thanya\Downloads\olympics-data.xlsx")
# df2=pd.read_feather("C:\Users\Thanya\Downloads\olympics-data.feature")
# # df2=pd.read_parquet

# df3=df1.to_csv
# d4=df2.to_parquet

# print(df)
# print(df.head(1))
print(df.tail(2))

print(df.columns)