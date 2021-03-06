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

fig, (ax1,ax2,ax3,ax4)  = plt.subplots(nrows = 1, ncols = 4, sharex = True, sharey=False,  figsize = (15,15))


###### define the colormap   ######
cmap = plt.cm.bwr
#cax = plt.axes([0.83, 0.1, 0.020, 0.8]) #plt.axes((left, bottom, width, height), facecolor='w')


picophyto1 = df.pivot(index ='loc', columns ='to',values = ['picophyto1_RCP6_2050','picophyto1_RCP8p5_2050','picophyto1_RCP6_2100', 'picophyto1_RCP8p5_2100'])
picophyto = df.pivot(index ='loc', columns ='to',values = ['picophyto_RCP6_2050','picophyto_RCP8p5_2050','picophyto_RCP6_2100', 'picophyto_RCP8p5_2100'])
nanophyto = df.pivot(index ='loc', columns ='to',values = ['nanophyto_RCP6_2050','nanophyto_RCP8p5_2050','nanophyto_RCP6_2100', 'nanophyto_RCP8p5_2100' ])
microphyto = df.pivot(index ='loc', columns ='to',values = ['microphyto_RCP6_2050','microphyto_RCP8p5_2050','microphyto_RCP6_2100', 'microphyto_RCP8p5_2100' ])

# a = sns.heatmap(picophyto1, vmin = -100.0, vmax = 101.0, annot = True, annot_kws={"size": 7, "weight": "bold"}, linewidths=0.5, linecolor='grey', square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
					# xticklabels=["a", "b", "c", "d"], cbar = False)
a = sns.heatmap(picophyto1, vmin = -100.0, vmax = 101.0, annot = True, fmt=".0f",  linewidths=0.0, square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
					xticklabels=["a", "b", "c", "d"], cbar = False)

b = sns.heatmap(picophyto, vmin = -100.0, vmax = 100.0, annot=True, fmt=".0f", linewidths=.0, square = True, cmap = cmap, ax = ax2, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = False)
c = sns.heatmap(nanophyto, vmin = -100.0, vmax = 100.0, annot=True, fmt=".0f", linewidths=.0, square = True, cmap = cmap, ax = ax3, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = False)
d = sns.heatmap(microphyto, vmin = -100.0, vmax = 100.0, annot=True, fmt=".0f", linewidths=.0, square = True, cmap = cmap, ax = ax4, center=0, yticklabels = False,
					xticklabels=["a", "b", "c", "d"], cbar = True)

#ax1.set_ylabel("Geographic zones", size = 16)
ax1.set_title("picophyto 0.6 $\mu$m")
ax2.set_title("picophyto")
ax3.set_title("nanophyto")
ax4.set_title("microphyto")

fig.subplots_adjust(hspace=0.1, wspace=0.1) # adjust the space between the plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)


fig.text(0.50, 0.95,
        "Phytoplankton relative concentration anomaly (future- modern)",
        ha='center', fontsize = 16)



# fig.text(0.50, 0.03,
        # 'RCP scenarios',
        # ha='center', fontsize = 16)
plt.show()


