#
# Author: Benjamin Kane
# https://github.com/bkane2/StratifiedDataSplitter
#

import pandas as pd
import numpy as np

def check_args(data, vars, fracs):
  """Verifies that all variables given as arguments exist and are categorical, and set sizes are valid"""
  for v in vars:
    # Attribute doesn't exist in dataframe
    if not v in data.columns.values.tolist():
      return 0
    # Attribute is not categorical
    if not pd.api.types.is_string_dtype(data[v]):
      return 1
    # Set sizes are invalid
    if not (sum(fracs)==1.0 and min(fracs)>0):
      return 2
  return -1


def partition(x, fracs):
  """Creates a partition interval such that a dataframe will be split into three segments about the interval."""
  # Example: if fracs[0]=0.70 and fracs[1]=0.15, and len(x) = 100, then the partition interval is [70, 85]
  return [int(fracs[0]*len(x)), int((fracs[0]+fracs[1])*len(x))]


def split(data, vars, fracs):
  """Splits dataframe into training, testing, and validation sets, preserving proportions of variables given in vars"""
  # Divide the data into strata for each unique combination of values of variables in vars
  strata = data.groupby(vars)

  # For each stratum, partition stratum into three sets of given proportions
  sets_strata = strata.apply(lambda x: np.split(x, partition(x, fracs)))

  # Group training, testing, and validation sets across each stratum together
  sets = zip(*[s for s in sets_strata])

  # Combine training, testing, and validation sets to get final sets. Reshuffle in the
  # process so that learning algorithm isn't affected by strata order
  train, test, validate = [pd.concat(s).sample(frac=1) for s in sets]
  return train, test, validate