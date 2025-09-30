import random
import pandas as pd
import numpy as np

olympic=pd.read_csv('./olympic.csv')
car=pd.read_csv('./car_sales_data.csv')

# oll1=olympic["born_country"].value_counts()
# oll2=olympic["born_city"].value_counts()

# oll=olympic[olympic["born_country"] == 'USA']["born_city"].value_counts().tail(25)

# diff=olympic.groupby(['born_region'])['born_country'].sum()
# diff1=olympic.groupby(['born_region'])['born_country'].mean()
car['sold']=np.random.randint(0, 11, size=len(car))
cars=car.groupby(['Manufacturer']).agg({'sold' : 'sum', 'Price': 'mean'}).reset_index()

print(cars)

