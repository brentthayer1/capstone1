import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

def select_columns(df, columns):
    return df[columns]

def drop_duplicates(df):
    """
    Drops any duplicate values in the dataframe

    Parameters:
        df (DataFrame): DataFrame to drop duplicates from

    Returns:
        out (DataFrame)
    """

    df.drop_duplicates(inplace=True)

    return df


def time_ms_to_sec(df):
    """
    Converts milliseconds to seconds
    Removes millisecond column and returns
    the dataframe with a new time_seconds
    column.

    Parameters:
        df (DataFrame): DataFrame who's time
        column will be converted

    Returns:
        out (DataFrame)
    """

    df['time_seconds'] = df['duration_ms']//1000
    df.drop('duration_ms', axis=1, inplace=True)
    pop = df.pop('time_seconds')
    df.insert(3, 'time_seconds', pop)


def drop_columns(df, cols):
    """
    Drops specified columns from DataFrame

    Parameters:
        df (DataFrame): DataFrame who's columns
        will be dropped
        cols (list): List of columns to be dropped

    Returns:
        out (DataFrame)
    """

    df.drop(cols, axis=1, inplace=True)


def check_for_nans(df, cols):
    """
    Checks for NaNs in specified columns

    Parameters:
        df (DataFrame): DataFrame to check for NaNs
        cols (list): List of columns to check

    Returns:
        out (count): Number of NaNs for each specified column
        in the dataframe
    """

    for col in cols:
        print(f'NaNs in {col}:', df[col].isnull().sum())


def plot_hist_and_means(ax, df_, column):
    """
    Plots the distributions and means for a
    specified column in a DataFrame

    Parameters:
        ax (axes object): Axes to plot on
        df_ (DataFrame): DataFrame who's column will be plotted
        column (series): Columns to plot

    Returns:
        Histogram plot of specified column
    """

    sns.distplot(df_[column], ax=ax,)
    ax.set_title(f'{column} mean: {round(df_[column].mean(), 2)}')


# def plot_hists_attribute(df_lst, column, color_list, df_name_lst):
#     for df_, colr, name in zip(df_lst, color_list, df_name_lst):
#         print(f'Mean value for {column} in {name}:', round(df_[column].mean(), 2))
#         sns.distplot(df_[column], color=colr)
#         plt.show()


def plot_dists_pdf(ax, df_, column, low, high):
    """
    Plots the distribution for a specified column in a DataFrame

    Parameters:
        ax (axes object): axes to plot on
        df_ (DataFrame): DataFrame who's column will be plotted
        column (series): Column to plot
        low (int/float): Lower x limit
        high (int/float): Upper x limit

    Returns:
        PDF plot of the specified column
    """

    sns.distplot(df_[column], hist=False, ax=ax)
    ax.set_xlim(low, high)
    ax.set_title(f'{column} pdf')


def plot_dists_cdf(ax, df_, column, low, high):
    """
    Plots the distribution for a specified column in a DataFrame

    Parameters:
        ax (axes object): axes to plot on
        df_ (DataFrame): DataFrame who's column will be plotted
        column (series): Column to plot
        low (int/float): Lower x limit
        high (int/float): Upper x limit

    Returns:
        CDF plot of the specified column
    """

    kwargs = {'cumulative': True}
    sns.distplot(df_[column], hist=False, hist_kws=kwargs, kde_kws=kwargs, ax=ax)
    ax.set_xlim(low, high)
    ax.set_title(f'{column} cdf')


def plot_scatter(ax, df_, column, against, low, high):
    """
    Plots a scatter plot for a specified column in a DataFrame
    against another column in the data frame.

    Parameters:
        ax (axes object): axes to plot on
        df_ (DataFrame): DataFrame who's columns will be plotted
        against each other
        column (series): X Column to plot
        against (series): Y Column to plot
        low (int/float): Lower x limit
        high (int/float): Upper x limit

    Returns:
        Scatter plot of specified columns
    """

    ax.scatter(df_[column], df_[against], s=0.5, alpha=0.5, marker='.')
    ax.set_xlim(low, high)
    ax.set_xlabel(column)
    ax.set_ylabel(against)
    ax.set_title(f'{column} vs. {against}')


def dfs_info_list(df_lst, df_name_lst, column):
    """
    Returns the mean and standard deviation for each DataFrame
    from a list of DataFrames.

    Parameters:
        df_lst (list): List of DataFrames to extract mean and
        standard deviations from
        df_name_lst (list): List of DataFrame names
        column (series): The column of the specified data frame to
        find the mean and standard deviation of

    Returns:
        (out) List of strings containing the mean and standard deviation
        for each df
    """

    lst = []
    for df_, df_name in zip(df_lst, df_name_lst):
        lst.append(f'{df_name}  Mean: {np.mean(df_[column]):0.03f}  Std Dev: {np.std(df_[column]):0.03f}')

    return lst


def master_plotter(df_lst, df_name_lst, column, against, low, high, fs):
    """
    Plots the CDF, PDF and scatter plot for a specified column in a DataFrame

    Parameters:
        df_lst (list): List of DataFrames to plot together
        df_name_lst (list): List of DataFrame names
        column (series): Column to plot
        against (series): Y Column to plot in scatter plot
        low (int/float): Lower x limit
        high (int/float): Upper x limit
        fs (tuple-int/float): Figure size of output

    Returns:
        CDF, PDF, scatter plot and mean/ standard deviation for
        the column in each DataFrame
    """

    info = dfs_info_list(df_lst, df_name_lst, column)
    fig, ax = plt.subplots(2,2, figsize=fs)
    for df_ in df_lst:
        plot_dists_cdf(ax[0][0], df_, column, low, high)
        plot_dists_pdf(ax[0][1], df_, column, low, high)
        ax[0][1].set_yticks([])
        plot_scatter(ax[1][0], df_, column, against, low, high)
        ax[1][1].set_xticks([])
        ax[1][1].set_yticks([])
    fig.legend(info, bbox_to_anchor=(.60, .43), loc=2, borderaxespad=0., fontsize='medium', markerscale=9, frameon=False)
    fig.tight_layout()


def spearman_correlation(frame, col1, col2):
    """
    Returns correlation and p-value for two series

    Parameters:
        frame (DataFrame): DataFrame who's columns will be compared
        col1 (series): First Series being compared
        col2 (series): Second Series being compared

    Returns:
        Correlation between the two series and the p-value
    """

    a, b = frame[col1], frame[col2]
    correlation, pvalue = stats.spearmanr(a, b)
    print(f'{col1} and {col2} have a correlation of {round(correlation, 3)}, with a p-value of {pvalue:.3e}') 


def plot_correlations(df_, columns):
    """
    Plots the correlation between specified columns

    Parameters:
        df_ (DataFrame): DataFrame who's columns will be plotted
        columns (list): The columns of the specified DataFrame to plot

    Returns:
        Correlation heat map
    """

    Var_Corr = df_[columns].corr()
    sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=True, cmap='Blues')




if __name__ == '__main__':
    pass
