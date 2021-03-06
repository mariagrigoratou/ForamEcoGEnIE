#from mpl_toolkits.basemap import Basemap
import string
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import time
from scipy.integrate import odeint
from scipy.interpolate import spline
import pandas as pd
import csv
#from matplotlib import style
#style.use('ggplot')


###---------------------------------- read csv data ----------------------------------------------------###

df_genie = pd.read_csv('sigma2pal09_export.csv')
#df_genie.dropna(inplace=True)
df_NA = pd.read_csv('Jonkers_2010_Subpolar_Atlantic.csv')
#df_NA.dropna(inplace=True)
df_trap_Papa = pd.read_csv('Papa_trap.csv')
#df_trap_Papa.dropna(inplace=True)
df_Azores = pd.read_csv('Azores_trap.csv')
#df_Azores.dropna(inplace=True)
df_Cape_Blanc = pd.read_csv('Cape_Blanc.csv')
#df_Cape_Blanc.dropna(inplace=True)
df_Southern_Ocean = pd.read_csv('W_Sea_a.csv')
#df_Southern_Ocean.dropna(inplace=True)
df_Southern_Ocean_two = pd.read_csv('W_Sea_b.csv')
#f_Southern_Ocean_two.dropna(inplace=True)
df_subtropics_Japan = pd.read_csv('subtropics_Japan.csv')
#df_subtropics_Japan.dropna(inplace=True)
df_temperate_Japan = pd.read_csv('Temperate_Japan.csv')
#df_temperate_Japan.dropna(inplace=True)
df_Sargasso = pd.read_csv('Sargasso.csv')
#df_Sargasso.dropna(inplace=True)
df_Brazil = pd.read_csv('Brazil.csv')
#df_Brazil.dropna(inplace=True)
df_Arabian = pd.read_csv('Arabian.csv')
#df_Arabian.dropna(inplace=True)
df_Subantarctica = pd.read_csv('Subantarctica.csv')
#df_Subantarctica.dropna(inplace=True)

###------------------------------ SUBPOLAR ATLANTIC ----------------------------------------------------###

Month_genie = df_genie ['Month']
export_NA =df_genie['NA']
Month_NA = df_NA ['MONTH']
Abud_NA = df_NA ['DAILY(mgC)']

NA_month_genie = np.array(Month_genie)
NA_month_trap = np.array(Month_NA)
a= np.array(export_NA)
NA_abund_genie = np.log10(a)
NA_abund_trap = np.log10(Abud_NA)


###---------------------------------------- PAPA -------------------------------------------------------###

Papa_month_gen = df_genie['Month']
Papa_abun_genie = df_genie['Papa_trap'] 
Papa_month_trap = df_trap_Papa['month']
Papa_abun_trap = df_trap_Papa['DAILY(mgC)'] 

Papa_month_genie = np.array(Papa_month_gen)
Papa_month_trap = np.array(Papa_month_trap)
Papa_abund_genie = np.log10(Papa_abun_genie)
Papa_abund_trap = np.log10(Papa_abun_trap)


###---------------------------------------- AZORES ------------------------------------------------------###

Azores_month_gen = df_genie['Month']
Azores_abun_genie = df_genie['Azores_trap'] 
Azores_month_trap = df_Azores['month']
Azores_abun_trap = df_Azores['DAILY(mgC)'] 

Azores_month_genie = np.array(Azores_month_gen)
Azores_month_trap = np.array(Azores_month_trap)
Azores_abund_genie = np.log10(Azores_abun_genie)
Azores_abund_trap = np.log10(Azores_abun_trap)

###---------------------------------------- CAPE BLACK ---------------------------------------------------###

Cape_Blanc_month_gen = df_genie['Month']
Cape_Blanc_abun_genie = df_genie['Cape_Blanc'] 
Cape_Blanc_month_trap = df_Cape_Blanc['Month']
Cape_Blanc_abun_trap = df_Cape_Blanc['DAILY(mgC)'] 

Cape_Blanc_month_genie = np.array(Cape_Blanc_month_gen)
Cape_Blanc_month_trap = np.array(Cape_Blanc_month_trap)
Cape_Blanc_abund_genie = np.log10(Cape_Blanc_abun_genie)
Cape_Blanc_abund_trap = np.log10(Cape_Blanc_abun_trap)


###------------------------------------ SOUTHERN OCEAN 1 ---------------------------------------------------###

Southern_Ocean_month_gen = df_genie['Month']
Southern_Ocean_abun_genie = df_genie['SO_1'] 
Southern_Ocean_month_trap = df_Southern_Ocean['month']
Southern_Ocean_abun_trap = df_Southern_Ocean['DAILY(mgC)'] 

Southern_Ocean_month_genie = np.array(Southern_Ocean_month_gen)
Southern_Ocean_month_trap = np.array(Southern_Ocean_month_trap)
Southern_Ocean_abund_genie = np.log10(Southern_Ocean_abun_genie)
Southern_Ocean_abund_trap = np.log10(Southern_Ocean_abun_trap)


###------------------------------------ SOUTHERN OCEAN 2 ---------------------------------------------------###

