# pands-project
Author JP Quinn
G00411303


For this project we were asked to study Fishers Iris data set, this is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus". From the amopunt of information online it seems this dataset has been studied by every data student at some stage. 

The dataset contains data from 3 species of Iris, Versicolor, Setosa and Virginica, the measuremenst in the data are the length and width of both the sepal and the petal, as part of the analysis.py project code I have written a brief summary of each of these variables in the file 'variables.txt' that is also to be found in the repository

CODE
with open('variables.txt','w') as f: 

    sl = ["\n","Sepal Length \n", "Measures the length of the sepal, which is each of the parts of the calyx of a flower, enclosing the petals and typically green and leaflike \n"]
    sw = ["\n", "Sepal Width \n", "Measures the width of the sepal\n"]
    pl = ["\n", "Petal Length \n", "The length of the petal, the petals are modified leaves that surround the reproductive parts of flowers \n"]
    pw = ["\n", "Petal width \n", "The width of the petals \n"]
    s = ["\n", "Species \n", "Shows which of the 3 iris species that the current data points to \n"]

in the 5 lines above I have typed a short description of the variables to be outputted on a text file. The \n function puts it onto a new line, keeping the file neat.

    f.write('A quick overview of the data variables \n')
    f.writelines(sl)
    f.writelines(sw)
    f.writelines(pl)
    f.writelines(pw)
    f.writelines(s)
    f.close()

The lines above write each of the variables to the text file and the f.close() closes the file

CODE
col = ['sepal_length','sepal_width','petal_length','petal_width','species'] 
iris = pd.read_csv('iris.csv', names=col)

I downloaded the iris data in csv format from http://archive.ics.uci.edu/ml/datasets/Iris, the file contained the data but no headers so the variable col contains headers and then names=col in the code assigns these to the file

CODE
avg= iris.groupby('species').mean()
print(avg) 

This code groups the data by species and the mean() function gives the average of the values, this prints the table below. From this we can see that the Setosa species looks to be the most easily identified by the narrow petal length and width. The other variables are all quite similar so we cannot easily identify versicolor or virginica

                 sepal_length  sepal_width  petal_length  petal_width
species
Iris-setosa             5.006        3.418         1.464        0.244
Iris-versicolor         5.936        2.770         4.260        1.326
Iris-virginica          6.588        2.974         5.552        2.026


CODE
versicolor = iris[iris['species'] == 'Iris-versicolor']  ##define each species, code adapted from datacamp module
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
plt.savefig('scatter petal.png')  ##savefig code found on https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/
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
plt.savefig('scatter sepal.png')
plt.show()

The above code plots 2 scatter charts, 1 showing the sepal length and width, and the other the petal. We use points to create a scatter for each seperate species and then plot length on the x axis against width on the y axis. The line plt.savefig('scatter sepal.png') then saves the png image of the plot, also saved in the repository. I prefer to show a grid on my charts which is plotted using plt.grid()

From the scatter plots we can get a visual confirmation that the setosa species is easier to identify with its narrow petals, however neither scatterplot can tell us much of use to seperate virginica or versicolor.

CODE
fig, axes = plt.subplots(1, 4, figsize=(15, 5)) 
fig.suptitle('Iris data')

df = iris[iris.species == 'Iris-versicolor'] 
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

For the next analysis I wanted to use a subplot to display a histogram of each of the 4 variables to see if we could learn anything of use. I had trouble getting this to work, I managed to adapt some code from https://cmdlinetips.com and got the charts working and then used a tutorial on https://python-graph-gallery.com to get them working as a subplot. The file has been saved as suplot.png in the repository. However the chart just brings the same conclusion as the previous data I had looked at. Setosa is easily identifiable, but it is difficult to seperate virginica and versicolor

CODE
sns.set_style("whitegrid")
sns.pairplot(iris,hue='species',size=2);
plt.savefig('pairplot.png') 
plt.show()

The last piece of code was adapted from code I stumbled when I was looking into subplots. Depressingly, the 3 lines of code make a much nicer set of charts than the ones I had previously spent hours researching and tinkering with. The result is saved as pairplot.png in the repository. Looking at this data it shows again that setosa is easy to seperate from the rest but you could make a more eductaed guess on the identity of virginica and versicolor based on  petal length. Virginica tends to have the longer petals and also the longer and wider sepal.


references
wikipedia: info on the fisher dataset
https://www.w3schools.com/python/python_file_write.asp:  helped write variable info to a file
https://www.adamsmith.haus/python/answers/how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python: Added column names to csv
https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/: explained how to get the average of the 4 variables for each species
https://www.marsja.se/how-to-save-a-seaborn-plot-as-a-file-e-g-png-pdf-eps-tiff/: Explained the savefig function
https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn:   Helped me create my subplot for my histograms
https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn: Helped with the creation of the histograms
https://pythonbasics.org/seaborn-pairplot/: Found the pairplot function from seaborn on here
www.datacamp.com: I have done a number of modules on here including a few using the iris data set and have done modules on Numpy, Matplotlib and seaborn which were a help with understanding the code.





