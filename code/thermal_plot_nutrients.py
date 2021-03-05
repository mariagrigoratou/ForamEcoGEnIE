#from mpl_toolkits.basemap import Basemap
import string
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import pandas as pd
import csv
import matplotlib.patches as mpatches
from matplotlib import style
#style.use('ggplot')
import seaborn as sns 


df = pd.read_csv('E:\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\thermal_plot.csv')
df.shape
df.dtypes

fig, (ax1,ax2)  = plt.subplots(nrows = 1, ncols = 2, sharex = True, sharey=False,  figsize = (15,15))
#fig, ax1 = plt.subplots(4,4, sharex='col', sharey='row', figsize=(15,15))

###### define the colormap   ######
cmap = plt.cm.bwr
#cax = plt.axes([0.83, 0.1, 0.020, 0.8]) #plt.axes((left, bottom, width, height), facecolor='w')



Fe = df.pivot(index ='loc', columns ='to',values = ['Fe_RCP6_2050','Fe_RCP8p5_2050','Fe_RCP6_2100', 'Fe_RCP8p5_2100'])
PO4 = df.pivot(index ='loc', columns ='to',values = ['PO4_RCP6_2050','PO4_RCP8p5_2050','PO4_RCP6_2100', 'PO4_RCP8p5_2100'])


a = sns.heatmap(Fe, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
					xticklabels=["a", "b", "c", "d"], cbar = False)
b = sns.heatmap(PO4, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax2, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = True)



#ax1.set_ylabel("Geographic zones", size = 16)
ax1.set_title("Fe")
ax2.set_title("PO4")



fig.subplots_adjust(hspace=0.1, wspace=0.1) # adjust the space between the plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)



fig.text(0.50, 0.95,
        "Nutrient concentration relative anomaly (future- present)",
        ha='center', fontsize = 16)
plt.show()


