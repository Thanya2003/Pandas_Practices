import pandas as pd
import numpy as np
 
resu= pd.read_csv('./car_sales_data.csv')

resu.loc[[2,3], "Price"]=np.nan

re=resu.isna().sum()
resu=resu.fillna(resu["Price"].mean())
resu=resu.fillna(resu["Price"].interpolate())
resu=resu.dropna()
resu=resu.dropna(subset=["Price"], inplace=True)
resu = resu[resu["Price"].isna()]

resu = resu[resu["Price"].notna()]

print(resu)
print(re)
