#from mpl_toolkits.basemap import Basemap
import string
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import time
from scipy.integrate import odeint
import pandas as pd
import csv
from scipy.stats.stats import pearsonr   
#from matplotlib import style
#style.use('ggplot')



###---------------------------------- read csv data rcp6ecogenie ----------------------------------------------------###
rcp6 = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\python_excel\\future_biomass_RCP6.csv')
rcp8p5= pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\python_excel\\future_biomass_RCP8p5.csv')				


###------------------------------ GLOBAL ----------------------------------------------------###

year = rcp6['year']
global_rcp6 = rcp6['Global']
global_rcp8p5 = rcp8p5['Global']

###------------------------------ sSO ----------------------------------------------------###

sSO_rcp6 = rcp6['sSO']
sSO_rcp8p5 = rcp8p5['sSO']


###------------------------------ sNA ----------------------------------------------------###

sNA_rcp6 = rcp6['sNA']
sNA_rcp8p5 = rcp8p5['sNA']

###------------------------------ sNH ----------------------------------------------------###

sNH_rcp6 = rcp6['sNH']
sNH_rcp8p5 = rcp8p5['sNH']


###------------------------------ mid_NP ----------------------------------------------------###

mid_NP_rcp6 = rcp6['mid_NP']
mid_NP_rcp8p5 = rcp8p5['mid_NP']

###------------------------------ mid_SP ----------------------------------------------------###

mid_SP_rcp6 = rcp6['mid_SP']
mid_SP_rcp8p5 = rcp8p5['mid_SP']

###------------------------------ mid_NA ----------------------------------------------------###

mid_NA_rcp6 = rcp6['mid_NA']
mid_NA_rcp8p5 = rcp8p5['mid_NA']

###------------------------------ mid_SA ----------------------------------------------------###

mid_SA_rcp6 = rcp6['mid_SA']
mid_SA_rcp8p5 = rcp8p5['mid_SA']

###------------------------------ lowLat_NP ----------------------------------------------------###

lowLat_NP_rcp6 = rcp6['lowLat_NP']
lowLat_NP_rcp8p5 = rcp8p5['lowLat_NP']

###------------------------------ lowLat_SP ----------------------------------------------------###

lowLat_SP_rcp6 = rcp6['lowLat_SP']
lowLat_SP_rcp8p5 = rcp8p5['lowLat_SP']

###------------------------------ lowLat_NA ----------------------------------------------------###

lowLat_NA_rcp6 = rcp6['lowLat_NA']
lowLat_NA_rcp8p5 = rcp8p5['lowLat_NA']

###------------------------------ lowLat_SA ----------------------------------------------------###

lowLat_SA_rcp6 = rcp6['lowLat_SA']
lowLat_SA_rcp8p5 = rcp8p5['lowLat_SA']

###------------------------------ IO ----------------------------------------------------###

IO_rcp6 = rcp6['IO']
IO_rcp8p5 = rcp8p5['IO']


### ------------------------------------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------------------------------------- ###


z =np.zeros((4,4)) 
fig, z = plt.subplots(4,4, sharex='col', sharey='row', figsize=(15,15))
fig.subplots_adjust(hspace=0.4, wspace=0.2)
# plt.xticks(rotation=45)
# plt.margins(x=0)
color = 'black'
color1 = 'tab:blue'
color2 = 'tab:brown'

###------------------------------ GLOBAL ----------------------------------------------------###

plt.subplot(441)
plt.margins(x=0)
plt.xlim(1776, 2100)
plt.ylim(-25, 25)

