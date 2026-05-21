# I made this script as a library for my custom made classes and methods to help me save time and effort

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class OutlierHandling:  # this class is using IQR to display and handle outliers in a dataframe

    exception_list = []

    def __init__(self):
        pass

    # this funciton will work on getting the iqr, lower/upper bounds from a column
    def fit_IQR(self, column: pd.Series):
        c = column.copy()

        try:
            q1 = c.quantile(1 / 4)
            q3 = c.quantile(3 / 4)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            return iqr, lower_bound, upper_bound
        except Exception as e:
            self.exception_list.append("fit_iqr exception as :", e)
            return None

    # def fit_IQR_df(self, df: pd.DataFrame):
    #     df2 = df.copy()
    #     for i in df.select_dtypes('number'):

    # this function for applying the transformation
    def remove_outliers(self, column: pd.Series):
        c = column.copy()
        iqr, lower, upper = self.fit_IQR(c)
        c = c[(c > lower) & (c < upper)]
        return c

    # this function for displaying
    def display_outliers(self, column: pd.Series):
        higher_outliers = []
        lower_outliers = []
        c = column.copy()
        iqr, lower, upper = self.fit_IQR(c)
        for counter, i in c.items():
            if i > upper:
                higher_outliers.append(i)
                print(f"{counter} : {i}")
            elif i < lower:
                lower_outliers.append(i)
                print(f"{counter} : {i}")
        return higher_outliers, lower_outliers

    def display_outliers_df(self, df: pd.DataFrame):
        higher_outliers = []
        lower_outliers = []
        # iqr, lower, upper = self.fit_IQR(c)
        for i in df.select_dtypes("number").columns:

            iqr, lower, upper = self.fit_IQR(df[i])
            print(f"{i} : ")
            for counter, j in df[i].items():
                if j > upper:
                    higher_outliers.append(j)
                    print(f"{counter} : {j}")
                elif j < lower:
                    lower_outliers.append(j)
                    print(f"{counter} : {j}")
            print("_________")
        return higher_outliers, lower_outliers

    # this function to return without print
    def return_outliers(self, column: pd.Series):
        counter = 0
        higher_outliers = []
        lower_outliers = []
        c = column.copy()
        iqr, lower, upper = self.fit_IQR(c)
        for i in c:
            if i > upper:
                higher_outliers.append(i)
            elif i < lower:
                lower_outliers.append(i)
            counter += 1
        return higher_outliers, lower_outliers

    # this function to return count
    def count_outliers(self, column: pd.Series):
        c = column.copy()
        higher, lower = self.return_outliers(c)
        number_of_outliers = len(higher) + len(lower)
        return number_of_outliers

    # for dataframe
    def count_outliers_df(self, df: pd.DataFrame):
        for i in df.select_dtypes("number").columns:

            higher, lower = self.return_outliers(df[i])
            total = len(higher) + len(lower)
            if total != 0:
                print(f"{i}: {len(higher)}, {i}: {len(lower)}, Total: {total}")
                print("________________\n")

    # this function to plot outliers
    def plot(self, dataframe: pd.DataFrame, h=10, w=6):

        length_list_hs = []
        length_list_ls = []
        names = []

        for i in dataframe.select_dtypes("number").columns:
            higher, lower = self.return_outliers(dataframe[i])
            length_list_hs.append(len(higher))
            length_list_ls.append(len(lower))
            names.append(i)
        # plotting

        plt.figure(figure=(h, w))
        plt.barh(names, length_list_hs, label="Higher Outliers")
        plt.barh(names, length_list_ls, label="Lower Outliers")
        plt.legend()
        plt.show()
