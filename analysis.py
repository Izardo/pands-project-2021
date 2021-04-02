import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('IRIS.csv')

# access basic info
def dataInfo(x):
    print(x)
    x = df.info()
    print(x)

def viewFull(x):
    pd.set_option('display.max_rows', 150)
    print(x)

# view summary

# main menu 
print("Iris dataset main menu\n 1. For basic dataset information: press 1\n 3. To view the entire dataset: press 2\n 3. For the dataset summary: press 3")

# main program 
choice = input("Please select an option: ")

if choice == "1":
    print("The following is an overview of the data, displaying the first and last 5 lines of the dataframe")