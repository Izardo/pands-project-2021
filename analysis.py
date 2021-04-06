# This program analyses the Iris dataset

# Author: Isabella Doyle
# imports libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reads in csv file and assigns data to variable 'df'
df = pd.read_csv('IRIS.csv')

# Functions to access basic info about the dataset
def dataInfo(x): 
    print(x)            # print(df) prints first and last 5 lines of dataset
    x = df.info()
    print(x)

# prints full dataset
def viewFull(x):
    pd.set_option('display.max_rows', 150)
    print(x)

# view summary shows basic statistical information
def viewSummary(x):
    describe = x.describe()
    print(describe)
   
#dataInfo(df)
#viewSummary(df)

'''# main menu 
print("Iris dataset main menu\n 1. For basic dataset information: press 1\n 3. To view the entire dataset: press 2\n 3. For the dataset summary: press 3")

# main program 
choice = input("Please select an option: ")

if choice == "1":
    print("The following is an overview of the data, displaying the first and last 5 lines of the dataframe")'''