Southern_Ocean_two_month_gen = df_genie['Month']
Southern_Ocean_two_abun_genie = df_genie['SO_2'] 
Southern_Ocean_two_month_trap = df_Southern_Ocean['month']
Southern_Ocean_two_abun_trap = df_Southern_Ocean['DAILY(mgC)'] 

Southern_Ocean_two_month_genie = np.array(Southern_Ocean_two_month_gen)
Southern_Ocean_two_month_trap = np.array(Southern_Ocean_two_month_trap)
Southern_Ocean_two_abund_genie = np.log10(Southern_Ocean_two_abun_genie)
Southern_Ocean_two_abund_trap = np.log10(Southern_Ocean_two_abun_trap)

###------------------------------------ SUBTROPICS JAPAN ---------------------------------------------------###

subtropics_Japan_month_gen = df_genie['Month']
subtropics_Japan_abun_genie = df_genie['Japan_Subtropic_trap'] 
subtropics_Japan_month_trap = df_subtropics_Japan['month']
subtropics_Japan_abun_trap = df_subtropics_Japan['DAILY(mgC)'] 

subtropics_Japan_month_genie = np.array(subtropics_Japan_month_gen)
subtropics_Japan_month_trap = np.array(subtropics_Japan_month_trap)
subtropics_Japan_abund_genie = np.log10(subtropics_Japan_abun_genie)
subtropics_Japan_abund_trap = np.log10(subtropics_Japan_abun_trap)

###------------------------------------ TEMPERATE JAPAN ---------------------------------------------------###

temperate_Japan_month_gen = df_genie['Month']
temperate_Japan_abun_genie = df_genie['Japan_Temperate_trap'] 
temperate_Japan_month_trap = df_temperate_Japan['month']
temperate_Japan_abun_trap = df_temperate_Japan['DAILY(mgC)'] 

temperate_Japan_month_genie = np.array(temperate_Japan_month_gen)
temperate_Japan_month_trap = np.array(temperate_Japan_month_trap)
temperate_Japan_abund_genie = np.log10(temperate_Japan_abun_genie)
temperate_Japan_abund_trap = np.log10(temperate_Japan_abun_trap)

###------------------------------------ SARGASSO SEA ---------------------------------------------------###

Sargasso_month_gen = df_genie['Month']
Sargasso_genie = df_genie['Sargasso_trap'] 
Sargasso_month_trap = df_Sargasso['month']
Sargasso_abun_trap = df_Sargasso['DAILY(mgC)'] 

Sargasso_month_genie = np.array(Sargasso_month_gen)
Sargasso_month_trap = np.array(Sargasso_month_trap)
Sargasso_abund_genie = np.log10(Sargasso_genie)
Sargasso_abund_trap = np.log10(Sargasso_abun_trap)

###------------------------------------ BRAZIL ---------------------------------------------------###

Brazil_month_gen = df_genie['Month']
Brazil_genie = df_genie['Biomass_Brazil'] 
Brazil_month_trap = df_Brazil['month']
Brazil_abun_trap = df_Brazil['DAILY(mgC)'] 

Brazil_month_genie = np.array(Brazil_month_gen)
Brazil_month_trap = np.array(Brazil_month_trap)
Brazil_abund_genie = np.log10(Brazil_genie)
Brazil_abund_trap = np.log10(Brazil_abun_trap)

###------------------------------------ ARABIAN ---------------------------------------------------###

Arabian_month_gen = df_genie['Month']
Arabian_genie = df_genie['Arabian_trap'] 
Arabian_month_trap = df_Arabian['month']
Arabian_abun_trap = df_Arabian['DAILY(mgC)'] 

Arabian_month_genie = np.array(Arabian_month_gen)
Arabian_month_trap = np.array(Arabian_month_trap)
Arabian_abund_genie = np.log10(Arabian_genie)
Arabian_abund_trap = np.log10(Arabian_abun_trap)

###------------------------------------ Subantarctica ---------------------------------------------------###

Subantarctica_month_gen = df_genie['Month']
Subantarctica_genie = df_genie['Subantractica'] 
Subantarctica_month_trap = df_Subantarctica['month']
Subantarctica_abun_trap = df_Subantarctica['DAILY(mgC)'] 

Subantarctica_month_genie = np.array(Subantarctica_month_gen)
Subantarctica_month_trap = np.array(Subantarctica_month_trap)
Subantarctica_abund_genie = np.log10(Subantarctica_genie)
Subantarctica_abund_trap = np.log10(Subantarctica_abun_trap)

### ----------------------------------------------------------------------------------------------------------- ###
### ----------------------------------------------------------------------------------------------------------- ###
### ----------------------------------------------------------------------------------------------------------- ###

z =np.zeros((4,3)) 
fig, z = plt.subplots(4,3, sharex='col', sharey='row', figsize=(15,15))
#fig, ax = plt.subplots(1, figsize=(12, 12),edgecolor='w')
### adjust the space between the plots
fig.subplots_adjust(hspace=0.4, wspace=0.2)
plt.xticks(rotation=45)
plt.margins(x=0)
color = 'black'
color1= 'tab:red'

