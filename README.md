# pands-project-2021

Project Introduction

This project was undertaken as part of the Programming and Scripting assessment module, which is a core module in the Higher Diploma in Data Analytics at the Galway-Mayo Institute of Technology. 

Project Objectives

Research the data set and write a summary about it.

The project description can be found at the following link: https://learnonline.gmit.ie/pluginfile.php/282709/mod_label/intro/Project%202021.pdf 

Tools used

Python 3.7

VSCode

Numpy

Matplotlib

Intro to Fisher’s Iris Data Set

Acquiring the data

Dataset obtained from: https://www.kaggle.com/arshid/iris-flower-dataset

Getting a feel for the data:

The dataInfo() function returns some basic information about the dataset. Firstly, it reutrns the first and last 5 lines of the dataset and further, using the pandas df.info() function, it tells us the type of data we are dealing with that is, a DataFrame, which is a 2-dimensional array with 150 columns and 5 rows. It tells us that there are 5 columns (or attributes): 4 of which are quantitative, sepal_length, sepal_width, petal_length, petal_width, while one, species, is categorical. Further, it returns the data type of each attribute. The quantitative are all of type float64 and the categorical is of object type. This will determine what type of analysis we can perform on the data. Next, it returns the memory usage of the dataset, which is 6.0KB. Finally, we can see that there are no non-null values in our dataset which ensures data integrity and prevents potentially inaccurate conclusions.


REFERENCES: 

"Using Pandas and Python to Explore Your Dataset"
by Reka Horvath
https://realpython.com/pandas-python-explore-dataset/ Accessed: 1/4/21