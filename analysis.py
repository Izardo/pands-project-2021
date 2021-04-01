import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# ensure all rowns/columns are displayed when printed
# pd.set_option('display.max_rows', None, 'display.max_columns', None)

# reading in the data from the csv file
irisData = pd.read_csv('IRIS.csv')

# returns a tuple representing the dimensionaloty of the data frame
# irisData.shape

irisData.head()
#print(irisData)