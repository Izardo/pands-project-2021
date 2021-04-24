# This program analyses the Iris dataset

# Author: Isabella Doyle

# imports libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys          

# reads in csv file with pandas, converts it to a DataFrame object and assigns it to variable 'df'
# Source: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
df = pd.read_csv('IRIS.csv')

# splits the DataFrame into 3 by the "species" attribute
iris_setosa = df[df["species"] == "Iris-setosa"]
iris_versicolor = df[df["species"] == "Iris-versicolor"]
iris_virginica = df[df["species"] == "Iris-virginica"]
speciesList = [iris_setosa, iris_versicolor, iris_virginica]
# Saving variable summary to a text file
# Source: https://www.askpython.com/python/python-stdin-stdout-stderr
def variableTextSummary():
    sys.stdout = open ('variableSummary.txt', 'w') # sys.stout is standard output to text file
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
    print("Variable Summary")
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^") 
    print("------------------------------------------------------------------------------")
    print("Preview of the first & last 5 records in the set, data shape, data types etc.")
    print("------------------------------------------------------------------------------")    
    print(print(df)) # print(df) prints first and last 5 lines of dataset 
    print(df.info()) # prints useful information about data set 
    print("------------------------------------------------------------------------------")
    print("Statistical Summary of each Variable (Grouped by Species)")
    print("------------------------------------------------------------------------------")
    # displays a basic statistical summary of all variables side-by-side
    # Source: https://stackoverflow.com/questions/40346436/describe-function-with-groupby-pandas-python-3-5-1
    print(df.groupby('species').describe(include='all')) # include='all' returns all columns
    print("------------------------------------------------------------------------------")
    print("Percentage of Occurances of Species")
    print("------------------------------------------------------------------------------")
    # returns the percentage of occurances per species
    # Source: https://stackoverflow.com/questions/14281871/given-a-pandas-series-that-represents-frequencies-of-a-value-how-can-i-turn-tho
    print(df['species'].value_counts(normalize=True, dropna=False)*100) # dropna=False means it will not include counts of NaN

# prints contents of 'variableSummary.txt' file
def viewTextSummary():
    text = open('variableSummary.txt', 'r') # opens 'variableSummary.txt' file in read mode and assigns it to the variable text
    print(text.read()) # uses print statement & read() method to read & print contents of file

# prints full DataFrame
# Source: https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
def viewFull():
    pd.set_option('display.max_rows', 150)
    print(df)

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

# https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40#:~:text=Iris%20data%20is%20a%20multivariate,and%20petal%20width%2C%20in%20centimeters.&text=It%20consists%20of%20a%20set,Class%2DLabels(Species).
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

def pairScatter():
    sns.set(style="darkgrid")
    sns.pairplot(df, hue="species")
    # plt.figure(figsize=(1,1))
    plt.savefig('pairPlot')
    plt.show()

# This function plots a histogram & density plot for each attribute
# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# adapted from: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40#:~:text=Iris%20data%20is%20a%20multivariate,and%20petal%20width%2C%20in%20centimeters.&text=It%20consists%20of%20a%20set,Class%2DLabels(Species).
# change legend font size: https://stackoverflow.com/questions/44880444/how-to-increase-the-font-size-of-the-legend-in-my-seaborn-plot
def hist():
    # plots sepal length values
    sns.FacetGrid(df,hue="species",height=7).map(sns.distplot,"sepal_length").add_legend(fontsize=12)   # increased legend fontsize
    plt.savefig('pngs/distinctHist_sepal_length')
    # plots sepal width values
    sns.FacetGrid(df,hue="species",height=7).map(sns.distplot,"sepal_width").add_legend(fontsize=12)
    plt.savefig('pngs/distinctHist_sepal_width')
    # plots petal length values
    sns.FacetGrid(df,hue="species",height=7).map(sns.distplot,"petal_length").add_legend(fontsize=12)
    plt.savefig('pngs/distinctHist_petal_length')
    # plots petal width values
    sns.FacetGrid(df,hue="species",height=7).map(sns.distplot,"petal_width").add_legend(fontsize=12)
    # saves pngs of plots in pngs folder
    plt.savefig('pngs/distinctHist_petal_width') 
    # matplotlib opens 4 seperate windows displaying the plots just created
    plt.show()                           

#variableTextSummary()
viewTextSummary()

'''# main menu 
print("Iris dataset main menu\n 1. For basic dataset information: press 1\n 3. To view the entire dataset: press 2\n 3. For the dataset summary: press 3")

# main program 
choice = input("Please select an option: ")

if choice == "1":
    print("The following is an overview of the data, displaying the first and last 5 lines of the dataframe")'''