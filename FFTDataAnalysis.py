import math
import csv
import serial
import neurokit2 as nk
import numpy as np
import pandas as pd
import time
from scipy.signal import hilbert, butter, find_peaks
import logging

##############
# LOAD DATA AND PLACE INTO PANDAS DATAFRAMES
##############
## NOTE: this csv only contains the NORMAL breathing data
## All types of data (type column : 5 conditions)(TODO, do for user1 first and then juust copy paste for user2)
#data is saved in two different files for each user
            
filename1 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp2/User1.csv"
filename2 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp2/User2.csv"

try:
    breathingData1 =  pd.read_csv(filename1)
    breathingData2 =  pd.read_csv(filename2)
    #Breathing data contains timestamp, relative time from start which is 0s , value of raw breathing signal, other irrelevant data
    breathingData1.columns=['timestamp','value', 'type']
    breathingData2.columns=['timestamp','value', 'type']
    logging.info('File was opened and breathing data is copied into a Pandas dataframe')
    
except IOError:
    logging.error('Could not open file with breathing data')

##############
# CLEAN THE DFs
##############
clean_data1 = nk.rsp_clean(breathingData1.value, sampling_rate=20, method="khodadad2018")
breathingData1['clean_data1'] = clean_data1
print("Cleaned Signal 1: ",clean_data1)
df1 = pd.DataFrame(clean_data1)

clean_data2 = nk.rsp_clean(breathingData2.value, sampling_rate=20, method="khodadad2018")
breathingData1['clean_data2'] = clean_data1
print("Cleaned Signal 2: ",clean_data2)
df2 = pd.DataFrame(clean_data2)

##############
# NORMALIZE THE DFs
##############
def normalize(breathing):
    normalizedBreathing = []
    mean = np.mean(breathing)
    std = np.std(breathing)
    #print("Normalized length: ",len(breathing))
    i=0
    
    while i < len(breathing):
        normalizedBreathing.append((breathing.iloc[i]-mean)/np.std(breathing))
        i+=1
    return normalizedBreathing

#FOR USER 1
#Normalize the breathing signal
normalized_breathingData1 = normalize(df1)
breathingData1['normalizedValue1'] = normalized_breathingData1
print("Normalized Value 1: ",normalized_breathingData1)
dataframe1 = pd.DataFrame(normalized_breathingData1)

#FOR USER 2
#Normalize the breathing signal
normalized_breathingData2 = normalize(df2)
breathingData2['normalizedValue2'] = normalized_breathingData2
print("Normalized Value 2: ",normalized_breathingData2)
dataframe2 = pd.DataFrame(normalized_breathingData2)


#####
#RSP PROCESSING SYNCSCORE
#####
syncScore = nk.signal_synchrony(dataframe1,dataframe2, method="hilbert")
print("SyncScore: ",syncScore)
