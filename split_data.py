#
#
#

import splitter as sp
import pandas as pd
import argparse
import os

# Usage: split_data.py [-h] dataset var [var ...]
parser = argparse.ArgumentParser(
  description='Split dataset into training, testing, and validation sets using stratified sampling on an indefinite subset of attributes.')
parser.add_argument('dataset', type=argparse.FileType('r'),
  help='Filename of dataset (must be CSV format).')
parser.add_argument('attributes', metavar='var', nargs='+',
  help='One or more attributes to use in stratified sampling.')
parser.add_argument('--distr', type=float, metavar='f', nargs=3, default=[0.70,0.15,0.15],
  help='Distribution of data to training, test, and validation sets given as three fractions between 0 and 1.')

# Parse arguments and read CSV into Pandas dataframe
args = parser.parse_args()
data = pd.read_csv(args.dataset, encoding='utf-8')
vars = args.attributes
fracs = args.distr

# Verify each attribute argument exists in dataframe
args_valid = sp.check_args(data, vars, fracs)
if args_valid == 0:
  raise SystemExit('One or more vars given do not exist in dataset.')
elif args_valid == 1:
  raise SystemExit('One or more vars given are not categorical.')
elif args_valid == 2:
  raise SystemExit('Fractions given for --distr must be positive and add to 1.')

# Split data into training, test, and validation sets
train, test, validate = sp.split(data, vars, fracs)

# Write training, test, and validation sets to CSV files contained in folder with the name of original dataset
path = os.path.splitext(os.path.basename(args.dataset.name))[0]
if not os.path.exists(path):
  os.makedirs(path)
for d in ((train, 'training.csv'), (test, 'testing.csv'), (validate, 'validation.csv')):
  d[0].to_csv(path + '/' + d[1], encoding='utf-8', index=False)