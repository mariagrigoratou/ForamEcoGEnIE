## pearson 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import pingouin as pg
from pingouin import remove_na
from xlsxwriter.utility import xl_range
import xlsxwriter

#get the data
#subpolar 
subpolar_present    = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='subpolar_STATS_foram_only',   usecols = "B:Q")
subpolar_2050rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='subpolar_STATS_foram_only',   usecols = "T:AI") 
subpolar_2100rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='subpolar_STATS_foram_only',   usecols = "AL:BA") 
#subpolar_2100rcp6   = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='subpolar_STATS_foram_only',   usecols = "BD:BS")

#temperate 
temp_present    = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='temp_STATS_foram_only',   usecols = "B:Q") 
temp_2050rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='temp_STATS_foram_only',   usecols = "T:AI") 
temp_2100rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='temp_STATS_foram_only',   usecols = "AL:BA") 
temp_2100rcp6   = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='temp_STATS_foram_only',   usecols = "BD:BS") 

#tropics
trop_present    = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='trop_STATS_foram_only',   usecols = "B:Q") 
trop_2050rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='trop_STATS_foram_only',   usecols = "T:AI") 
trop_2100rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='trop_STATS_foram_only',   usecols = "AL:BA") 
trop_2100rcp6   = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='trop_STATS_foram_only',   usecols = "BD:BS") 

#Indian ocean
io_present    = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='io_STATS_foram_only',   usecols = "B:Q") 
io_2050rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='io_STATS_foram_only',   usecols = "T:AI") 
io_2100rcp8p5 = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='io_STATS_foram_only',   usecols = "AL:BA") 
io_2100rcp6   = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='io_STATS_foram_only',   usecols = "BD:BS") 

###########################################################################################################################
## spearman pairwise_corr, foram vs all
#subpolar 
corr_subpolar_present     = pd.DataFrame(pg.pairwise_corr(subpolar_present, columns=['foram'], method='spearman'))
corr_subpolar_2050rcp8p5 = pd.DataFrame(pg.pairwise_corr(subpolar_2050rcp8p5, columns=['foram.1'], method='spearman'))
corr_subpolar_2100rcp8p5  = pd.DataFrame(pg.pairwise_corr(subpolar_2100rcp8p5, columns=['foram.2'], method='spearman'))
#corr_subpolar_2100rcp6    = pd.DataFrame(pg.pairwise_corr(subpolar_2100rcp6, columns=['foram.3'], method='spearman'))
#temperate
corr_temp_present     = pd.DataFrame(pg.pairwise_corr(temp_present, columns=['foram'], method='spearman'))
corr_temp_2050rcp8p5 = pd.DataFrame(pg.pairwise_corr(temp_2050rcp8p5, columns=['foram.1'], method='spearman'))
corr_temp_2100rcp8p5  = pd.DataFrame(pg.pairwise_corr(temp_2100rcp8p5, columns=['foram.2'], method='spearman'))
corr_temp_2100rcp6    = pd.DataFrame(pg.pairwise_corr(temp_2100rcp6, columns=['foram.3'], method='spearman'))
#trop
corr_trop_present     = pd.DataFrame(pg.pairwise_corr(trop_present, columns=['foram'], method='spearman'))
corr_trop_2050rcp8p5 = pd.DataFrame(pg.pairwise_corr(trop_2050rcp8p5, columns=['foram.1'], method='spearman'))
corr_trop_2100rcp8p5  = pd.DataFrame(pg.pairwise_corr(trop_2100rcp8p5, columns=['foram.2'], method='spearman'))
corr_trop_2100rcp6    = pd.DataFrame(pg.pairwise_corr(trop_2100rcp6, columns=['foram.3'], method='spearman'))
#Indian Ocean 
corr_io_present     = pd.DataFrame(pg.pairwise_corr(io_present, columns=['foram'], method='spearman'))
corr_io_2050rcp8p5 = pd.DataFrame(pg.pairwise_corr(io_2050rcp8p5, columns=['foram.1'], method='spearman'))
corr_io_2100rcp8p5  = pd.DataFrame(pg.pairwise_corr(io_2100rcp8p5, columns=['foram.2'], method='spearman'))
corr_io_2100rcp6    = pd.DataFrame(pg.pairwise_corr(io_2100rcp6, columns=['foram.3'], method='spearman'))


###########################################################################################################################


result = pd.ExcelWriter('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\pingouin_output\\pairwise_corr_foram_only.xlsx', engine='xlsxwriter')
workbook = result.book
#subpolar
corr_subpolar_present.to_excel(result, 'subpolar',startcol=0,startrow=0)
corr_subpolar_2050rcp8p5.to_excel(result, 'subpolar',startcol=0,startrow=20)
corr_subpolar_2100rcp8p5.to_excel(result, 'subpolar',startcol=0,startrow=40)
corr_subpolar_2100rcp6.to_excel(result, 'subpolar',startcol=0,startrow=60)
#temperate
corr_temp_present.to_excel(result, 'temp',startcol=0,startrow=0)
corr_temp_2050rcp8p5.to_excel(result, 'temp',startcol=0,startrow=20)
corr_temp_2100rcp8p5.to_excel(result, 'temp',startcol=0,startrow=40)
corr_temp_2100rcp6.to_excel(result, 'temp',startcol=0,startrow=60)
#tropics
corr_trop_present.to_excel(result, 'trop',startcol=0,startrow=0)
corr_trop_2050rcp8p5.to_excel(result, 'trop',startcol=0,startrow=20)
corr_trop_2100rcp8p5.to_excel(result, 'trop',startcol=0,startrow=40)
corr_trop_2100rcp6.to_excel(result, 'trop',startcol=0,startrow=60)
#Indian Ocean
corr_io_present.to_excel(result, 'io',startcol=0,startrow=0)
corr_io_2050rcp8p5.to_excel(result, 'io',startcol=0,startrow=20)
corr_io_2100rcp8p5.to_excel(result, 'io',startcol=0,startrow=40)
corr_io_2100rcp6.to_excel(result, 'io',startcol=0,startrow=60)

result.close()


