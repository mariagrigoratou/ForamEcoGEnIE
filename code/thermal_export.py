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


df = pd.read_csv('E:PHD\\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\thermal_plot_export_average.csv')
df.shape
df.dtypes

#fig, (ax1)  = plt.subplots(nrows = 1, ncols = 1,  figsize = (15,15))
fig, (ax1)  = plt.subplots(figsize = (15,15))

###### define the colormap   ######
cmap = plt.cm.bwr

difference = df.pivot(index ='loc', columns ='to',values = ['diff_average_RCP6_2050','diff_average_RCP8.5_2050','diff_average_RCP6_2100', 'diff_average_RCP8.5_2100'])
#total_all = df.pivot(index ='loc', columns ='to',values = ['present_average', 'average_RCP6_2050','average_RCP8.5_2050','average_RCP6_2100', 'average_RCP8.5_2100'])

d = sns.heatmap(difference, vmin = -100, vmax = 100, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
				xticklabels=["a", "b", "c", "d"],cbar = True)

#ax1.set_ylabel("Geographic zones", size = 16)

#ax1.set_title("CaCO3 production")

fig.subplots_adjust(hspace=0.1, wspace=0.1) # adjust the space between the plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

fig.text(0.50, 0.95,
        "'Foraminifera carbonate production (CaCO3 y$^{-1}$) anomaly(future- present)",
        ha='center', fontsize = 16)
plt.show()


