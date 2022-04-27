##pand-project
##Author JP Quinn


from re import S
from tkinter import W
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

col = ['sepal_length','sepal_width','petal_length','petal_width','species']
idata = pd.read_csv('iris.csv', names=col)


spl = list(idata[['sepal_length']])
spw = list(idata[['sepal_width']])
pl = list(idata[['petal_length']])
pw = list(idata[['petal_width']])

w = np.array(idata[spl])
x = np.array(idata[spw])
y = np.array(idata[pl])
z = np.array(idata[pw])

plt.hist(w)
plt.show()

plt.hist(x)
plt.show()

plt.hist(y)
plt.show()

plt.hist(z)
plt.show()




