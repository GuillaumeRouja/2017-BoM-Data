# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:36:48 2019

@author: guill
"""

import pandas as pd
import glob
import math 

def Datastations (station,path): # Collect and compile all weather csv files for a given period
    allFiles = glob.glob(path + "/*.csv") 
    list_ = []
    array = ['T', 'MinT','MaxT','Precip','AIR_TEMP','AIR_TEMP_MIN','AIR_TEMP_MAX','PRCP'] #create array of rows to be kept
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        df = df[df.station_number==station]
        df = df.loc[df['parameter'].isin(array)] #Keep the rows we need (NB:useless columns will be droped at cleaning stage)
        list_.append(df)  
    frame = pd.concat(list_,ignore_index=True)
    return (frame)


#Create a warning line each time a period of at least 5 consecutive days without data is identified

def Datagap (parameter,df):
    k=0
    for i in range(len(df)):
        if (math.isnan(df[parameter].values[i])):
            k=k+1
            if (k>=120):
                print ('Warning datagap >= 5 days: check your data',parameter)
                k=0
        else:
            k=0
            

#Filling missing weather data based on x previous/following day(s)#

def Datafilling (parameter,df):
    for i in range(len(df)):
        j=0 #initialize counter of loops to find data at a given hour
        if (math.isnan(df[parameter].values[i])): #if a data is missing      
            while (j<6): #We allow a maximum of 5 missing data at a given hour either before or after current time
                j=j+1 #increment counter of loops to find missing data
                if (math.isnan(df[parameter].values[i-j*24]))== False: #if a data is found:
                    df[parameter].values[i] = df[parameter].values[i-j*24] #missing data is filled with data from x previous day
                    j=6 #Exit the loop and start a new count
                else: #if data not found at D-1 we look at D+1 then D-2, D+2, etc.
                    if (math.isnan(df[parameter].values[i+j*24]))== False: #if a data is found 
                        df[parameter].values[i] = df[parameter].values[i+j*24] #missing data is filled with data from x following day
                        j=6 #Exit the loop and start a new count


