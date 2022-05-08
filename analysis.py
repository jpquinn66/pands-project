##pand-project
##Author JP Quinn
##G00411303


from itertools import groupby 
import numpy as np
from  matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import csv
##import of all the packages required for this project

with open('variables.txt','w') as f: ##method adapted from https://www.w3schools.com/python/python_file_write.asp


##assigns text to variables and then writes lines to a text code. \n pushes to a new line

    sl = ["\n","Sepal Length \n", "Measures the length of the sepal, which is each of the parts of the calyx of a flower, enclosing the petals and typically green and leaflike \n"]
    sw = ["\n", "Sepal Width \n", "Measures the width of the sepal\n"]
    pl = ["\n", "Petal Length \n", "The length of the petal, the petals are modified leaves that surround the reproductive parts of flowers \n"]
    pw = ["\n", "Petal width \n", "The width of the petals \n"]
    s = ["\n", "Species \n", "Shows which of the 3 iris species that the current data points to \n"]
    f.write('A quick overview of the data variables \n')
    f.writelines(sl)
    f.writelines(sw)
    f.writelines(pl)
    f.writelines(pw)
    f.writelines(s)
    f.close()

col = ['sepal_length','sepal_width','petal_length','petal_width','species'] ## data has no column names so adding column names, method adapted from code on https://www.adamsmith.haus/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python
iris = pd.read_csv('iris.csv', names=col)

avg= iris.groupby('species').mean() ##prints mean values for each dataset, grouped by species https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
print(avg) 

versicolor = iris[iris['species'] == 'Iris-versicolor']  ##define each species, code adapted from datacamp module
setosa = iris[iris['species'] == 'Iris-setosa']
virginica = iris[iris['species'] == 'Iris-virginica']

fig, ax = plt.subplots()  ##create scatterplot that sets a colour for each species and labels them. 
points = ax.scatter(versicolor['petal_length'], versicolor['petal_width'], label='Versicolor')
points.set_facecolor('purple')
ax.scatter(setosa['petal_length'], setosa['petal_width'], label='Setosa', facecolor='blue')
ax.scatter(virginica['petal_length'], virginica['petal_width'], label='Virginica', facecolor='red')

ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.set_title('Iris Petal Sizes')
ax.legend()  ##adds legend
plt.grid()  ##adds grid to chart
plt.savefig('scatterpetal.png')  ##savefig saves a png file of the scatterplot code found on https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/
plt.show()

fig, ax = plt.subplots()
points = ax.scatter(versicolor['sepal_length'], versicolor['sepal_width'], label='Versicolor')
points.set_facecolor('purple')
ax.scatter(setosa['sepal_length'], setosa['sepal_width'], label='Setosa', facecolor='blue')
ax.scatter(virginica['sepal_length'], virginica['sepal_width'], label='Virginica', facecolor='red')

ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_title('Iris Sepal Sizes')
ax.legend()
plt.grid()
plt.savefig('scattersepal.png')
plt.show()


fig, axes = plt.subplots(1, 4, figsize=(15, 5)) ##subplots here puts all charts on the one image file https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn
fig.suptitle('Iris data')

df = iris[iris.species == 'Iris-versicolor'] ##https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn
sns.distplot(df['sepal_length'], hist=False,  kde=True, label='Versicolor',color='black', ax=axes[0])
df = iris[iris.species == 'Iris-setosa']
sns.distplot(df['sepal_length'],hist=False,  kde=True, label='Setosa', ax = axes[0])
df =iris[iris.species == 'Iris-virginica']
sns.distplot(df['sepal_length'],hist=False,  kde=True, label='Virginica', ax = axes[0])
plt.legend(prop={'size': 12})
plt.title('Sepal length by species')

sns.distplot(df['sepal_width'], hist=False,  kde=True, label='Versicolor',color='black', ax=axes[1])
df =iris[iris.species == 'Iris-setosa']
sns.distplot(df['sepal_width'],  hist=False,  kde=True, label='Setosa', ax=axes[1])
df =iris[iris.species == 'Iris-virginica']
sns.distplot(df['sepal_width'],  hist=False,  kde=True, label='Virginica', ax = axes[1])
plt.legend(prop={'size': 12})
plt.title('Sepal width by species')

sns.distplot(df['petal_length'], hist=False,  kde=True, label='Versicolor', color='black',ax = axes[2])
df = iris[iris.species == 'Iris-setosa']
sns.distplot(df['petal_length'],  hist=False,  kde=True, label='Setosa', ax = axes[2])
df = iris[iris.species == 'Iris-virginica']
sns.distplot(df['petal_length'],  hist=False,  kde=True, label='Virginica', ax = axes[2])
plt.legend(prop={'size': 12})
plt.title('Petal length by species')

sns.distplot(df['petal_width'],  hist=False,  kde=True, label='Versicolor', color='black',ax = axes[3])
df = iris[iris.species == 'Iris-setosa']
sns.distplot(df['petal_width'],  hist=False,  kde=True, label='Setosa', ax = axes[3])
df = iris[iris.species == 'Iris-virginica']
sns.distplot(df['petal_width'],  hist=False,  kde=True, label='Virginica', ax = axes[3])
plt.legend(prop={'size': 12})
plt.title('Petal width by species')
plt.grid()
plt.savefig('subplot.png') 
plt.show() 

sns.set_style("whitegrid")  ##sets background of the chart to a white grid
sns.pairplot(iris,hue='species',size=2);    ##creates pairplot from seaborn
plt.savefig('pairplot.png') 
plt.show() ##https://pythonbasics.org/seaborn-pairplot/
