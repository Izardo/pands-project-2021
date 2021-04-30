# This program analyses the Iris data set

# Author: Isabella Doyle

# imports libraries and aliases each library for ease of use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# reads in csv file with pandas, converts it to a DataFrame object & assigns it to variable 'df'
df = pd.read_csv('IRIS.csv')

# Function saves variable summary to a text file | Ref: [1]
def saveSummaryToText(): # Creates a function called saveSummaryToText()
    # sys.stdout is used to print text to a text file inside the paranthesis are two -
    # parameters: file path & 'w' which opens a file for writing | Ref: [2]
    sys.stdout = open ('variableSummary.txt', 'w')
    print("\n")
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
    print("Summary Information")
    print("*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^")
    print("------------------------------------------------------------------------------")
    print("Preview of the first & last 5 records")
    print("------------------------------------------------------------------------------")
    print(df) # prints first & last 5 lines of dataset
    print("------------------------------------------------------------------------------")
    print("Basic Information (Data Shape, Data Types etc.)")
    print("------------------------------------------------------------------------------")
    print(df.info()) # prints useful information about the data set
    print("------------------------------------------------------------------------------")
    print("Statistical Summary of each Variable (Grouped by Species)")
    print("------------------------------------------------------------------------------")
    # decribe() displays a basic statistical summary of all variables & uses groupby() -
    # method to group by species, include='all' returns all columns | Ref: [3]
    print(df.groupby('species').describe(include='all'))
    print("------------------------------------------------------------------------------")
    print("Count of Species in Percentile")
    print("------------------------------------------------------------------------------")
    # accesses the species attribute in the data frame & returns the percentage of occurances -
    # per species.  normalize=True returns relative frequencies of the species attribute, -
    # dropna=False excludes counting of NaN(s) | Ref: [4]
    print(df['species'].value_counts(normalize=True, dropna=False)*100)

# Function prints contents of 'variableSummary.txt' file
def viewTextSummary(): # creates a function called viewTextSummary()
    # opens 'variableSummary.txt' file in read mode and assigns it to the variable text
    text = open('variableSummary.txt', 'r')
    # uses print statement & read() method to read & print contents of file
    print(text.read())

# Function prints full DataFrame
def viewFull(): # defines a function called viewFull()
    pd.set_option('display.max_rows', 150)
    print(df)

# General note: The plt.savefig() lines of code that save code to a specified path are - 
# commented out for improved CPU performance

# Function creates 4 box plots & opens them in a single window
def boxAll():
    sns.set(style="ticks") # sets style using the seaborn library
    plt.figure(figsize = (12,10)) # specifies figure size using matplotlib.pyplot
    plt.subplot(2,2,1) # creates subplot with parameters: rows, columns & index | Ref: [5][6]
    # boxplot() takes three parameters: x axis values, y axis values and the data frame -
    # that you will extract the data from
    sns.boxplot(x='species',y ='sepal_length',data=df)
    plt.subplot(2,2,2)
    sns.boxplot(x='species',y='sepal_width',data=df)
    plt.subplot(2,2,3)
    sns.boxplot(x='species',y='petal_length',data=df)
    plt.subplot(2,2,4)
    sns.boxplot(x='species',y='petal_width',data=df)
    # plt.savefig('pngs/boxplots.png')
    plt.show() # matplotlib opens a new window displaying the plots

# Function creates 4 violin plots & opens them in a single window
def violinAll():
    # similar syntax for creating box plots was used for creating violin plots, see above
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

# Splits the DataFrame into 3 (using pandas) by the "species" attribute so it can be -
# used for creating the histograms & pair plots | Ref: [7]
iris_setosa = df[df["species"] == "Iris-setosa"] # Extracts setosa records from the data set
iris_versicolor = df[df["species"] == "Iris-versicolor"] # extracts versicolor records from data set
iris_virginica = df[df["species"] == "Iris-virginica"] # extracts virginica records from data set

# This function plots a histogram & density plot for each attribute in the data set using seaborn -
# & matplotlib
def hist():
    # Plots sepal length using FacetGrid from the seaborn library with 4 parameters contained -
    # in parenthesis: the dataframe, the hue which seperates & colorcodes the distinct species, -
    # the height of the grid and legend_out=False places the legend inside rather than outside -
    # of the plot. map() applies a plotting function to the subset, in this case, "sepal length", -
    # distplot shows a distrbution line overlaying the histogram | Ref: [8][9]
    sns.FacetGrid(df,hue="species", height=6, legend_out=False).map(sns.distplot,"sepal_length").add_legend(fontsize=10)
    plt.title("Sepal Length Histogram & Density Plot") # adds a title to histogram
    plt.xlabel("Sepal Length in cm") # adds a label to the x axis
    plt.subplots_adjust(top=0.8)     # adds padding to the top of plot so the title is visible
    
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
    plt.show() # matplotlib opens 4 seperate windows displaying the plots just created

