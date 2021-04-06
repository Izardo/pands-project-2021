# pands-project-2021

### Project Introduction

This project was undertaken as part of the Programming and Scripting assessment module, which is a core module in the Higher Diploma in Data Analytics at the Galway-Mayo Institute of Technology. 

#### Project Objectives

Research the data set and write a summary about it.

The project description can be found at the following link: https://learnonline.gmit.ie/pluginfile.php/282709/mod_label/intro/Project%202021.pdf 

### Tools used

Python 3.7

VSCode

Numpy

Matplotlib

### 1.0 Intro to Fisher’s Iris Data Set

Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica

### 1.1 Acquiring the data

[Add some basic info about kaggle here]
Dataset obtained from: https://www.kaggle.com/arshid/iris-flower-dataset

### 1.3 Getting a feel for the data:

#### Basic Statistical Analysis

First, we must import all of libraries needed for our analysis. 
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
Next, we load our IRIS.csv file with pandas. CSV stands for comma-seperated value and this file type is commonly used in data analysis. Pandas is a very useful way to manipulate data and CSV files, while DataFrames are pandas way of storing 2 dimensional data.[1]
```
df = pd.read_csv('IRIS.csv')
```

Simply using the print() function with the name of the DataFrame in the brackets will allow  you to preview the data, printing the first and last 5 rows of the dataset.

![Preview data set](screenshots/print(df).png "Preview")

The info() function from the pandas library prints prints a concise summary about the dataframe.[2]

![Screenshot of consice summary output](screenshots/info().png "Concise summary")

 and further, using the pandas df.info() function, it tells us the type of data we are dealing with that is, a DataFrame, which is a 2-dimensional array with 150 columns and 5 rows. It tells us that there are 5 columns (or attributes): 4 of which are quantitative, sepal_length, sepal_width, petal_length, petal_width, while one, species, is categorical. Further, it returns the data type of each attribute. Moreover, the first four attributes are known as independent variables while the class label is known as dependent. 

The quantitative are all of type float64 and the categorical is of object type. This will determine what type of analysis we can perform on the data. Next, it returns the memory usage of the dataset, which is 6.0KB. Finally, we can see that there are no non-null values in our dataset which ensures data integrity and prevents potentially inaccurate conclusions.

The pd.set_option() function allows us to view the entire dataset (i.e., 150 rows and 5 columns). It takes in two parameters: pat (a specified option) and value (in our case, the amount of rows we wish to display).[3]

```
def dataInfo(x):
    print(x)
    x = df.info()
    print(x) 
```

References: 

[1] "Python Pandas read_csv – Load Data from CSV Files" Shane Lynn, 6 Apr. 2021, www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
[2] 4 Apr. 2021, https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
[3] 4 Apr. 2021, https://pandas.pydata.org/docs/reference/api/pandas.set_option.html

"Using Pandas and Python to Explore Your Dataset" Reka Horvath, 1 Apr. 2021, https://realpython.com/pandas-python-explore-dataset/