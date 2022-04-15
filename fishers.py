##pand-project
##Author JP Quinn

import numpy as np
import pandas as p
import seaborn as sb

from matplotlib import pyplot as plot

def import_csv():

    data = p.read_csv('iris.csv')
    data.columns=['sepal_length','sepal_width','petal_length','petal_width', 'species']

    return data
    


