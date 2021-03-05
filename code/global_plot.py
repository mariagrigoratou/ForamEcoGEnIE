from mpl_toolkits.basemap import Basemap
import string
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import time
from scipy.integrate import odeint
import pandas as pd
import csv
from matplotlib import style
style.use('ggplot')


###----------------------------------------------------------------------------------###
### export data from csv - biomass estimated from abundance data ###


df =pd.read_csv('E:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\GLOBAL_MAP_PLOTS\selected_traps_globalmap.csv')#first parameter is the filename and the second parameter is the sheet
dfNet = pd.read_csv('E:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\GLOBAL_MAP_PLOTS\\Net_global_map.csv')
df.shape
# lat- lon
lonsNet = dfNet['lon']
latsNet = dfNet['lat']

lonsTrap = df['Lon']
latsTrap = df['Lat']

latNet = np.array(latsNet)
lonNet = np.array(lonsNet)

latTrap = np.array(latsTrap)
lonTrap = np.array(lonsTrap)



### CREATE MAP SUBPLOT ####

##### projections: mill, robin

### x variable: lon, y variable: lat ###
### llcrnrlat = lower left corner lat/lon ###
### urcrnrlat = upper right corner lat/lon ###
### north = +, south = -, west = -, east =+ ###
### resolution: c= crue, l=low, h=high, f= four resolution ###
#figure(0)
plt.figure(figsize=(15,15))
fig, ax = plt.subplots(1, figsize=(15, 15),edgecolor='g')
#m= Basemap(projection = 'mill', llcrnrlat = -90, urcrnrlat = 90,\
#           llcrnrlon = -180, urcrnrlon = 180, resolution = 'c')

m = Basemap(projection='robin', lat_0=0, lon_0=0,
              resolution='c')
			  
# Draw coastlines and fill continents and water with color
m.drawcoastlines()
m.fillcontinents(color='#CCCCCC',lake_color='white')
m.drawmapboundary(fill_color='white')
draw_map(m)
#m.drawparallels(np.arange(-90.,91.,15.),labels=[True,False,False,False],dashes=[2,2])
#m.drawmeridians(np.arange(-180.,181.,15.),labels=[False,False,False,False],dashes=[2,2])
#m.bluemarble()
#plt.show()

### non-spinose 
x,y = m(lonTrap, latTrap)
sc = plt.scatter(x,y, marker = 's', color ='r', edgecolors='red')

x1,y1 = m(lonNet, latNet)
sc = plt.scatter(x1,y1, marker = 'o',color ='k' , edgecolors='black')

#plt.legend(loc= 'lower right', ncol=3)
plt.show()

#######################################################################################################################################################################################################################################################################
