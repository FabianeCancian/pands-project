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

# this function will calculate and write the median of each variable on dataset. 
def median ():
    f.write("This is the median for sepal lenght: ")
    f.write(str(statistics.median(sepal_length)) + '\n')
    f.write("This is the median for sepal width: ")
    f.write(str(statistics.median(sepal_width)) + '\n')
    f.write("This is the median for petal lenght: ")
    f.write(str(statistics.median(petal_length))+ '\n')
    f.write("This is the median for petal width: ")
    f.write(str(statistics.median(petal_width))+ '\n')

# this function will calculate and write the median of each variable on dataset. 
def mode ():
    f.write("This is the mode for sepal lenght: ")
    f.write(str(statistics.mode(sepal_length)) + '\n')
    f.write("This is the mode for sepal width: ")
    f.write(str(statistics.mode(sepal_width)) + '\n')
    f.write("This is the mode for petal lenght: ")
    f.write(str(statistics.mode(petal_length))+ '\n')
    f.write("This is the mode for petal width: ")
    f.write(str(statistics.mode(petal_width))+ '\n')

#Creating a file for the summary of each variable and write the output of the above functions on the archive. 
f = open("variables.txt", "w")
mean()
median ()
mode()
f.close()

#Scatter plots
import seaborn as sns
iris = sns.load_dataset('iris')

# Data preprocessing
# Separate features and target variable
X = iris.drop('species', axis=1)
y = iris['species']

# Data processing
# Perform any necessary data processing steps here

# Data analysis
# Calculate summary statistics
summary_stats = X.describe()
print("Summary Statistics:")
print(summary_stats)

# Plot the graph using Seaborn and Matplotlib
sns.set(style="ticks")
sns.pairplot(iris, hue="species", palette='mako')
plt.savefig('Scatterplot_sepal.png')
plt.show ()