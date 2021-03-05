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
from scipy.stats.stats import pearsonr   
#from matplotlib import style
#style.use('ggplot')


###---------------------------------- read csv data observations ----------------------------------------------------###
df_biotrans = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Biotrans_net.csv')
#df_biotrans.dropna(inplace=True)
df_biotrans57N = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Biotrans57N_net.csv')
df_biotrans57N.dropna(inplace=True)
df_Azores = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Azores_net.csv')
#df_Azores.dropna(inplace=True)
df_Azores_Jan = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Azores_net_January.csv')
df_NE_Atlantic = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\NE_Atlantic.csv')
df_NE_Atlantic.dropna(inplace=True)
df_Brazil_34 = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Brazil_34.csv')
#df_Brazil_34.dropna(inplace=True)
df_Brazil_23 = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Brazil_23.csv')
#df_Brazil_23.dropna(inplace=True)
df_Caribbean = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Caribbean.csv')
#df_Caribbean.dropna(inplace=True)
df_Japan = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Japan.csv')
#df_Brazil_23.dropna(inplace=True)
df_Panama = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Panama.csv')
df_SE_Atlantic = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\SE_Atlantic.csv')
df_Arabian = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Arabian.csv')
df_California = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\California.csv')
df_Ross_Sea = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Antarctica.csv')
df_Arctic = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Arctic.csv')
df_Atlantic_Current = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Atlantic_Current.csv')
df_Labrador = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\Labrador.csv')

###---------------------------------- read csv data foramecogenie ----------------------------------------------------###
df_phyto = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\PRESENT\chla\Total_phyto_genie.csv')
df_sigma2pal09 = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\python_excel\\sigma2pal09_abundance.csv')				
###------------------------------ BIOTRANS 47N ----------------------------------------------------###

Month_genie = df_sigma2pal09['Month']
biotrans47_genie1 = df_sigma2pal09['ind_Biotrans47']
phyto47 = df_phyto['Biotrans_47']
Month_biotrans47_net = df_biotrans ['Month']
abund_biotrans47_net = df_biotrans ['ind']


month_genie = np.array(Month_genie)
biotrans47N_month_net = np.array(Month_biotrans47_net)
biotrans47_abund_net = np.log10(abund_biotrans47_net)
biotrans47_genie1 = np.log10(biotrans47_genie1)
phyto_biotrans47 = np.log10(phyto47)

###---------------------------------------- BIOTRANS57N -------------------------------------------------------###

biotrans57_genie1 = df_sigma2pal09['ind_Biotrans57']
biotrans57_genie1 = df_sigma2pal09['ind_Biotrans57'] 

biotrans57N_month_net = df_biotrans57N['month']
biotrans57N_abund_net = df_biotrans57N['ind'] 
phyto57 = df_phyto['Biotrans_57']

phyto_biotrans57 = np.log10(phyto57)
biotrans57N_month_net = np.array(biotrans57N_month_net)
biotrans57N_abund_net = np.log10(biotrans57N_abund_net)
biotrans57_genie1 = np.log10(biotrans57_genie1)

###---------------------------------------- AZORES ------------------------------------------------------###

Azores_genie1 = df_sigma2pal09['ind_Azores_tows']
Azores_month_net = df_Azores['month']
Azores_abund_net = df_Azores['ind'] 
Azores_month_net_Jan = df_Azores_Jan['Month']
Azores_abund_net_Jan = df_Azores_Jan['ind'] 
phytoazores = df_phyto['Azores_tows']

phyto_Azores = np.log10(phytoazores)
Azores_month_net = np.array(Azores_month_net)
Azores_abund_net = np.log10(Azores_abund_net)
Azores_abund_net_Jan = np.log10(Azores_abund_net_Jan)
Azores_genie1 = np.log10(Azores_genie1)

###---------------------------------------- NE_Atlantic ------------------------------------------------------###

NE_Atlantic_genie1 = df_sigma2pal09['ind_NE_Atlantic'] 
NE_Atlantic_month_net = df_NE_Atlantic['Month']
NE_Atlantic_abund_net = df_NE_Atlantic['ind'] 
phytoNE_Atlantic = df_phyto['NE_Atlantic']

NE_Atlantic_month_net = np.array(NE_Atlantic_month_net)
NE_Atlantic_abund_net = np.log10(NE_Atlantic_abund_net)
phyto_NE_Atlantic = np.log10(phytoNE_Atlantic)
NE_Atlantic_genie1 = np.log10(NE_Atlantic_genie1)

