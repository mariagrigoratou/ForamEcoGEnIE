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



###---------------------------------- read csv data foramecogenie ----------------------------------------------------###
df_zoo = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\python_excel\\zoo_biomass_seasonal.csv')
df_sigma2pal09 = pd.read_csv('E:PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\python_excel\\sigma2pal09_biomass.csv')				
###------------------------------ BIOTRANS 47N ----------------------------------------------------###

Month_genie = df_sigma2pal09['Month']
biotrans47_foram = df_sigma2pal09['ind_Biotrans47']
zoo47 = df_zoo['Biotrans47']

month_genie = np.array(Month_genie)
biotrans47_foram = np.log10(biotrans47_foram)
zoo_biotrans47 = np.log10(zoo47)

###---------------------------------------- BIOTRANS57N -------------------------------------------------------###

biotrans57_foram = df_sigma2pal09['ind_Biotrans57'] 
zoo57 = df_zoo['Biotrans57']

zoo_biotrans57 = np.log10(zoo57)
biotrans57_foram = np.log10(biotrans57_foram)

###---------------------------------------- AZORES ------------------------------------------------------###

Azores_foram = df_sigma2pal09['ind_Azores_tows']
zooazores = df_zoo['Azores_tows']

zoo_Azores = np.log10(zooazores)
Azores_foram = np.log10(Azores_foram)

###---------------------------------------- NE_Atlantic ------------------------------------------------------###

NE_Atlantic_foram = df_sigma2pal09['ind_NE_Atlantic'] 
zooNE_Atlantic = df_zoo['NE_Atlantic']

zoo_NE_Atlantic = np.log10(zooNE_Atlantic)
NE_Atlantic_foram = np.log10(NE_Atlantic_foram)

###---------------------------------------- BRAZIL 34S ------------------------------------------------------###

Brazil34_foram = df_sigma2pal09['ind_Brazil34']
zoobrazil34 = df_zoo['Brazil34']

zoo_Brazil_34 = np.log10(zoobrazil34)
Brazil34_foram = np.log10(Brazil34_foram)

###---------------------------------------- BRAZIL 23S ------------------------------------------------------###


Brazil23_foram = df_sigma2pal09['ind_Brazil23'] 
zoobrazil23 = df_zoo['Brazil23']

zoo_Brazil_23 = np.log10(zoobrazil23)
Brazil23_foram = np.log10(Brazil23_foram)

###---------------------------------------- CARIBBEAN ------------------------------------------------------###

zoocaribbean = df_zoo['Caribbean_Schiebel'] 
Caribbean_foram = df_sigma2pal09['ind_Caribbean_Schiebel'] 

zoo_Caribbean = np.log10(zoocaribbean)
Caribbean_foram = np.log10(Caribbean_foram)

###---------------------------------------- japan ------------------------------------------------------###

Japan_foram = df_sigma2pal09['ind_Japan_net']
zoojapan = df_zoo['Japan_net']

zoo_Japan = np.log10(zoojapan)
Japan_foram = np.log10(Japan_foram)

###---------------------------------------- Panama ------------------------------------------------------###

Panama_foram = df_sigma2pal09['ind_Panama'] 
zoopanama = df_zoo['Panama']

zoo_Panama = np.log10(zoopanama)
Panama_foram = np.log10(Panama_foram)

###---------------------------------------- SE_Atlantic ------------------------------------------------------###

zooSE_Atlantic = df_zoo['SE_Atlantic']
SE_Atlantic_foram = df_sigma2pal09['ind_SE_Atlantic'] 

zoo_SE_Atlantic = np.log10(zooSE_Atlantic)
SE_Atlantic_foram = np.log10(SE_Atlantic_foram)

###---------------------------------------- California ------------------------------------------------------###

California_foram = df_sigma2pal09['ind_California']
zoocalifornia = df_zoo['California'] 

zoo_California = np.log10(zoocalifornia)
California_foram = np.log10(California_foram)

###---------------------------------------- Arabian ------------------------------------------------------###

Arabian_foram = df_sigma2pal09['ind_Arabian'] 
zooarabian = df_zoo['Arabian']

zoo_Arabian = np.log10(zooarabian)
Arabian_foram = np.log10(Arabian_foram)



###---------------------------------------- Labrador ------------------------------------------------------###

Ladrador_Sea_foram = df_sigma2pal09['ind_Labrador_Sea']
zoolabrador = df_zoo['Labrador_Sea'] 

zoo_Labrador = np.log10(zoolabrador)
Ladrador_Sea_foram = np.log10(Ladrador_Sea_foram)

###---------------------------------------- Atlantic Current ------------------------------------------------------###

