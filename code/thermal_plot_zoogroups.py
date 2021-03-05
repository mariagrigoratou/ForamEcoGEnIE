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

fig, (ax1,ax2, ax3, ax4)  = plt.subplots(nrows = 1, ncols = 4, sharex = True, sharey=False,  figsize = (15,15))


###### define the colormap   ######
cmap = plt.cm.bwr
#cax = plt.axes([0.83, 0.1, 0.020, 0.8]) #plt.axes((left, bottom, width, height), facecolor='w')
zoo190 = df.pivot(index ='loc', columns ='to',values = ['190umzoo_RCP6_2050','190umzoo_RCP8p5_2050','190umzoo_RCP6_2100', '190umzoo_RCP8p5_2100'])
nanozoo = df.pivot(index ='loc', columns ='to',values = ['nanozoo_RCP6_2050','nanozoo_RCP8p5_2050','nanozoo_RCP6_2100', 'nanozoo_RCP8p5_2100'])
microzoo = df.pivot(index ='loc', columns ='to',values = ['microzoo_RCP6_2050','microzoo_RCP8p5_2050','microzoo_RCP6_2100', 'microzoo_RCP8p5_2100'])
mesozoo = df.pivot(index ='loc', columns ='to',values = ['mesozoo_RCP6_2050','mesozoo_RCP8p5_2050','mesozoo_RCP6_2100', 'mesozoo_RCP8p5_2100'])

a = sns.heatmap(zoo190, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
					xticklabels=["a", "b", "c", "d"], cbar = False)

d = sns.heatmap(nanozoo, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax2, center=0, yticklabels = True,
					xticklabels=["a", "b", "c", "d"], cbar = False)
e = sns.heatmap(microzoo, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax3, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = False)
f = sns.heatmap(mesozoo, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax4, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = True)


#ax1.set_ylabel("Geographic zones", size = 16)
ax1.set_title("microzo 190 $\mu$m")
ax2.set_title("nanozoo")
ax3.set_title("microzoo")
ax4.set_title("mesozoo")


fig.subplots_adjust(hspace=0.1, wspace=0.1) # adjust the space between the plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)



fig.text(0.50, 0.95,
        "Zooplankton relative biomass anomaly (future- present)",
        ha='center', fontsize = 16)


plt.show()