###---------------------------------------- BRAZIL 34S ------------------------------------------------------###

Brazil34_genie1 = df_sigma2pal09['ind_Brazil34']
phytobrazil34 = df_phyto['Brazil34']
Brazil_34_month_net = df_Brazil_34['Month']
Brazil_34_abund_net = df_Brazil_34['ind'] 

phyto_Brazil_34 = np.log10(phytobrazil34)
Brazil_34_month_net = np.array(Brazil_34_month_net)
Brazil_34_abund_net = np.log10(Brazil_34_abund_net)
Brazil34_genie1 = np.log10(Brazil34_genie1)

###---------------------------------------- BRAZIL 23S ------------------------------------------------------###


Brazil23_genie1 = df_sigma2pal09['ind_Brazil23'] 
phytobrazil23 = df_phyto['brazil24']
Brazil_23_month_net = df_Brazil_23['Month']
Brazil_23_abund_net = df_Brazil_23['ind'] 

phyto_Brazil_23 = np.log10(phytobrazil23)
Brazil_23_month_net = np.array(Brazil_23_month_net)
Brazil_23_abund_net = np.log10(Brazil_23_abund_net)
Brazil23_genie1 = np.log10(Brazil23_genie1)

###---------------------------------------- CARIBBEAN ------------------------------------------------------###

phytocaribbean = df_phyto['Caribbean'] 
Caribbean_genie1 = df_sigma2pal09['ind_Caribbean_Schiebel'] 

Caribbean_month_net = df_Caribbean['Month']
Caribbean_abund_net = df_Caribbean['ind'] 

phyto_Caribbean = np.log10(phytocaribbean)
Caribbean_month_net = np.array(Caribbean_month_net)
Caribbean_abund_net = np.log10(Caribbean_abund_net)
Caribbean_genie1 = np.log10(Caribbean_genie1)

###---------------------------------------- japan ------------------------------------------------------###

Japan_genie1 = df_sigma2pal09['ind_Japan_net']
phytojapan = df_phyto['Japan_net']
Japan_month_net = df_Japan['Month']
Japan_abund_net = df_Japan['ind'] 

phyto_Japan = np.log10(phytojapan)
Japan_month_net = np.array(Japan_month_net)
Japan_abund_net = np.log10(Japan_abund_net)
Japan_genie1 = np.log10(Japan_genie1)

###---------------------------------------- Panama ------------------------------------------------------###

Panama_genie1 = df_sigma2pal09['ind_Panama'] 
phytopanama = df_phyto['Panama']
Panama_month_net = df_Panama['Month']
Panama_abund_net = df_Panama['ind'] 

phyto_Panama = np.log10(phytopanama)
Panama_month_net = np.array(Panama_month_net)
Panama_abund_net = np.log10(Panama_abund_net)
Panama_genie1 = np.log10(Panama_genie1)

###---------------------------------------- SE_Atlantic ------------------------------------------------------###

phytoSE_Atlantic = df_phyto['SE_Atlantic']
SE_Atlantic_genie1 = df_sigma2pal09['ind_SE_Atlantic'] 
SE_Atlantic_month_net = df_SE_Atlantic['Month']
SE_Atlantic_abund_net = df_SE_Atlantic['ind'] 

phyto_SE_Atlantic = np.log10(phytoSE_Atlantic)
SE_Atlantic_month_net = np.array(SE_Atlantic_month_net)
SE_Atlantic_abund_net = np.log10(SE_Atlantic_abund_net)
SE_Atlantic_genie1 = np.log10(SE_Atlantic_genie1)

###---------------------------------------- California ------------------------------------------------------###

California_genie1 = df_sigma2pal09['ind_California']
phytocalifornia = df_phyto['california'] 
California_month_net = df_California['Month']
California_abund_net = df_California['ind'] 

phyto_California = np.log10(phytocalifornia)
California_month_net = np.array(California_month_net)
California_abund_net = np.log10(California_abund_net)
California_genie1 = np.log10(California_genie1)

###---------------------------------------- Arabian ------------------------------------------------------###


Arabian_genie1 = df_sigma2pal09['ind_Arabian'] 
phytoarabian = df_phyto['Arabian']
Arabian_month_net = df_Arabian['Month']
Arabian_abund_net = df_Arabian['ind'] 

