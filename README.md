# How to use #

### Dependencies ###

This program requires the following Python installation and libraries:
* [Python](https://www.python.org) v3.0+
* [Pandas](https://pandas.pydata.org) v0.22.0+
* [NumPy](http://www.numpy.org) v1.14.0+

The Pandas and NumPy libraries are used for their highly efficient data structures and basic functions (for instance, [groupby](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html)), which are implemented using optimized CPython code allowing for speedy computation. These dependencies can be easily installed with `pip` through the following command:

```shell
pip3 install numpy pandas
```

### Running ###

To run, move a CSV file containing initial dataset into the same directory as `split_data.py` and `splitter.py`. Then run the program using the following inputs:

```shell
python3 split_data.py dataset var [var ...] [--distr f f f]
```

Where `dataset` is the filename of the .csv file containing your data, followed by one or more `var` names indicating variables in the dataset to be used in stratified sampling. Optionally, a distribution of data to training, testing, and validation sets can be specified using `distr`, followed by three fractions `f` between 0 and 1, adding up to 1. The default distribution is 70% to training set, 15% testing set, and 15% validation set.

For example, if you have a dataset named `testdata.csv`, in which there are unevenly distributed variables `var1` and `var3`, you can split the data by running the following command:

```shell
python3 split_data.py testdata.csv var1 var3
```

### Output ###

The program will output the resulting training, testing, and validation sets directly to .csv files. These files will be saved in a directory (created automatically) with the same name as the original dataset. For instance, the three sets from splitting `testdata.csv` will be saved in a directory named `testdata`.

Note that if the program is run twice on the same dataset, the previous result will be overwritten unless the directory is renamed.

# Implementation details #

### The algorithm ###

T

### Runtime analysis ###

T
