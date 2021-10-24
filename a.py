# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:31:10 2021

@author: ignac
"""

import netCDF4 as nc

import pandas as pd

res = nc.Dataset('2018.nc4','r')




res.variables


LON_2018 = res.variables["longitude"][:]
LAT_2018 = res.variables["latitude"][:]
TIME_2018 = res.variables["time"][:]
TDROP_2018 = res.variables["tdrop"][0,:,:]
TBAR_2018 = res.variables["tbar"][0,:,:]
TSKINICE_2018 = res.variables["tskinice"][0,:,:]
RAINOCN_2018 = res.variables["rainocn"][0,:,:]
DELTS_2018 = res.variables["delts"][0,:,:]


LAT_TDROP_2018 = TDROP_2018[:,0]
LON_TDROP_2018 = TDROP_2018[0,:]

LAT_TBAR_2018 = TBAR_2018[:,0]
LON_TBAR_2018 = TBAR_2018[0,:]

LAT_TSKINICE_2018 = TSKINICE_2018[:,0]
LON_TSKINICE_2018 = TSKINICE_2018[0,:]

LAT_RAINOCN_2018 = RAINOCN_2018[:,0]
LON_RAINOCN_2018 = RAINOCN_2018[0,:]

LAT_DELTS_2018 = DELTS_2018[:,0]
LON_DELTS_2018 = DELTS_2018[0,:]




df1 = pd.DataFrame()


datos = {
'LON_2018' : [res.variables["longitude"][:]],
'LAT_2018' : [res.variables["latitude"][:]],
'TIME_2018' : [res.variables["time"][:]],
'TDROP_2018' : [res.variables["tdrop"][0,:,:]],
'TBAR_2018' : [res.variables["tbar"][0,:,:]],
'TSKINICE_2018' : [res.variables["tskinice"][0,:,:]],
'RAINOCN_2018' : [res.variables["rainocn"][0,:,:]],
'DELTS_2018' : [res.variables["delts"][0,:,:]]}



df1 = df1.append(pd.DataFrame(data=datos))



print(df1)


print(df1.info)