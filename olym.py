import pandas as pd

oly=pd.read_excel("./olympics-data.xlsx")
oly.to_csv("olympic.csv", index=False)

oly["first_name"]=oly["name"].str.split(' ').str[0]
qu=oly.query('first_name == "Albert"')

oly["born_datetime"]=pd.to_datetime(oly["born_date"])

oly["born_year"]=oly["born_datetime"].dt.year

oly["height_cat"]=oly["height_cm"].apply(lambda x: 'Short' if x< 165 else('Average' if x< 185 else 'Tall'))

def cat_athlete(row):
    if row["height_cm"] < 175 and row["weight_kg"] < 70:
        return 'Light_Weight'
    elif row["height_cm"] < 185 and row["weight_kg"] < 80:
        return 'Middle_weight'
    else:
        return 'Heavy_weight'

oly['category'] = oly.apply(cat_athlete, axis=1)
print(oly.head())