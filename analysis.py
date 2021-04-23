# This program analyses the Iris dataset

# Author: Isabella Doyle

# imports libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys          

# MAIN PROGRAM
# reads in csv file and assigns data to variable 'df'
df = pd.read_csv('IRIS.csv')

# splits the DataFrame into 3 by the "species" attribute
iris_setosa = df[df["species"] == "Iris-setosa"]
iris_versicolor = df[df["species"] == "Iris-versicolor"]
iris_virginica = df[df["species"] == "Iris-virginica"]
speciesList = [iris_setosa, iris_versicolor, iris_virginica] 

# Saving summary statistics to a text file
def summaryText():
    sys.stdout = open ('variableSummary.txt', 'w') # sys.stout is standard output file # with open opens file and then closes it when finished
    print(dataInfo())
    print(summaryAll())
    print(summaryBySpecies())
    print(countSpecies())

# Function to access basic info about the dataset
def dataInfo():   
    print(df)               # print(df) prints first and last 5 lines of dataset     
    df.info()               # prints useful information about data set

# view summary shows basic statistical information
# may not be needed but gives us an instant range of values to familariase ourselves with the data
def summaryAll():
    print(df.describe())

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html
def countSpecies():                         # counts unique values in the column 'species'
    print(df['species'].value_counts())     # returns the count of instances of each unique value
    print(df['species'].value_counts(normalize=True, dropna=False)*100)  # return the percentage of occurances of each species, dropna=False means it will not include counts of NaN
# https://stackoverflow.com/questions/14281871/given-a-pandas-series-that-represents-frequencies-of-a-value-how-can-i-turn-tho


# prints full dataset to compare against Fisher's 
def viewFull():
    pd.set_option('display.max_rows', 150) # https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
    print(df)

# side-by-side summary of species
# REF: Describe Function With Groupby Pandas (Python 3.5.1), 7 Apr. 2021, ayhan,
# https://stackoverflow.com/questions/40346436/describe-function-with-groupby-pandas-python-3-5-1
def summaryBySpecies():
    summary = df.groupby('species').describe()
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

countSpecies()
#summaryText()
# hist()
#pairScatter()
# calling the functions
# boxAll()
# allViolin()
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