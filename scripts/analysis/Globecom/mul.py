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

plt.figure(figsize=(20, 3.5))
plt.suptitle('Link K',x= 0.23, y= 0.86, fontsize=19)

plt.plot(kdisabled,color='#FF7F0E',lw=1, label='Disabled')
plt.fill_between(list(range(x)), 0,  sin,color='#FF7F0E')
plt.plot(kenabled/3, color='#1F77B4',lw=1, label='Enabled')
plt.fill_between(list(range(x)), 0,  con, color='#1F77B4')

plt.legend(loc='upper right')

plt.xlim(0,15500)
plt.xticks(np.arange(0, 15500, 1925), ['0', '1925', '3850', '5775', '7700', '9625', '11550', '13475', '15400'])
plt.ylim(0,4992)
plt.yticks(np.arange(0, 6864, 624), ['0', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%', '50%'])

plt.show()







