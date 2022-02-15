from typing import Callable
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

  return {
    "filter_by_cpc": filter_by_cpc
  }

def get_filter(name: str) -> Callable:
  filter_fn = simple_filter().get(name)
  if not filter_fn:
    raise Exception('No filter fn for that criteria')

  return filter_fn

# Filter all countries having cpc > 300
print('Cars per cap > 300:\n', get_filter('filter_by_cpc')(300))