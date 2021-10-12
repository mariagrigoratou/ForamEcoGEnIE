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


###---------------------------------- read csv data observations ----------------------------------------------------###
df_biotrans = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Biotrans_net.csv')
#df_biotrans.dropna(inplace=True)
df_biotrans57N = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Biotrans57N_net.csv')
df_biotrans57N.dropna(inplace=True)
df_Azores = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Azores_net.csv')
#df_Azores.dropna(inplace=True)
df_Azores_Jan = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Azores_net_January.csv')
df_NE_Atlantic = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\NE_Atlantic.csv')
df_NE_Atlantic.dropna(inplace=True)
df_Brazil_34 = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Brazil_34.csv')
#df_Brazil_34.dropna(inplace=True)
df_Brazil_23 = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Brazil_23.csv')
#df_Brazil_23.dropna(inplace=True)
df_Caribbean = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Caribbean.csv')
#df_Caribbean.dropna(inplace=True)
df_Japan = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Japan.csv')
#df_Brazil_23.dropna(inplace=True)
df_Panama = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Panama.csv')
df_SE_Atlantic = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\SE_Atlantic.csv')
df_Arabian = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Arabian.csv')
df_California = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\California.csv')
df_Ross_Sea = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Antarctica.csv')
df_Arctic = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Arctic.csv')
df_Atlantic_Current = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Atlantic_Current.csv')
df_Labrador = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\OBSV\\Nets\\Labrador.csv')

###---------------------------------- read csv data foramecogenie ----------------------------------------------------###
df_phyto = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\PRESENT\chla\\Total_phyto_genie.csv')
df_sigma2pal09 = pd.read_csv('D:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\python_excel\\sigma2pal09_abundance.csv')				
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
#phytoNE_Atlantic = df_phyto['NE_Atlantic']

NE_Atlantic_month_net = np.array(NE_Atlantic_month_net)
NE_Atlantic_abund_net = np.log10(NE_Atlantic_abund_net)
#phyto_NE_Atlantic = np.log10(phytoNE_Atlantic)
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

#phytoSE_Atlantic = df_phyto['SE_Atlantic']
SE_Atlantic_genie1 = df_sigma2pal09['ind_SE_Atlantic'] 
SE_Atlantic_month_net = df_SE_Atlantic['Month']
SE_Atlantic_abund_net = df_SE_Atlantic['ind'] 

#phyto_SE_Atlantic = np.log10(phytoSE_Atlantic)
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

# Ross_Sea_genie1 = df_sigma2pal09['ind_Ross_Sea'] 
# phytoRoss_Sea = df_phyto['Ross_Sea'] 
# Ross_Sea_month_net = df_Ross_Sea['Month']
# Ross_Sea_abund_net = df_Ross_Sea['ind'] 

# phyto_Ross_Sea = np.log10(phytoRoss_Sea)
# Ross_Sea_month_net = np.array(Ross_Sea_month_net)
# Ross_Sea_abund_net = np.log10(Ross_Sea_abund_net)
# Ross_Sea_genie1 = np.log10(Ross_Sea_genie1)

# ###---------------------------------------- Arctic ------------------------------------------------------###

# phytoarctic = df_phyto['Arctic']
# Arctic_abund_genie = df_sigma2pal09['ind_Arctic'] 
# Arctic_month_net = df_Arctic['Month']
# Arctic_abund_net = df_Arctic['ind'] 

# phyto_Arctic = np.log10(phytoarctic)
# Arctic_month_net = np.array(Arctic_month_net)
# Arctic_abund_genie = np.log10(Arctic_abund_genie)
# Arctic_abund_net = np.log10(Arctic_abund_net)


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


z =np.zeros((4,4)) 
fig, z = plt.subplots(4,4, sharex='col', sharey='row', figsize=(15,15))
fig.subplots_adjust(hspace=0.4, wspace=0.2)
# plt.xticks(rotation=45)
# plt.margins(x=0)
color = 'black'
color1 = 'tab:blue'
color2 = 'tab:brown'
###---------------------------------------- biotrans57N -------------------------------------------------------###

plt.subplot(4,4,1)
plt.margins(x=0)
plt.xticks(rotation=45)
ax1[3, 1].set_ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, biotrans57_genie1, color = color1) #row=0, col=0
obsv = plt.plot(biotrans57N_month_net, biotrans57N_abund_net, marker='o', linestyle='none',markersize=5, color= color) #row=0, col=0
ax1[3, 1].tick_params(axis='y', labelcolor= color)


