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

Where `dataset` is the filename of the .csv file containing your data, followed by one or more `var` names indicating categorical variables in the dataset to be used in stratified sampling. Optionally, a distribution of data to training, testing, and validation sets can be specified using the flag `--distr`, followed by three fractions `f` between 0 and 1, adding up to 1. The default distribution is 0.70 training set, 0.15 testing set, and 0.15 validation set.

For example, if you have a dataset named `testdata.csv`, in which there are categorical variables `var1` and `var3`, you can split the data while preserving the proportions of `var1` and `var3` by running the following command:

```shell
python3 split_data.py testdata.csv var1 var3
```

### Output ###

The program will output the resulting training, testing, and validation sets directly to .csv files. These files will be saved in a directory (created automatically) with the same name as the original dataset. For instance, the three sets from splitting `testdata.csv` will be saved in a directory named `testdata`.

Note that if the program is run twice on the same dataset, the previous result will be overwritten unless the directory is renamed.

# Implementation details #

### The algorithm ###

The program splits the data into respective sets using the following algorithm:

1. The dataset is split into strata for each possible combination of values of the given variable. For example, if preserving the proportions of `var1={A,B}` and `var3={a,b,c}`, the data is grouped into 6 strata represented by the values `(A,a), (A,b), (A,c), (B,a), (B,b), (B,c)`. More generally, if *n* variables are given as input, with each having *v<sub>i</sub>* values, then the dataset is split into *Π<sup>n</sup><sub>i=0</sub> v<sub>i</sub>* strata.

### Runtime analysis ###

T
