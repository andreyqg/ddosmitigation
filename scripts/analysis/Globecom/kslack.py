import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

kenabled = pd.read_csv("kenabled.txt",delimiter='|',usecols=[3],skiprows=12)
kdisabled = pd.read_csv("kdisabled.txt",delimiter='|',usecols=[3],skiprows=12)

sin = [x[0] for x in kdisabled.values.tolist()]
con = [x[0] for x in kenabled.values.tolist()]
con= np.array(con)/3

x = len(kenabled)


y = np.vstack([sin,con])

labels = ["Disabled ", "Enabled"]

fig, ax = plt.subplots()
ax.stackplot(list(range(x)), sin, con, labels=labels)
ax.legend(loc='upper left')
plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()








