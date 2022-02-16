from typing import Callable, List
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from pandas_df.datasource import df

"""
------------- FILTERING ---------------
"""
def simple_filter():
  def filter_by_cpc(threshold: int):
    return df[df.cars_per_cap > threshold]

  def filter_by_country(countries: List[str]):
    """
    Use .isin() to filter the value belongs to a list
    """
    return df[df.country.isin(countries)]

  return {
    "filter_by_cpc": filter_by_cpc,
    "filter_by_country": filter_by_country
  }

def get_filter(name: str) -> Callable:
  filter_fn = simple_filter().get(name)
  if not filter_fn:
    raise Exception('No filter fn for that criteria')

  return filter_fn

# Filter all countries having cpc > 300
print('Cars per cap > 300:\n', get_filter('filter_by_cpc')(300))

# Filter by country
print('Only US and JP: \n', get_filter('filter_by_country')(['United States', 'Japan']))