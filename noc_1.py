import pandas as pd

olly = pd.read_csv('./olympic.csv')
noc = pd.read_csv('./noc_regions.csv')

olym= pd.merge(olly, noc, left_on='born_country', right_on='NOC', how='left')

olym.rename(columns={'region':'born_country_full'}, inplace=True)

# olym=olym[olym['NOC_x'] != olym['born_country_full']][['name', 'NOC_x', 'born_country_full']]

usa=olym[olym['born_country']=='USA'].copy()
gbr=olym[olym['born_country']=='GBR'].copy()

new=pd.concat([usa, gbr])[['name', 'born_country']]

print(new.tail())