# Function creates a pairPlot for multivariate analysis of the data
def pairPlot():
    sns.set(style="darkgrid") # sets grid style using the seaborn library
    # pairPlot() plots relationships of two variables in a dataset & contains 2 parameters: 
    # the dataFrame and the hue (the hue seperates the species by colorcode). Ref: [10]
    sns.pairplot(df, hue="species")
    # plt.savefig('pngs/pairPlot') # saves the plot to the pngs folder under the name pairPlot
    plt.show() # matplotlib opens a winsow diplaying 12 plots

# main program
choice = "" # The variable 'choice' is defined and contains an empty string value so that the -
            # while loop below evaluates as True and the program proceeds to the next code block

# The while loop continuously executes until x is entered
while choice != "x": # when x is entered the while loop evaluates as False and the program ends
# The input method displays the information between the quotation marks, requesting the user to -
# input an option (1 to 6 or x to quit). The input is assigneed to the variable 'choice' as a string -
# # \n creates a new line
    choice = input("\n\nIris Data Set Menu \n\
        1. View basic summary information \n\
        2. View full data set \n\
        3. View boxplot \n\
        4. View violin plot \n\
        5. View histogram \n\
        6. View pair plot \n\n\
    Please select a menu option from 1-6 (x to quit): ")

# The if-else statement controls the flow of the program further and executes particular code blocks
# depending on the value contained in choice
    if choice == "1": # The value in the variable choice is compared to the string value to the right -
                      # of the equality operator, if they are the same the if statement evaluates to -
                      # true and the following block of code is executed 
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
        # The print statement is executed if none of the menu options were selected & advises them to 
        # select a menu option
# Executes when x is input by the user & the program terminates        
print("You have quit the program. Goodbye!") 

'''References:
[1] "Pandas.read_csv" Pandas, 29 Apr. 2021, https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
[2] "Python – stdin, stdout, and stderr" Ask Python, 29 Apr. 2021, https://www.askpython.com/python/python-stdin-stdout-stderr
[3] "Describe Function With Groupby Pandas (Python 3.5.1)" Stack Overflow, 29 Apr. 2021, https://stackoverflow.com/questions/40346436/describe-function-with-groupby-pandas-python-3-5-1
[4] "How can I turn those frequencies into percentages?" Stack Overflow, 29 Apr. 2021, https://stackoverflow.com/questions/14281871/given-a-pandas-series-that-represents-frequencies-of-a-value-how-can-i-turn-tho
[5] "matplotlib.pyplot.subplot" Matplotlib, 29 Apr. 2021, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
[6] "Box plot and Histogram exploration on Iris data" GeeksforGeeks, 29 Apr. 2021, https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
[7] "Indexing, Slicing and Subsetting DataFrames in Python" Data Carpentry, 29 Apr. 2021, https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html
[8] "Seaborn.FacetGrid" Seaborn, 28 Apr. 2021, https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
[9] "Seaborn Distplot" Python Basics, 28 Apr. 2021, https://pythonbasics.org/seaborn-distplot/#:~:text=Seaborn%20distplot%20lets%20you%20show,a%20univariate%20distribution%20of%20observations
[10] "Seaborn.pairplot" Seaborn, 29 Apr. 2021, https://seaborn.pydata.org/generated/seaborn.pairplot.html

Other resources:
"Options and settings", Pandas, 29 Apr. 2021, https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
"Exploratory Data Analysis: Uni-variate analysis of Iris Data set, Pratik Nabriya, 29 Apr. 2021, "https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40#:~:text=Iris%20data%20is%20a%20multivariate,and%20petal%20width%2C%20in%20centimeters.&text=It%20consists%20of%20a%20set,Class%2DLabels(Species).
"How to increase the font size of the legend in my Seaborn plot?", Stack Overflow, 29 Apr. 2021, https://stackoverflow.com/questions/44880444/how-to-increase-the-font-size-of-the-legend-in-my-seaborn-plot
"Seaborn Cheat Sheet", DataCamp, 29 Apr. 2021, https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf
"Matplotlib Labels and Title" W3 Schools, 29 Apr. 2021, https://www.w3schools.com/python/matplotlib_labels.asp'''
