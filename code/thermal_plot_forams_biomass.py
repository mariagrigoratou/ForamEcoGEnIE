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


df = pd.read_csv('thermal_plot_forams.csv')
df.shape
df.dtypes

fig, (ax1)  = plt.subplots(figsize = (15,15))

###### define the colormap   ######
cmap = plt.cm.bwr

foram = df.pivot(index ='loc', columns ='to',values = ['foram_RCP6_2050','foram_RCP8p5_2050','foram_RCP6_2100', 'foram_RCP8p5_2100'])


d = sns.heatmap(foram, vmin = -100, vmax = 100, annot=True, linewidths=.0, square = True, cmap = cmap, ax = ax1, center=0, yticklabels = True,
				xticklabels=["a", "b", "c", "d"],cbar = True)

#ax1.set_ylabel("Geographic zones", size = 16)

#ax1.set_title("CaCO3 production")

fig.subplots_adjust(hspace=0.1, wspace=0.1) # adjust the space between the plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

fig.text(0.50, 0.95,
        "'Foraminifera carbonate production (CaCO3 y$^{-1}$) anomaly(future- present)",
        ha='center', fontsize = 16)
plt.show()


