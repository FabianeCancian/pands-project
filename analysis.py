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
#Save plot
plt.savefig('Histogram_Sepal_Lengh.png')
plt.show ()

#Defining sepal width to numpy
sepal_width = df['sepal_width'].to_numpy()
#Plotting Histogram
plt.hist(sepal_width, color='indigo', edgecolor= 'black')
# create title
plt.title('Sepal Widht Histogram')
#Save plot
plt.savefig('Histogram_Sepal_Widht.png')
plt.show ()

#Defining Petal Lenght to numpy
petal_length = df['petal_length'].to_numpy()
#Plotting Histogram
plt.hist(petal_length, color='indigo', edgecolor= 'black')
# create title
plt.title('Petal Lenght Histogram')
#Save plot
plt.savefig('Histogram_Petal_Lengh.png')
plt.show ()

#Defining Petal Lenght to numpy
petal_width = df['petal_width'].to_numpy()
#Plotting Histogram
plt.hist(petal_width, color='indigo', edgecolor= 'black')
# create title
plt.title('Petal Width Histogram')
#Save plot
plt.savefig('Histogram_Petal_widht.png')
plt.show ()

#Calculating Media of each variable
import statistics
#this funciton will calculate and write the mean of each variable on the dataset.
def mean ():
    f.write("This is the mean for sepal lenght: ")
    f.write(str(statistics.mean(sepal_length)) + '\n')
    f.write("This is the mean for sepal width: ")
    f.write(str(statistics.mean(sepal_width)) + '\n')
    f.write("This is the mean for petal lenght: ")
    f.write(str(statistics.mean(petal_length))+ '\n')
    f.write("This is the mean for petal width: ")
    f.write(str(statistics.mean(petal_width))+ '\n')

#Creating a file for the summary of each variable and write the output of the above function on the archive. 
f = open("variables.txt", "w")
mean()
f.close()