###------------------------------ SUBPOLAR ATLANTIC ----------------------------------------------------###

plt.subplot(z[0,0])
plt.margins(x=0)
plt.ylim(-5, 4)

x,y= (NA_abund_genie, NA_month_genie) 
x1,y1= (NA_abund_trap, NA_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.xticks(rotation=45)
plt.title('Subpolar Atlantic (No 15)')



###------------------------------ SARGASSO ----------------------------------------------------###
plt.subplot(z[0,1])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Sargasso_abund_genie, Sargasso_month_genie)
x1,y1= (Sargasso_abund_trap, Sargasso_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('Sargasso (No 16)')
plt.xticks(rotation=45)
###---------------------------------------- CAPE BLANC ---------------------------------------------------###
plt.subplot(z[0,2])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Cape_Blanc_abund_genie, Cape_Blanc_month_genie)
x1,y1= (Cape_Blanc_abund_trap, Cape_Blanc_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('Cape Blanc (No 17)')
plt.xticks(rotation=45)
#plt.legend(bbox_to_anchor=(0.8,0.90), loc='2', ncol=1,borderaxespad=0., fontsize=13)
###---------------------------------------- AZORES ------------------------------------------------------###
plt.subplot(z[1,0])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Azores_abund_genie, Azores_month_genie)
x1,y1= (Azores_abund_trap, Azores_month_trap)
model = plt.plot(y,x, color= color1, label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('Azores (No 18)')
plt.xticks(rotation=45)
###---------------------------------------- BRAZIL ------------------------------------------------------###
plt.subplot(z[1,1])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Brazil_abund_genie, Brazil_month_genie)
x1,y1= (Brazil_abund_trap, Brazil_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')


plt.title('W Atlantic (No 19)')
plt.xticks(rotation=45)
###---------------------------------------- ARABIAN SEA ------------------------------------------------------###
plt.subplot(z[1,2])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Arabian_abund_genie, Arabian_month_genie)
x1,y1= (Arabian_abund_trap, Arabian_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')


plt.title('Arabian Sea (No 20)')
plt.xticks(rotation=45)

###---------------------------------------- PAPA -------------------------------------------------------###
plt.subplot(z[2,0])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Papa_abund_genie, Papa_month_genie)
x1,y1= (Papa_abund_trap, Papa_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('Papa (No 21)')
plt.xticks(rotation=45)

###------------------------------------ TEMPERATE JAPAN ---------------------------------------------------###
plt.subplot(z[2,1])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y = (temperate_Japan_abund_genie, temperate_Japan_month_genie)
x1,y1 = (temperate_Japan_abund_trap, temperate_Japan_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('NW Pacific subarctic (No 22)')
plt.xticks(rotation=45)

###------------------------------------ SUBTROPICS JAPAN ---------------------------------------------------###
plt.subplot(z[2,2])
plt.ylim(-5, 4)
plt.margins(x=0)
x,y = (subtropics_Japan_abund_genie, subtropics_Japan_month_genie)
x1,y1 = (subtropics_Japan_abund_trap, subtropics_Japan_month_trap)

model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('NW Pacific subtropic (No 23)')
plt.xticks(rotation=45)


###------------------------------------ Weddell Sea a -34.8E Lon ---------------------------------------------------###
plt.subplot(z[3,0])
plt.ylim(-5, 4)
plt.margins(x=0)
x,y = (Southern_Ocean_abund_genie, Southern_Ocean_month_genie)
x1,y1 = (Southern_Ocean_abund_trap, Southern_Ocean_month_trap)

model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('Weddell Sea A (No 24)')
plt.xticks(rotation=45)

###------------------------------------ Weddell Sea b -2E Lon ---------------------------------------------------###
plt.subplot(z[3,1])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Southern_Ocean_two_abund_genie, Southern_Ocean_two_month_genie)
x1,y1= (Southern_Ocean_two_abund_trap, Southern_Ocean_two_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title('Weddell Sea B (No 25)')
plt.xticks(rotation=45)
###------------------------------------  Subantarctica ---------------------------------------------------###
plt.subplot(z[3,2])
plt.ylim(-5, 4)
plt.margins(x=0)

x,y= (Subantarctica_abund_genie, Subantarctica_month_genie)
x1,y1= (Subantarctica_abund_trap, Subantarctica_month_trap)
model = plt.plot(y,x, color= color1,  label= 'model')
trap = plt.scatter(y1,x1, color= color, s =20, edgecolors='none', label = 'trap')

plt.title(' Subantarctic Zone (No 26)')
plt.xticks(rotation=45)


label = [ "model", "trap"]
fig.legend((model, trap),labels= label,
            loc = 'upper right', 
            ncol=1,
            frameon=False, 
            fontsize=11) 


fig.text(0.50, 0.95,
        'Foraminifera export production',
        ha='center', fontsize = 16)

fig.text(0.080, 0.55,
        'Biomass Fluxes Log$_{10}$(mg C m$^{-2}$ d$^{-2}$)',
        ha='center', rotation = 'vertical', fontsize = 16)

fig.text(0.50, 0.03,
        'Time (months)',
        ha='center', fontsize = 16)

plt.show()