phyto_Arabian = np.log10(phytoarabian)
Arabian_month_net = np.array(Arabian_month_net)
Arabian_abund_net = np.log10(Arabian_abund_net)
Arabian_genie1 = np.log10(Arabian_genie1)


###---------------------------------------- Ross_Sea ------------------------------------------------------###

Ross_Sea_genie1 = df_sigma2pal09['ind_Ross_Sea'] 
phytoRoss_Sea = df_phyto['Ross_Sea'] 
Ross_Sea_month_net = df_Ross_Sea['Month']
Ross_Sea_abund_net = df_Ross_Sea['ind'] 

phyto_Ross_Sea = np.log10(phytoRoss_Sea)
Ross_Sea_month_net = np.array(Ross_Sea_month_net)
Ross_Sea_abund_net = np.log10(Ross_Sea_abund_net)
Ross_Sea_genie1 = np.log10(Ross_Sea_genie1)

###---------------------------------------- Arctic ------------------------------------------------------###

phytoarctic = df_phyto['Arctic']
Arctic_abund_genie = df_sigma2pal09['ind_Arctic'] 
Arctic_month_net = df_Arctic['Month']
Arctic_abund_net = df_Arctic['ind'] 

phyto_Arctic = np.log10(phytoarctic)
Arctic_month_net = np.array(Arctic_month_net)
Arctic_abund_genie = np.log10(Arctic_abund_genie)
Arctic_abund_net = np.log10(Arctic_abund_net)


###---------------------------------------- Labrador ------------------------------------------------------###

Ladrador_Sea_genie1 = df_sigma2pal09['ind_Labrador_Sea']
phytolabrador = df_phyto['Labrador_ Sea'] 
Labrador_month_net = df_Labrador['Month']
Labrador_abund_net = df_Labrador['ind'] 

phyto_Labrador = np.log10(phytolabrador)
Labrador_month_net = np.array(Labrador_month_net)
Labrador_abund_net = np.log10(Labrador_abund_net)
Ladrador_Sea_genie1 = np.log10(Ladrador_Sea_genie1)

###---------------------------------------- Atlantic Current ------------------------------------------------------###

Atlantic_Current_genie1 = df_sigma2pal09['ind_Atlantic_current']
phytoAtlantic = df_phyto['Atlantic_current']  
Atlantic_Current_month_net = df_Atlantic_Current['Month']
Atlantic_Current_abund_net = df_Atlantic_Current['ind'] 

phyto_Atlantic_Current = np.log10(phytoAtlantic)
Atlantic_Current_month_net = np.array(Atlantic_Current_month_net)
Atlantic_Current_abund_net = np.log10(Atlantic_Current_abund_net)
Atlantic_Current_genie1 = np.log10(Atlantic_Current_genie1)

### ------------------------------------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------------------------------------- ###

color= 'black'
color1 = 'tab:blue'
color2 = 'tab:brown'


fig, ax1 = plt.subplots(4,4, sharex='col', sharey='row', figsize=(15,15))
fig.subplots_adjust(hspace=0.4, wspace=0.2)# adjust the space between the plots

