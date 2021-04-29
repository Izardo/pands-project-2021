# This program analyses the Iris data set

# Author: Isabella Doyle

# imports libraries and aliases each library for ease of use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# reads in csv file with pandas, converts it to a DataFrame object and assigns it to variable 'df'
df = pd.read_csv('IRIS.csv')

# Saving variable summary to a text file
def saveSummaryToText():
    sys.stdout = open ('variableSummary.txt', 'w') # sys.stout is standard output to text file
    print("\n")
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
    print("Summary Information")
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
    print("------------------------------------------------------------------------------")
    print("Preview of the first & last 5 records")
    print("------------------------------------------------------------------------------")
    print(df) # print(df) prints first and last 5 lines of dataset
    print("------------------------------------------------------------------------------")
    print("Basic Information (Data Shape, Data Types etc.)")
    print("------------------------------------------------------------------------------")
    print(df.info()) # prints useful information about data set
    print("------------------------------------------------------------------------------")
    print("Statistical Summary of each Variable (Grouped by Species)")
    print("------------------------------------------------------------------------------")
    # displays a basic statistical summary of all variables side-by-side
    print(df.groupby('species').describe(include='all')) # include='all' returns all columns
    print("------------------------------------------------------------------------------")
    print("Count of Species in Percentile")
    print("------------------------------------------------------------------------------")
    # returns the percentage of occurances per species
    print(df['species'].value_counts(normalize=True, dropna=False)*100) # dropna=False excludes counting of NaN(s)

# prints contents of 'variableSummary.txt' file
def viewTextSummary():
    text = open('variableSummary.txt', 'r') # opens 'variableSummary.txt' file in read mode and assigns it to the variable text
    print(text.read()) # uses print statement & read() method to read & print contents of file

# prints full DataFrame
def viewFull():
    pd.set_option('display.max_rows', 150)
    print(df)

# General note: The plt.savefig() lines of code are commented out for ease of use/CPU performance


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

def violinAll():
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

# splits the DataFrame into 3 by the "species" attribute so it can be used for creating the histograms & pair plots
iris_setosa = df[df["species"] == "Iris-setosa"] # extracts setosa records from the data set
iris_versicolor = df[df["species"] == "Iris-versicolor"] # extracts versicolor records from data set
iris_virginica = df[df["species"] == "Iris-virginica"] # extracts virginica records from data set
speciesList = [iris_setosa, iris_versicolor, iris_virginica]

# This function plots a histogram & density plot for each attribute in the data set using seaborn & matplotlib
def hist():
    # plots sepal length values
    sns.FacetGrid(df,hue="species", height=6, legend_out=False).map(sns.distplot,"sepal_length").add_legend(fontsize=10)   # increased legend fontsize # hue inclued each subset (species) of data in the plot
    plt.title("Sepal Length Histogram & Density Plot")
    plt.xlabel("Sepal Length in cm")
    plt.subplots_adjust(top=0.8)
    # plt.savefig('pngs/distinctHist_sepal_length') # saves pngs of plots in pngs folder
    # plots sepal width values
    sns.FacetGrid(df,hue="species", height=6, legend_out=False).map(sns.distplot,"sepal_width").add_legend(fontsize=10)
    plt.title("Sepal Width Histogram & Density Plot")
    plt.xlabel("Sepal width in cm")
    plt.subplots_adjust(top=0.8)
    # plt.savefig('pngs/distinctHist_sepal_width')
    # plots petal length values
    sns.FacetGrid(df,hue="species", height=6, legend_out=False).map(sns.distplot,"petal_length").add_legend(fontsize=10)
    plt.title("Petal Length Histogram & Density Plot")
    plt.xlabel("Petal length in cm")
    plt.subplots_adjust(top=0.8)
    # plt.savefig('pngs/distinctHist_petal_length')
    # plots petal width values
    sns.FacetGrid(df,hue="species", height=6, legend_out=False).map(sns.distplot,"petal_width").add_legend(fontsize=10)
    plt.title("Petal Width Histogram & Density Plot")
    plt.xlabel("Petal width in cm")
    plt.subplots_adjust(top=0.8)
    # plt.savefig('pngs/distinctHist_petal_width')
    # matplotlib opens 4 seperate windows displaying the plots just created
    plt.show()

