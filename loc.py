import pandas as pd

df=pd.read_csv("./results.csv")
# df.index=df["year"]
d2=df.tail(5)

# tt=d2.loc[1:5]
# tt=df.loc[1:5]
# print(tt)

# tt1=df.sample(10)
# print(tt1)

# df.loc[5:8, "type"] = "winter"
# print(df.loc[4:10])

# sort=df.sort_values(["discipline", "event"], ascending=True)
# print(sort)

cond=df[(df["year"]>=1948) & (df["medal"]=='Bronze')][['discipline', 'event', 'medal', 'year']]
print(cond)


stri=df[df['discipline'].str.contains("Fencing", case=False)]
print(stri)
qu=df.query('year == 1996 and discipline == "Handball"')
print(qu)
