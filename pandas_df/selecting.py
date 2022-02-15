import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from pandas_df.datasource import df

"""
------------- SELECTING ---------------
"""

"""
Get a column
Double-bracket to access column as DataFrame
"""
country_col = df[['country']]
print('All', country_col, type(country_col))
# print(type(cars['country'])) # <class 'pandas.core.series.Series'>

"""
Get 1 or several rows by indexes
"""
# Get the US row by index
print('US')
print('-----------')
print(df.loc[['US']])

# Get several rows by indexes
print('Several rows')
print('-----------')
print(df.loc[['US', 'JP', 'RU']])

# Get several rows from index 0 -> 2:
print('Row indexes')
print('-----------')
print(df.loc['US':'JP', 'country'])

"""
Get specific rows and columns
"""
# Get country and cars_per_cap columns for US and RU
print('US and RU')
print('-----------')
print(df.loc[['US', 'RU'], ['country', 'cars_per_cap']])

# Loop through DataFrame
for index, row in df.iterrows():
  print(f"Country: {row['country']}. Cars per cap: {row['cars_per_cap']}")

# Print the first 3 rows:
print('First 3 rows')
print(df.loc['US':'JP'])  