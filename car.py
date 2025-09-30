from nt import rename
import pandas as pd
import numpy as np

car=pd.read_csv('./car_sales_data.csv')
# car["discount"] = "10%"
car["Discount"]=np.where(car["Price"] > 30000, "20%", "15%")
car=car.drop(columns = ["Fuel type"])
car["Discount"]=car["Discount"].str.replace("%", " ").astype(int)

car["Total_price"]= car["Price"]-(car["Price"]*car["Discount"]//100)
car=car.rename(columns={'Total_price' : 'Billing_price'})

print(car)