def pairPlot():
    sns.set(style="darkgrid")
    sns.pairplot(df, hue="species")
    # plt.savefig('pngs/pairPlot') saves the plot to the pngs folder under the name pairPlot
    plt.show()

# splits the DataFrame into 3 by the "species" attribute so it can be used for creating the histograms & pair plots
iris_setosa = df[df["species"] == "Iris-setosa"]
iris_versicolor = df[df["species"] == "Iris-versicolor"]
iris_virginica = df[df["species"] == "Iris-virginica"]
speciesList = [iris_setosa, iris_versicolor, iris_virginica]

# main program

choice = "" # The variable 'choice' is defined and contains an empty string value so that the while loop 
            # below evaluates as True and the program proceeds to the appropriate stage

# The while loop continuously executes until x is entered
while choice != "x": # when x is entered the while loop evaluates as False and the program ends
# The input method displays the information between the quotation marks, requesting the user to
# input an option (1 to 6 or x to quit). The input is assigneed to the variable 'choice' as a string
    choice = input("\n\nIris Dataset Main Menu \n\
        1. View basic summary information \n\
        2. View full data set \n\
        3. View boxplot \n\
        4. View violin plot \n\
        5. View histogram \n\
        6. View pair plot \n\n\
    Please select a menu option from 1-6 (x to quit): ") # \n creates a new line

# The if-else statement controls the flow of the program further and executes particular code blocks
# depending on the value contained in choice
    if choice == "1": # The value in the variable choice is compared to the string value to the right of the equality operator, 
                      # if they are the same the if statement evaluates to true and the following block of code is executed 
        print("Viewing basic summary information: ") # Prints the string inside the quotation marks
        viewTextSummary() # Calls the viewTextSummary() function, executing the code contained within it
    elif choice == "2": 
        print("Full data set:")
        viewFull()
    elif choice == "3":
        print("\nBox plot displaying each variable in a new window (close window to continue):")
        boxAll()
    elif choice == "4":
        print("\nViolin plots displaying each variable (close window to continue):")
        violinAll()
    elif choice == "5":
        print("\nHistograms displaying each variable in 4 seperate windows (close windows to continue):")
        hist()
    elif choice == "6":
        print("Pair plots compares 2 variables:")
        pairPlot()
    else: # The else statement executes if all of the other statements evaluate to false
        print("\n\nYou have not entered a number between 1 and 6.") 
        # The print statement is executed if none of the menu options were selected & advises them to select a menu option
        
print("You have quit the program. Goodbye!") # Executes when x is input by the user & the program terminates

'''References:
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
https://www.askpython.com/python/python-stdin-stdout-stderr
https://stackoverflow.com/questions/40346436/describe-function-with-groupby-pandas-python-3-5-1
https://stackoverflow.com/questions/14281871/given-a-pandas-series-that-represents-frequencies-of-a-value-how-can-i-turn-tho
https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
boxAll # Adopted from: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40#:~:text=Iris%20data%20is%20a%20multivariate,and%20petal%20width%2C%20in%20centimeters.&text=It%20consists%20of%20a%20set,Class%2DLabels(Species).
https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40#:~:text=Iris%20data%20is%20a%20multivariate,and%20petal%20width%2C%20in%20centimeters.&text=It%20consists%20of%20a%20set,Class%2DLabels(Species).
https://stackoverflow.com/questions/44880444/how-to-increase-the-font-size-of-the-legend-in-my-seaborn-plot
https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
https://www.w3schools.com/python/matplotlib_labels.asp add legend'''
