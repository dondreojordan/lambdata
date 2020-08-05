"""
Lambdata - A collection of Data Science Helper Functions
"""

import pandas as pd
import sklearn.model_selection import train_test_split


# Pull data from dropbox
!wget https://www.dropbox.com/s/hfdbukd3se01934/hotel_bookings.csv?dl=0

# Used data set testing
DF =pd.read_csv('/content/hotel_bookings.csv?dl=0')


def clean_values(df):
     """
    Takes a dataframe and only prints the columns with null values and the amount
    of nulls
    :param df: Dataframe
    :return: None
    """
    cols = df.columns
    df.replace({'': np.NaN}, axis=1, inplace=True)
    nulls = df.isnull().sum().sort_values(ascending=False)
    print("Before cleaning missing values/n:", nulls)
    df.replace({'': np.NaN}, axis=1, inplace=True)
    print("After cleaning missing values/n:",
          nulls)
    if all(_ == 0 for _ in nulls):
        print('There are no nans in the dataframe')
    else:
        for i in range(len(cols)):
            if nulls[i] > 0:
                print(f"{cols[i].ljust(20, ' ')} {nulls[i]}")
    return


def clean_header(df):
    """This functions removes augmentation and spaces from headers"""
    pass


def add_datetime_cols(df, col_name):
    """
    Adds columns by year, month, week and day of year.
    Drops column from original dataframe. 
    :param col_name: Column in dataframe indicating date/time. 
    :return: Dataframe with...
    """
    pd.to_datetime(df['col_name'], inplace=True)
    df['year'] = df[col_name].dt.year
    df['month'] = df[col_name].dt.month
    df['week'] = df[col_name].dt.week
    df['day_of_year'] = df[col_name].dt.dayofyear
    df.drop(col_name, axis=1, inplace=True)


def train_val_test_split(df, target_col, test_size, val_size, random_state=None):
    """
    Performs a train test val split on the data
    :param df: A pandas dataframe
    :param target_col: A string which is the target column's name
    :param test_size: A float, the percentage of data in the train
    :param val_size: A float, the percentage of the data in the validation set
    :param random_state: An integer, used for random state in train test split
    :return: X_train, X_val, X_test, y_train, y_val, y_test
    """
    features = df.drop(target_col, axis=1)
    target = df[target_col]
    X, X_test, y, y_test = train_test_split(features, target, test_size=test_size, random_state=random_state)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=val_size, random_state=random_state)
    return X_train, X_val, X_test, y_train, y_val, y_test


print('You are ready to go!')
