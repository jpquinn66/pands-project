##pand-project
##Author JP Quinn

from itertools import groupby
import numpy as np
from  matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import csv

with open('variables.txt','w') as f:

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

col = ['sepal_length','sepal_width','petal_length','petal_width','species'] ## data has no column names so adding ala https://www.adamsmith.haus/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python
iris = pd.read_csv('iris.csv', names=col)

versicolor = iris[iris['species'] == 'Iris-versicolor']
setosa = iris[iris['species'] == 'Iris-setosa']
virginica = iris[iris['species'] == 'Iris-virginica']

fig, ax = plt.subplots()
points = ax.scatter(versicolor['petal_length'], versicolor['petal_width'], label='Versicolor')
points.set_facecolor('purple')
ax.scatter(setosa['petal_length'], setosa['petal_width'], label='Setosa', facecolor='blue')
ax.scatter(virginica['petal_length'], virginica['petal_width'], label='Virginica', facecolor='red')

ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.set_title('Iris Petal Sizes')
ax.legend()
plt.grid()
plt.show()

sl = iris['sepal_length'].tolist()
sw = iris['sepal_width'].tolist()
pl = iris['petal_length'].tolist()
pw = iris['petal_width'].tolist()
c = iris['species'].tolist()

df = iris[iris.species == 'Iris-versicolor'] ##https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn
sns.distplot(df['sepal_length'],  kde=False, label='Versicolor')
df = iris[iris.species == 'Iris-setosa']
sns.distplot(df['sepal_length'],  kde=False, label='Setosa')
df = iris[iris.species == 'Iris-virginica']
sns.distplot(df['sepal_length'],  kde=False, label='Virginica')
plt.legend(prop={'size': 12})
plt.title('Sepal length by species')
plt.grid()
plt.show()



##sns.FacetGrid(iris,hue='species',size=3).map(sns.distplot,'petal_length').add_legend()
##plt.show()

sns.violinplot(x='species',y='petal_length',data=iris)
plt.show()


##sns.set_style('whitegrid')
##iris = sns.load_dataset('iris')
##sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
##plt.legend(loc='lower right')
##plt.savefig('scatter.png')   ##savefig code found on https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/
##plt.show()

