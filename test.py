import numpy as np
import pandas as p
import seaborn as s


with open('iris.csv', newline='') as f:
  reader = csv.reader(f)
  row1 = next(reader)  # gets the first line
  # now do something here 
  # if first row is the header, then you can do one more next() to get the next row:
  # row2 = next(f)