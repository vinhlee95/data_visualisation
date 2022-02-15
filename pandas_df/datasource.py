import pandas as pd

# Datasources
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
indexes = ['US', 'AUS', 'JP', 'IN', 'RU', 'MR', 'EG']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

cars_dict = { 'country': names, 'drives_right': dr, 'cars_per_cap': cpc }

df = pd.DataFrame(data=cars_dict, index=indexes)