plt.rc('xtick',labelsize=9)
plt.rc('ytick',labelsize=10)
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------ BIOTRANS 47n ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[0, 0].set_ylim([-1.0, 2.5])
x,y= (biotrans47_genie1, month_genie)
x1, y1 = (biotrans47_genie1, month_genie)
model1 = ax1[0, 0].plot(y, x, color = color1) #row=0, col=0
obsv = ax1[0, 0].plot(biotrans47N_month_net, biotrans47_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
ax1[0, 0].tick_params(axis='y', labelcolor= color)


ax2 = ax1[0, 0].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_biotrans47, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Biotrans 47N (No 1)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- Atlantic_Current -------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[0, 1].set_ylim([-1.0, 2.5])
model1 = ax1[0, 1].plot(month_genie, Atlantic_Current_genie1, color = color1) #row=0, col=0
obsv = ax1[0, 1].plot(Atlantic_Current_month_net, Atlantic_Current_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[0,1].tick_params(axis='y', labelcolor= color)

ax2 = ax1[0, 1].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5.0, 1.0])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Atlantic_Current, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('NW Atlantic (No 2)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  Japan ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[0, 2].set_ylim([-1.0, 2.5])
model1 = ax1[0, 2].plot(month_genie, Japan_genie1, color = color1) #row=0, col=0
obsv = ax1[0, 2].plot(Japan_month_net, Japan_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[0, 2].tick_params(axis='y', labelcolor= color)

ax2 = ax1[0, 2].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5.0, 1.0])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Japan, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x,linestyle=':', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('NW Pacific (Japan Front, No 3)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  BRAZIL 34S ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[0, 3].set_ylim([-1.0, 2.5])
model1 = ax1[0, 3].plot(month_genie, Brazil34_genie1, color = color1) #row=0, col=0
obsv = ax1[0, 3].plot(Brazil_34_month_net, Brazil_34_abund_net, marker='o', linestyle='none', markersize=7, color= color) #row=0, col=0
ax1[0, 3].tick_params(axis='y', labelcolor= color)

plt.margins(x=0)
plt.xticks(rotation=45)
ax2 = ax1[0, 3].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(True)
plt.setp(ax2.get_yticklabels(), visible=True)
x,y= (phyto_Brazil_34, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('SE Brazilian margin 34S (No 4)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- AZORES ------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[1, 0].set_ylim([-1.0, 2.5])
model1 = ax1[1, 0].plot(month_genie, Azores_genie1, color = color1) #row=0, col=0
obsv = ax1[1, 0].plot(Azores_month_net, Azores_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
obsv1 = ax1[1, 0].scatter(Azores_month_net_Jan, Azores_abund_net_Jan, marker = 'o', facecolors='none', edgecolors='black') #row=0, col=0
ax1[1, 0].tick_params(axis='y', labelcolor= color)

ax2 = ax1[1, 0].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Azores, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Azores front (No 5)')
plt.margins(x=0)
plt.xticks(rotation=45)
###---------------------------------------- NE_Atlantic ------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[1,1].set_ylim([-1.0, 2.5])
model1 = ax1[1,1].plot(month_genie, NE_Atlantic_genie1, color = color1) #row=0, col=0
obsv = ax1[1,1].plot(NE_Atlantic_month_net, NE_Atlantic_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
ax1[1,1].tick_params(axis='y', labelcolor= color)

ax2 = ax1[1,1].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_NE_Atlantic, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x,linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('NE Atlantic (No 6)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  BRAZIL 23S ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[1,2].set_ylim([-1.0, 2.5])
model1 = ax1[1,2].plot(month_genie, Brazil23_genie1, color = color1) #row=0, col=0
obsv = ax1[1,2].plot(Brazil_23_month_net, Brazil_23_abund_net, marker='o', linestyle='none', markersize=7, color= color) #row=0, col=0
ax1[1,2].tick_params(axis='y', labelcolor= color)

ax2 = ax1[1,2].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Brazil_23, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':',color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('SE Brazilian margin 23S (No 7)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  Caribbean ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[1,3].set_ylim([-1.0, 2.5])
model1 = ax1[1,3].plot(month_genie, Caribbean_genie1, color = color1) #row=0, col=0
obsv = ax1[1,3].plot(Caribbean_month_net, Caribbean_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
ax1[1,3].tick_params(axis='y', labelcolor= color)

plt.margins(x=0)
plt.xticks(rotation=45)
ax2 = ax1[1,3].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(True)
plt.setp(ax2.get_yticklabels(), visible=True)
x,y= (phyto_Caribbean, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x,linestyle=':', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Caribbean Sea (No 8)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  SE_Atlantic ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[2,0].set_ylim([-1.0, 2.5])
model1 = ax1[2,0].plot(month_genie, SE_Atlantic_genie1, color = color1) #row=0, col=0
obsv = ax1[2,0].plot(SE_Atlantic_month_net, SE_Atlantic_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[2,0].tick_params(axis='y', labelcolor= color)

ax2 = ax1[2,0].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_SE_Atlantic, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('SE Atlantic Upwelling (No 9)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  Panama ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[2,1].set_ylim([-1.0, 2.5])
model1 = ax1[2,1].plot(month_genie, Panama_genie1, color = color1) #row=0, col=0
obsv = ax1[2,1].plot(Panama_month_net, Panama_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
ax1[2,1].tick_params(axis='y', labelcolor= color)

ax2 = ax1[2,1].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Panama, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Panama Basin (No 10)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  California ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[2,2].set_ylim([-1.0, 2.5])
model1 = ax1[2,2].plot(month_genie, California_genie1, color = color1) #row=0, col=0
obsv = ax1[2,2].plot(California_month_net, California_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[2,2].tick_params(axis='y', labelcolor= color)

ax2 = ax1[2,2].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)

##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(month_genie, phyto_California, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('California Upwelling (No 11)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  Arabian Sea ----------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[2,3].set_ylim([-1.0, 2.5])
model1 = ax1[2,3].plot(month_genie, Arabian_genie1, color = color1) #row=0, col=0
obsv = ax1[2,3].plot(Arabian_month_net, Arabian_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[2,3].tick_params(axis='y', labelcolor= color)

ax2 = ax1[2,3].twinx() # instantiate a second axes that shares the same x-axis
color3 = 'tab:green'
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(True)
plt.setp(ax2.get_yticklabels(), visible= True)
x,y= (phyto_Arabian, month_genie)
##ax2.set_ylabel('model', color=color)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Arabian Sea (No 12)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- Labrador Sea -------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[3, 0].set_ylim([-1.0, 2.5])
model1 = ax1[3, 0].plot(month_genie, Ladrador_Sea_genie1, color = color1) #row=0, col=0
obsv = ax1[3, 0].plot(Labrador_month_net, Labrador_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[3, 0].tick_params(axis='y', labelcolor= color)


ax2 = ax1[3, 0].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Labrador, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Labrador Sea (No 13)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- biotrans57N -------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[3, 1].set_ylim([-1.0, 2.5])
model1 = ax1[3, 1].plot(month_genie, biotrans57_genie1, color = color1) #row=0, col=0
obsv = ax1[3, 1].plot(biotrans57N_month_net, biotrans57N_abund_net, marker='o', linestyle='none',markersize=5, color= color) #row=0, col=0
ax1[3, 1].tick_params(axis='y', labelcolor= color)

plt.margins(x=0)
plt.xticks(rotation=45)
ax2 = ax1[3, 1].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_biotrans57, month_genie)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(y,x, linestyle=':', color=color2)
##ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Biotrans 57N(No 14)')
plt.margins(x=0)
plt.xticks(rotation=45)

# ###---------------------------------------- Ross Sea -------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[3, 2].set_ylim([-1.0, 2.5])
model = ax1[3, 2].plot(month_genie, Ross_Sea_genie1, color = color) #row=0, col=0
obsv = ax1[3, 2].plot(Ross_Sea_month_net, Ross_Sea_abund_net, marker='o', linestyle='none',markersize=7, color= color) #row=0, col=0
ax1[3,2].tick_params(axis='y', labelcolor= color1)

# plt.margins(x=0)
# plt.xticks(rotation=45)
ax2 = ax1[3, 2].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(True)
plt.setp(ax2.get_yticklabels(), visible=True)
##ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
phyto = ax2.plot(month_genie, phyto_Ross_Sea, linestyle=':', color=color2)

ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Ross Sea (No 15)')
plt.margins(x=0)
plt.xticks(rotation=45)

##---------------------------------------- Arctic -------------------------------------------------------###
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[3, 3].set_ylim([-1.0, 2.5])
x1,y1= (Arctic_abund_net, Arctic_month_net)
model = ax1[3, 3].plot(month_genie, Arctic_abund_genie, color = color) #row=0, col=0
obsv = ax1[3, 3].plot(y1, x1, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
ax1[3,3].tick_params(axis='y', labelcolor= color1)

plt.margins(x=0)
plt.xticks(rotation=45)
ax2 = ax1[3, 3].twinx() # instantiate a second axes that shares the same x-axis
ax2.set_ylim([-5, 1])
ax2.spines['right'].set_visible(False)
plt.setp(ax2.get_yticklabels(), visible=False)
x,y= (phyto_Arctic, month_genie)
#ax2.set_ylabel('model', color=color2)  # we already handled the x-label with ax1
#phyto = ax2.plot(y,x, '--', color=color2)
phyto = ax2.plot(y,x, linestyle=':', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_title('Greenland Sea (No 16)')
plt.margins(x=0)
plt.xticks(rotation=45)

################ ------------------------------------------------------------------------------------ ###########

label = [ "model",  "obsv",  "phyto",]
fig.legend((model1, obsv, phyto,),labels= label,
            loc = 'upper right', 
            ncol=3,
            frameon=False, 
            fontsize=11) 

fig.text(0.50, 0.95,
        'Foraminifera monthly abundance (ind C m$^{-3}$)',
        ha='center', fontsize = 16)

fig.text(0.080, 0.55,
        'Log10 abundance (ind C m$^{-3}$)',
        ha='center', rotation = 'vertical', fontsize = 16)
		

fig.text(0.50, 0.03,
        'Time (months)',
        ha='center', fontsize = 16)
plt.show()





