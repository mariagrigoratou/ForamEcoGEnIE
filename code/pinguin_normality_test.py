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
x = subpolar_present    = pd.read_excel('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\\genie_outpout.xlsx', sheet_name='subpolar_STATS_foram_only',   usecols = "Q")
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

#################################################################################################################################################################
#check for the normality of the dataset 
#subpolar 
nor_subpolar_present    = pg.normality(subpolar_present)
nor_subpolar_2050rcp8p5 = pg.normality(subpolar_2050rcp8p5)
nor_subpolar_2100rcp8p5 = pg.normality(subpolar_present)
#nor_subpolar_2100rcp6   = pg.normality(subpolar_present)
#temperate 
nor_temp_present    = pg.normality(temp_present)
nor_temp_2050rcp8p5 = pg.normality(temp_2050rcp8p5)
nor_temp_2100rcp8p5 = pg.normality(temp_present)
nor_temp_2100rcp6   = pg.normality(temp_present)
#tropics 
nor_trop_present    = pg.normality(trop_present)
nor_trop_2050rcp8p5 = pg.normality(trop_2050rcp8p5)
nor_trop_2100rcp8p5 = pg.normality(trop_present)
nor_trop_2100rcp6   = pg.normality(trop_present)
#Indian Ocean
#temperate 
nor_io_present    = pg.normality(io_present)
nor_io_2050rcp8p5 = pg.normality(io_2050rcp8p5)
nor_io_2100rcp8p5 = pg.normality(io_present)
nor_io_2100rcp6   = pg.normality(io_present)


#save output in an excel file 
writer = pd.ExcelWriter('E:\PHD\FORAMECOGENIE_MARCH_2020\EXCEL_METAANALYSIS\FUTURE\RCP\pingouin_output\\normality_data_check_forams_only.xlsx', engine='xlsxwriter')
workbook = writer.book
#polar
nor_subpolar_present.to_excel(writer, 'subpolar',startcol=0,startrow=0)
nor_subpolar_2050rcp8p5.to_excel(writer, 'subpolar',startcol=5,startrow=0)
nor_subpolar_2100rcp8p5.to_excel(writer, 'subpolar',startcol=10,startrow=0)
nor_subpolar_2100rcp6.to_excel(writer, 'subpolar',startcol=15,startrow=0)
#temp
nor_temp_present.to_excel(writer, 'temp',startcol=0,startrow=0)
nor_temp_2050rcp8p5.to_excel(writer, 'temp',startcol=5,startrow=0)
nor_temp_2100rcp8p5.to_excel(writer, 'temp',startcol=10,startrow=0)
nor_temp_2100rcp6.to_excel(writer, 'temp',startcol=15,startrow=0)
#trop
nor_trop_present.to_excel(writer, 'trops',startcol=0,startrow=0)
nor_trop_2050rcp8p5.to_excel(writer, 'trops',startcol=5,startrow=0)
nor_trop_2100rcp8p5.to_excel(writer, 'trops',startcol=10,startrow=0)
nor_trop_2100rcp6.to_excel(writer, 'trops',startcol=15,startrow=0)
#Indian Ocean
nor_io_present.to_excel(writer, 'io',startcol=0,startrow=0)
nor_io_2050rcp8p5.to_excel(writer, 'io',startcol=5,startrow=0)
nor_io_2100rcp8p5.to_excel(writer, 'io',startcol=10,startrow=0)
nor_io_2100rcp6.to_excel(writer, 'io',startcol=15,startrow=0)
writer.close()


#################################################################################################################################################################