Atlantic_Current_foram = df_sigma2pal09['ind_Atlantic_current']
zooAtlantic = df_zoo['Atlantic_current']  

zoo_Atlantic_Current = np.log10(zooAtlantic)
Atlantic_Current_foram = np.log10(Atlantic_Current_foram)

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

###------------------------------ BIOTRANS 47n ----------------------------------------------------###

plt.subplot(441)
#plt.subplot(z[0,0,0])
plt.margins(x=0)
plt.ylim(-4, -1)

x,y= (biotrans47_foram, month_genie)
x1, y1 = (zoo_biotrans47, month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.xticks(rotation=45)
plt.title('Biotrans 47N (No 1)')


###---------------------------------------- Atlantic_Current -------------------------------------------------------###

plt.subplot(442)
plt.ylim(-4, -1)
plt.margins(x=0)
x,y = (Atlantic_Current_foram, month_genie)
x1, y1 = (zoo_Atlantic_Current, month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('NW Atlantic (No 2)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  Japan ----------------------------------------------------###
plt.subplot(443)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (Japan_foram ,month_genie)
x1, y1 = ( zoo_Japan,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('NW Pacific (Japan Front, No 3)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  BRAZIL 34S ----------------------------------------------------###

plt.subplot(444)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = ( Brazil34_foram,month_genie)
x1, y1 = ( zoo_Brazil_34,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('SE Brazilian margin 34S (No 4)')
plt.margins(x=0)
plt.xticks(rotation=45)
###---------------------------------------- AZORES ------------------------------------------------------###
plt.subplot(445)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (Azores_foram,month_genie)
x1, y1 = (zoo_Azores,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('Azores front (No 5)')
plt.margins(x=0)
plt.xticks(rotation=45)
###---------------------------------------- NE_Atlantic ------------------------------------------------------###

plt.subplot(446)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (NE_Atlantic_foram,month_genie)
x1, y1 = (zoo_NE_Atlantic,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('NE Atlantic (No 6)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  BRAZIL 23S ----------------------------------------------------###

plt.subplot(447)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (Brazil23_foram,month_genie)
x1, y1 = (zoo_Brazil_23,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('SE Brazilian margin 23S (No 7)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  Caribbean ----------------------------------------------------###
plt.subplot(448)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (Caribbean_foram,month_genie)
x1, y1 = (zoo_Caribbean,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('Caribbean Sea (No 8)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  SE_Atlantic ----------------------------------------------------###
plt.subplot(449)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (SE_Atlantic_foram,month_genie)
x1, y1 = (zoo_SE_Atlantic,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('SE Atlantic Upwelling (No 9)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  Panama ----------------------------------------------------###
plt.subplot(4,4,10)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (Panama_foram,month_genie)
x1, y1 = (zoo_Panama,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('Panama Basin (No 10)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  California ----------------------------------------------------###
plt.subplot(4,4,11)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (California_foram,month_genie)
x1, y1 = (zoo_California,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('California Upwelling (No 11)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  Arabian Sea ----------------------------------------------------###
plt.subplot(4,4,12)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (Arabian_foram,month_genie)
x1, y1 = (zoo_Arabian ,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')


plt.title('Arabian Sea (No 12)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- Labrador Sea -------------------------------------------------------###
plt.subplot(4,4,13)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = ( Ladrador_Sea_foram,month_genie)
x1, y1 = ( zoo_Labrador,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')

plt.title('Labrador Sea (No 13)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- biotrans57N -------------------------------------------------------###
plt.subplot(4,4,14)
plt.ylim(-4, -1)
plt.margins(x=0)

x, y = (biotrans57_foram ,month_genie)
x1, y1 = (zoo_biotrans57 ,month_genie)
foram = plt.plot(y,x, color= color1, label= 'foram')
zoo = plt.plot(y1,x1, color= color, label = 'zoo')


plt.title('Biotrans 57N(No 14)')
plt.margins(x=0)
plt.xticks(rotation=45)

################ ------------------------------------------------------------------------------------ ###########

label = [ "foram",  "zoo"]
fig.legend((foram, zoo,),labels= label,
            loc = 'upper right', 
            ncol=3,
            frameon=False, 
            fontsize=11) 

fig.text(0.50, 0.95,
        'Foraminifera vs Zooplankton 190 um monthly biomass (mmol C m$^{-3}$)',
        ha='center', fontsize = 16)

fig.text(0.080, 0.25,
        'Log10 biomass (mmol C m$^{-3}$)',
        ha='center', rotation = 'vertical', fontsize = 16)
		

fig.text(0.50, 0.03,
        'Time (months)',
        ha='center', fontsize = 16)

plt.show()


