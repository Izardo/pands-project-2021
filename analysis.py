# This program analyses the Iris dataset

# Author: Isabella Doyle
# imports libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reads in csv file and assigns data to variable 'df'
df = pd.read_csv('IRIS.csv')

# Functions to access basic info about the dataset
def dataInfo(x): 
    print(x)            # print(df) prints first and last 5 lines of dataset
    x = df.info()
    print(x)

# prints full dataset to compare against Fisher's 
def viewFull(x):
    pd.set_option('display.max_rows', 150)
    print(x)

# view summary shows basic statistical information
# may not be needed but gives us an instant range of values to familariase ourselves with the data
def viewFullSummary(x):
    describe = x.describe()
    print(describe)

# side-by-side summary of species
# REF: Describe Function With Groupby Pandas (Python 3.5.1), 7 Apr. 2021, ayhan,
# https://stackoverflow.com/questions/40346436/describe-function-with-groupby-pandas-python-3-5-1
def summaryGrouped(x):
    summary = x.groupby('species').describe()
    print(summary)

# seperate summaries
def individualSummary(x, y):    # x = the dataframe you wish to use, y = the column you wish to get a summary of
    summary = x[x["species"] == y].describe()   # Ref: "Lesson 3. Run Calculations and Summary Statistics on Pandas Dataframes"
                                                # Jenny Palomino, Leah Wasser, 7 Apr. 2021, www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/run-calculations-summary-statistics-pandas-dataframes/
    print(summary)

# Adopted from: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40#:~:text=Iris%20data%20is%20a%20multivariate,and%20petal%20width%2C%20in%20centimeters.&text=It%20consists%20of%20a%20set,Class%2DLabels(Species).
def boxAll():
    sns.set(style="ticks") 
    plt.figure(figsize = (12,10))
    plt.subplot(2,2,1)
    sns.boxplot(x='species',y ='sepal_length',data=df)
    plt.subplot(2,2,2)
    sns.boxplot(x='species',y='sepal_width',data=df)
    plt.subplot(2,2,3)
    sns.boxplot(x='species',y='petal_length',data=df)
    plt.subplot(2,2,4)
    sns.boxplot(x='species',y='petal_width',data=df)
    plt.show()

def allViolin():
    sns.set(style="whitegrid")
    plt.figure(figsize=(12,10))
    plt.subplot(2,2,1)
    sns.violinplot(x='species',y='sepal_length',data=df)
    plt.subplot(2,2,2)
    sns.violinplot(x='species',y='sepal_width',data=df)
    plt.subplot(2,2,3)
    sns.violinplot(x='species',y='petal_length',data=df)
    plt.subplot(2,2,4)
    sns.violinplot(x='species',y='petal_width',data=df)
    plt.show()


# calling the functions
# boxAll()
allViolin()
#individualSummary(df, "Iris-setosa")
#summaryGrouped(df)
#viewFull(df)  
#dataInfo(df)
#viewSummary(df)

'''# main menu 
print("Iris dataset main menu\n 1. For basic dataset information: press 1\n 3. To view the entire dataset: press 2\n 3. For the dataset summary: press 3")

# main program 
choice = input("Please select an option: ")

if choice == "1":
    print("The following is an overview of the data, displaying the first and last 5 lines of the dataframe")'''