x,y= (global_rcp6, year)
x1, y1 = (global_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8.5')

plt.title('Global')



###------------------------------  sSO ----------------------------------------------------###
plt.subplot(442)
plt.xlim(1776, 2100)
plt.margins(x=0)
plt.ylim(-25, 25)

x,y= (sSO_rcp6, year)
x1, y1 = (sSO_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('subpolar SO')
plt.margins(x=0)

###------------------------------  sNA ----------------------------------------------------###

plt.subplot(443)
plt.xlim(1776, 2100)
plt.ylim(-25, 25)
plt.margins(x=0)

x,y= (sNA_rcp6, year)
x1, y1 = (sNA_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('subpolar NA')
plt.margins(x=0)


###------------------------------  sNH ----------------------------------------------------###

plt.subplot(444)
plt.xlim(1776, 2100)
plt.ylim(-25, 25)
plt.margins(x=0)

x,y= (sNH_rcp6, year)
x1, y1 = (sNH_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('subpoplar NH')
plt.margins(x=0)



###------------------------------  mid_NP ----------------------------------------------------###
plt.subplot(445)
plt.xlim(1776, 2100)
plt.ylim(-40, 0)
plt.margins(x=0)

x,y= (mid_NP_rcp6, year)
x1, y1 = (mid_NP_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('Mid NP')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  mid_SP ----------------------------------------------------###
plt.subplot(446)
plt.xlim(1776, 2100)
plt.ylim(-40, 0)
plt.margins(x=0)

x,y= (mid_SP_rcp6, year)
x1, y1 = (mid_SP_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('Mid SP')
plt.margins(x=0)

###------------------------------  mid_NA ----------------------------------------------------###
plt.subplot(447)
plt.xlim(1776, 2100)
plt.ylim(-40, 0)
plt.margins(x=0)

x,y= (mid_NA_rcp6, year)
x1, y1 = (mid_NA_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('Mid NA')
plt.margins(x=0)


###------------------------------  mid_SA ----------------------------------------------------###
plt.subplot(448)
plt.xlim(1776, 2100)
plt.ylim(-40, 0)
plt.margins(x=0)

x,y= (mid_SA_rcp6, year)
x1, y1 = (mid_SA_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('Mid SA')
plt.margins(x=0)


###------------------------------  lowLat_NP ----------------------------------------------------###
plt.subplot(4,4,9)
plt.xlim(1776, 2100)
plt.ylim(-100, 0)
plt.margins(x=0)

x,y= (lowLat_NP_rcp6, year)
x1, y1 = (lowLat_NP_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')


plt.title('LowLat NP')
plt.margins(x=0)


###---------------------------------------- lowLat_SP -------------------------------------------------------###
plt.subplot(4,4,10)
plt.xlim(1776, 2100)
plt.ylim(-100, 0)
plt.margins(x=0)

x,y= (lowLat_SP_rcp6, year)
x1, y1 = (lowLat_SP_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('LowLat SP')
plt.margins(x=0)


###---------------------------------------- lowLat_NA -------------------------------------------------------###
plt.subplot(4,4,11)
plt.xlim(1776, 2100)
plt.ylim(-100, 0)
plt.margins(x=0)

x,y= (lowLat_NA_rcp6, year)
x1, y1 = (lowLat_NA_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')


plt.title('LowLat NA')
plt.margins(x=0)



###---------------------------------------- lowLat_SA ------------------------------------------------------###
plt.subplot(4,4,12)
plt.xlim(1776, 2100)
plt.ylim(-100, 0)
plt.margins(x=0)

x,y= (lowLat_SA_rcp6, year)
x1, y1 = (lowLat_SA_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('LowLat SA')
plt.margins(x=0)


###---------------------------------------- IO ------------------------------------------------------###

plt.subplot(4,4,13)
plt.xlim(1776, 2100)
plt.ylim(-20, 0)
plt.margins(x=0)

x,y= (IO_rcp6, year)
x1, y1 = (IO_rcp8p5, year)
rcp6 = plt.plot(y,x, color= color1, label= 'rcp6')
rcp8p5 = plt.plot(y1,x1, color= color, label = 'rcp8p5')

plt.title('Indian Ocean')
plt.margins(x=0)


################ ------------------------------------------------------------------------------------ ###########
label = [ "rcp6",  "rcp8.5"]
fig.legend((rcp6, rcp8p5),labels= label,
            loc = 'upper right', 
            ncol=3,
            frameon=False, 
            fontsize=11) 

fig.text(0.50, 0.95,
        'Foraminifera relative (%) biomass anomaly (future - preindustrial)',
        ha='center', fontsize = 16)

fig.text(0.080, 0.35,
        '% biomass anomaly',
        ha='center', rotation = 'vertical', fontsize = 16)
		

fig.text(0.50, 0.03,
        'Time (years)',
        ha='center', fontsize = 16)

plt.show()


