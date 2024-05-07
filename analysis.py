#Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#Importing data from csv file
df = pd.read_csv('IrisDataset.csv')
#Defining sepal lengh to numpy
sepal_length = df['sepal_length'].to_numpy()

#Plotting Histogram
plt.hist(sepal_length, color='indigo', edgecolor= 'black')
# create title
plt.title('Sepal Lengh Histogram')
plt.show ()
#Save plot
plt.savefig('Histogram_Sepal_Lengh.png')

#Defining sepal width to numpy
sepal_width = df['sepal_width'].to_numpy()
#Plotting Histogram
plt.hist(sepal_width, color='indigo', edgecolor= 'black')
# create title
plt.title('Sepal Widht Histogram')
plt.show ()
#Save plot
plt.savefig('Histogram_Sepal_Widht.png')

#Defining Petal Lenght to numpy
petal_length = df['petal_length'].to_numpy()
#Plotting Histogram
plt.hist(petal_length, color='indigo', edgecolor= 'black')
# create title
plt.title('Petal Lenght Histogram')
plt.show ()
#Save plot
plt.savefig('Histogram_Petal_Lengh.png')

#Defining Petal Lenght to numpy
petal_width = df['petal_width'].to_numpy()
#Plotting Histogram
plt.hist(petal_width, color='indigo', edgecolor= 'black')
# create title
plt.title('Petal Width Histogram')
plt.show ()
#Save plot
plt.savefig('Histogram_Petal_widht.png')