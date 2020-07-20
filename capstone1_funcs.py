
import matplotlib.pyplot as plt
import numpy as np


def select_columns(df, columns):
    return df[columns]

def plot_selected_cols(dfs, column):
    for df in dfs:
        plt.hist(df[column])

def create_dec_id(df, str):
    lst = []
    for i in range(len(df)):
        lst.append(f'{str}_{i}')
    df[dec_id] = lst



if __name__ == '__main__':
    pass
