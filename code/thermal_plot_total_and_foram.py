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


df = pd.read_csv('thermal_plot.csv')
df.shape
df.dtypes

fig, (ax1,ax2,ax3, ax4)  = plt.subplots(nrows = 1, ncols = 4, sharex = True, sharey=False,  figsize = (15,15))
#fig, ax1 = plt.subplots(4,4, sharex='col', sharey='row', figsize=(15,15))

###### define the colormap   ######
cmap = plt.cm.bwr
#cax = plt.axes([0.83, 0.1, 0.020, 0.8]) #plt.axes((left, bottom, width, height), facecolor='w')



total = df.pivot(index ='loc', columns ='to',values = ['total_RCP6_2050','total_RCP8p5_2050','total_RCP6_2100', 'total_RCP8p5_2100'])
phyto = df.pivot(index ='loc', columns ='to',values = ['totalphyto_RCP6_2050','totalphyto_RCP8p5_2050','totalphyto_RCP6_2100', 'totalphyto_RCP8p5_2100' ])
zoo = df.pivot(index ='loc', columns ='to',values = ['totalzoo_RCP6_2050','totalzoo_RCP8p5_2050','totalzoo_RCP6_2100', 'totalzoo_RCP8p5_2100'])
foram = df.pivot(index ='loc', columns ='to',values = ['foram_RCP6_2050','foram_RCP8p5_2050','foram_RCP6_2100', 'foram_RCP8p5_2100'])


a = sns.heatmap(total, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
					xticklabels=["a", "b", "c", "d"], cbar = False)
b = sns.heatmap(phyto, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax2, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = False)
c = sns.heatmap(zoo, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax3, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = False)
d = sns.heatmap(foram, vmin = -100.0, vmax = 100.0, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax4, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = True)



#ax1.set_ylabel("Geographic zones", size = 16)
ax1.set_title("total plankton")
ax2.set_title("phyto")
ax3.set_title("zoo")
ax4.set_title("foram")


fig.subplots_adjust(hspace=0.1, wspace=0.1) # adjust the space between the plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)



fig.text(0.50, 0.95,
        "Plankton relative biomass anomaly (future- present)",
        ha='center', fontsize = 16)
plt.show()


