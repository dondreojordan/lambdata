"""
Lambdata - A collection of Dataframe Helper Functions
"""

import pandas as pd
import numpy as np
import datetime


# Used data set testing
TEST = {'FIRST_NAME': ['Corey', 'Test', ' ', 'Kim', 'John'],
        'LAST_NAME': ['Shafer', 'User', 'Sue', 'Berly', 'Jacob'],
        'SALARY': [50000, 25000, 95000, 115000, 1000000],
        'START_YEAR': [
            '2016-05-29',
            '2005-10-04',
            '2010-12-10',
            '1998-02-09',
            '2019-08-11'
            ]}

TEST = pd.DataFrame(data=TEST)


def clean_null_values(df):
    """
    Takes a dataframe and adds name to empty cell
    :param df: Dataframe
    """

    df.replace({' ': 'Tony'}, inplace=True)
    df.isnull().sum().sort_values(ascending=False)


def add_datetime_col(df, col_name):
    """
    Adds columns month, day, year to the dataframe.
    Drops the original columns.
    :param df: A pandas Dataframe
    :param col_name: A column name of string for date
    :return: None
    """

    col_name = 'start_year'

    df[col_name] = pd.to_datetime(df[col_name], infer_datetime_format=True)
    df['year'] = df[col_name].dt.year
    df['month'] = df[col_name].dt.month
    df['day_of_year'] = df[col_name].dt.dayofyear
    df['week'] = df[col_name].dt.week
    df.drop(col_name, axis=1, inplace=True)

def clean_header(df):
    """
    This functions removes capitalization in the column headers.
    :param df: Dataframe
    :param columns: Columns in dataframe
    :return: None
    """

    df.columns = map(str.lower, df.columns)


print("You are ready to go Dondre'! (:")