plt.title('Biotrans 57N(loc 1)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- Labrador Sea -------------------------------------------------------###

plt.subplot(4,4,2)
plt.margins(x=0)
plt.xticks(rotation=45)
plt.ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, Ladrador_Sea_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Labrador_month_net, Labrador_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0



plt.title('Labrador Sea (loc 2)')
plt.margins(x=0)
plt.xticks(rotation=45)



###---------------------------------------- NW Atlantic -------------------------------------------------------###
plt.subplot(443)
plt.ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, Atlantic_Current_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Atlantic_Current_month_net, Atlantic_Current_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0


plt.title('NW Atlantic (loc 3)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------ BIOTRANS 47n ----------------------------------------------------###
plt.subplot(444)
plt.ylim([-1.0, 2.5])
x,y= (biotrans47_genie1, month_genie)
x1, y1 = (biotrans47_genie1, month_genie)
model1 = plt.plot(y, x, color = color1) #row=0, col=0
obsv =  plt.plot(biotrans47N_month_net, biotrans47_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0


plt.title('Biotrans 47N (loc 4)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  Japan Front ----------------------------------------------------###
plt.subplot(445)
plt.ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, Japan_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Japan_month_net, Japan_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0



plt.title('NW Pacific (Japan Front, loc 5)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- AZORES ------------------------------------------------------###
plt.subplot(446)
model1 = plt.plot(month_genie, Azores_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Azores_month_net, Azores_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
obsv1 = plt.scatter(Azores_month_net_Jan, Azores_abund_net_Jan, marker = 'o', facecolors='none', edgecolors='black') #row=0, col=0
plt.ylim([-1.0, 2.5])


plt.title('Azores front (loc 6)')
plt.margins(x=0)
plt.xticks(rotation=45)

###---------------------------------------- NE_Atlantic ------------------------------------------------------###
plt.subplot(447)
model1 = plt.plot(month_genie, NE_Atlantic_genie1, color = color1) #row=0, col=0
obsv = plt.plot(NE_Atlantic_month_net, NE_Atlantic_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
plt.ylim([-1.0, 2.5])

plt.title('NE Atlantic (loc 7)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  BRAZIL 34S ----------------------------------------------------###
plt.subplot(448)
plt.ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, Brazil34_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Brazil_34_month_net, Brazil_34_abund_net, marker='o', linestyle='none', markersize=7, color= color) #row=0, col=0


plt.title('SE Brazilian margin 34S (loc 8)')
plt.margins(x=0)
plt.xticks(rotation=45)



###------------------------------  Caribbean ----------------------------------------------------###
plt.subplot(449)
model1 = plt.plot(month_genie, Caribbean_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Caribbean_month_net, Caribbean_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
plt.ylim([-1.0, 2.5])


plt.title('Caribbean Sea (loc 9)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  BRAZIL 23S ----------------------------------------------------###
plt.subplot(4,4,10)
model1 = plt.plot(month_genie, Brazil23_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Brazil_23_month_net, Brazil_23_abund_net, marker='o', linestyle='none', markersize=7, color= color) #row=0, col=0
plt.ylim([-1.0, 2.5])


plt.title('SE Brazilian margin 23S (loc 10)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  California ----------------------------------------------------###

plt.subplot(4,4,11)
plt.ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, California_genie1, color = color1) #row=0, col=0
obsv = plt.plot(California_month_net, California_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0


plt.title('California Upwelling (loc 11)')
plt.margins(x=0)
plt.xticks(rotation=45)

###------------------------------  Panama ----------------------------------------------------###

plt.subplot(4,4,12)
model1 = plt.plot(month_genie, Panama_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Panama_month_net, Panama_abund_net, marker='o', linestyle='none', markersize=5, color= color) #row=0, col=0
plt.ylim([-1.0, 2.5])

plt.title('Panama Basin Upwelling (loc 12)')
plt.margins(x=0)
plt.xticks(rotation=45)


###------------------------------  Arabian Sea ----------------------------------------------------###

plt.subplot(4,4,13)
plt.ylim([-1.0, 2.5])
model1 = plt.plot(month_genie, Arabian_genie1, color = color1) #row=0, col=0
obsv = plt.plot(Arabian_month_net, Arabian_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0



plt.title('Arabian Sea Upwelling (loc 13)')
plt.margins(x=0)
plt.xticks(rotation=45)
###------------------------------  SE_Atlantic ----------------------------------------------------###
plt.subplot(4,4,14)
model1 = plt.plot(month_genie, SE_Atlantic_genie1, color = color1) #row=0, col=0
obsv = plt.plot(SE_Atlantic_month_net, SE_Atlantic_abund_net, marker='o', linestyle='none', markersize=5,color= color) #row=0, col=0
plt.ylim([-1.0, 2.5])

plt.title('SE Atlantic Upwelling (loc 14)')
plt.margins(x=0)
plt.xticks(rotation=45)


################ ------------------------------------------------------------------------------------ ###########

label = [ "model",  "obsv"]
fig.legend((model1, obsv,),labels= label,
            loc = 'upper right', 
            #ncol=3,
            frameon=False, 
            fontsize=14) 

fig.text(0.50, 0.95,
        'Foraminifera monthly abundance (ind C m$^{-3}$)',
        ha='center', fontsize = 16)

fig.text(0.080, 0.25,
        'Log10 abundance (ind C m$^{-3}$)',
        ha='center', rotation = 'vertical', fontsize = 16)
		

fig.text(0.50, 0.03,
        'Time (months)',
        ha='center', fontsize = 16)


plt.show()

#fig.savefig('D:\myimage1.tiff', format='tiff', dpi=300)




