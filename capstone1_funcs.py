
import matplotlib.pyplot as plt
import numpy as np


def select_columns(df, columns):
    return df[columns]

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import scipy.stats as stats

def drop_duplicates(df):
    '''
    Drops any duplicate values in the dataframe

    Input- df (pd.DataFrame)
    Output- df (pd.DataFrame)
    '''
    df.drop_duplicates(inplace=True)
    return df

def time_ms_to_sec(df):
    '''
    Converts milliseconds to second.
    Removes millisecond column and returns
    the dataframe with a new time_seconds
    column.

    Input- df (pd.DataFrame)
    Output- df (pd.DataFrame)
    '''

    df['time_seconds'] = df['duration_ms']//1000
    df.drop('duration_ms', axis=1, inplace=True)
    pop = df.pop('time_seconds')
    df.insert(3, 'time_seconds', pop)

def check_for_nans(df, cols):
    '''
    Returns the number of NaNs for each specified column
    in a dataframe

    Inputs- df (pd.DataFrame), cols (list of columns)
    Output- List of NaNs for each column
    '''
    for col in cols:
        print(f'NaNs in {col}:', df['acousticness'].isnull().sum())

def scatter_plot(df, x_col, y_col, alpha=0.5):
    plt.scatter(df[x_col], df[y_col], alpha=alpha)
    plt.show()

def plot_hist(axs, dfs, names, col):
    for ax, df, name in zip(axs, dfs, names):
        ax.hist(df[col], bins=70)
        ax.set_title(name)
    fig.tight_layout()





if __name__ == '__main__':
    pass
