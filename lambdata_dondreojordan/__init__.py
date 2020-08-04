"""
lambdata - a collection of Data Science helper functions
"""

import numpy as np
import pandas as pd


list = []
date_column = []
column_names = X.columns


print(column_names)


def clean_values(X):
    print("Before cleaning missing values/n:",
          X.isnull().sort_values(ascending=False))
    X.replace({'?': np.Nan, '': np.NaN}, axis=1, inplace=True)
    print("After cleaning missing values/n:",
          X.isnull().sort_values(ascending=False))
    return X


def clean_header(X):
    """This functions removes augmentation and spaces from headers"""
    X.columns = X.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    for i in column_names:
            print('{} is unique: {}'.format(i, X[i].is_unique))


def clean_datetime(X, date_column):
    pd.to_datetime(X['date_column'], inplace=True)
    X['year'] = X[date_column].dt.year
    X['month'] = X[date_column].dt.month
    X['week'] = X[date_column].dt.week
    X['day_of_year'] = X[date_column].dt.dayofyear
    return X['year'], X['month'], X['week'], X['day_of_year']


# TEST= pd.DataFrame(np.ones(10))


print('You are ready to go!')
