import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from pandas_df.datasource import df

# 2-dimensional NumPy array of values
# print(df.values)

# Column names
# print(df.columns)
# Index(['country', 'drives_right', 'cars_per_cap'], dtype='object')

# Index
# print(df.index)
# Index(['US', 'AUS', 'JP', 'IN', 'RU', 'MR', 'EG'], dtype='object')

"""
SORTING
"""
# Sort df by cars_per_cap
print(df.sort_values('cars_per_cap').head(n=3))

# Sort by country, ascending and then cars_per_cap, descending
print(df.sort_values(['country', 'cars_per_cap'], ascending=[True, False]))


"""
TRANSFORMING DATASET
"""

# Add new column
cars_per_cap_list = df.loc[:, 'cars_per_cap'].values.flatten().tolist()
df['is_high_car_per_cap'] = ['high' if i > 500 else 'low' for i in cars_per_cap_list]
print(df)