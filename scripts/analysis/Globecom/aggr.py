import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

aggrenabled = pd.read_csv("aggrenabled.txt",delimiter='|',usecols=[3],skiprows=12)
aggrdisabled = pd.read_csv("aggrdisabled.txt",delimiter='|',usecols=[3],skiprows=12)

sin = [x[0] for x in aggrdisabled.values.tolist()]
con = [x[0] for x in aggrenabled.values.tolist()]
con= np.array(con)/3
 

x = len(aggrenabled)

plt.figure(figsize=(9, 3.5))
plt.suptitle('Aggregated',x= 0.24, y= 0.86, fontsize=24)

plt.plot(aggrdisabled,color='#FF7F0E',lw=1, label='Disabled')
plt.fill_between(list(range(x)), 0,  sin,color='#FF7F0E')
plt.plot(aggrenabled/3, color='#1F77B4',lw=1, label='Enabled')
plt.fill_between(list(range(x)), 0,  con, color='#1F77B4')



plt.xlim(0,15500)
plt.xticks(np.arange(0, 15500, 1925), ['0', '1925', '3850', '5775', '7700', '9625', '11550', '13475', '15400'], fontsize=16)
plt.ylim(0,5616)
plt.yticks(np.arange(0, 6864, 624), ['0', '5%', '', '15%', '', '25%', '', '35%', '', '45%', ''], fontsize=16)

plt.show()







