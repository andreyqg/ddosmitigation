import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

nenabled = pd.read_csv("nenabled.txt",delimiter='|',usecols=[3],skiprows=12)
ndisabled = pd.read_csv("ndisabled.txt",delimiter='|',usecols=[3],skiprows=12)

sin = [x[0] for x in ndisabled.values.tolist()]
con = [x[0] for x in nenabled.values.tolist()]
con= np.array(con)/3

x = len(nenabled)

plt.figure(figsize=(9, 3.5))
plt.suptitle('Link N',x= 0.23, y= 0.86, fontsize=24)

plt.plot(ndisabled,color='#FF7F0E',lw=1, label='Disabled')
plt.fill_between(list(range(x)), 0,  sin,color='#FF7F0E')
plt.plot(nenabled/3, color='#1F77B4',lw=1, label='Enabled')
plt.fill_between(list(range(x)), 0,  con, color='#1F77B4')


plt.xlim(0,15500)
plt.xticks(np.arange(0, 15500, 1925), ['0', '1925', '3850', '5775', '7700', '9625', '11550', '13475', '15400'], fontsize=16)
plt.ylim(0,4992)
plt.yticks(np.arange(0, 6864, 624), ['0', '5%', '', '15%', '', '25%', '', '35%', '', '45%', ''], fontsize=16)

plt.show()







