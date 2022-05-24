import math
import csv
import serial
import neurokit2 as nk
import numpy as np
import pandas as pd
import time
from scipy.signal import hilbert, butter, find_peaks, lfilter, filtfilt
import logging
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
from chart_studio import plotly
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import plotly.express as px


filename1 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp15/User1.csv"
filename2 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp15/User2.csv"
try:
    breathingData1 =  pd.read_csv(filename1, encoding='cp1252')
    breathingData2 =  pd.read_csv(filename2, encoding='cp1252')
    breathingData1.columns=['timestamp','value', 'type']
    breathingData2.columns=['timestamp','value', 'type']

except IOError:
    logging.error('Could not open file with breathing data')

'''
#user1
baseline1_df = breathingData1[breathingData1['type'] == 'Baseline']
visual1_df = breathingData1[breathingData1['type'] == 'Visual']
vibro1_df = breathingData1[breathingData1['type'] == 'Vibrotactile']
visualvibro1_df = breathingData1[breathingData1['type'] == 'VisualVibro']
insync1_df = breathingData1[breathingData1['type'] == 'InSync']

#user2
baseline2_df = breathingData2[breathingData2['type'] == 'Baseline']
visual2_df = breathingData2[breathingData2['type'] == 'Visual']
vibro2_df = breathingData2[breathingData2['type'] == 'Vibrotactile']
visualvibro2_df = breathingData2[breathingData2['type'] == 'VisualVibro']
insync2_df = breathingData2[breathingData2['type'] == 'InSync']
'''

##############
# COMPUTE TIME (for X-AXIS) FOR EACH DF - ALL (depends on fs, i.e., SAMPLING RATE)
##############
#User1
reltime1 = np.arange(0, breathingData1.shape[0], 1)
reltime1 = reltime1/20 # 20Hz   #sampling rate because of delay(50) in arduino(if data lag then change delay)
breathingData1['reltime1',1] = reltime1

'''
## time for baseline breathing
reltime_baseline1 = np.arange(0, baseline1_df.shape[0], 1)
reltime_baseline1 = reltime_baseline1/20
baseline1_df['reltime_baseline1',1] = reltime_baseline1

## time for visual breathing
reltime_visual1 = np.arange(0, visual1_df.shape[0], 1)
reltime_visual1 = reltime_visual1/20
visual1_df['reltime_visual1',1] = reltime_visual1

## time for vibro breathing 
reltime_vibro1 = np.arange(0, vibro1_df.shape[0], 1)
reltime_vibro1 = reltime_vibro1/20
vibro1_df['reltime_vibro1',1] = reltime_vibro1

## time for visualvibro breathing
reltime_visualvibro1 = np.arange(0, visualvibro1_df.shape[0], 1)
reltime_visualvibro1 = reltime_visualvibro1/20
visualvibro1_df['reltime_visualvibro1',1] = reltime_visualvibro1

## time for insync breathing
reltime_insync1 = np.arange(0, insync1_df.shape[0], 1)
reltime_insync1 = reltime_insync1/20
insync1_df['reltime_insync1',1] = reltime_insync1
'''

#User2
reltime2 = np.arange(0, breathingData2.shape[0], 1)
reltime2 = reltime2/20 # 20Hz   #sampling rate because of delay(50) in arduino(if data lag then change delay)
breathingData2['reltime2',1] = reltime2

'''
## time for baseline breathing
reltime_baseline2 = np.arange(0, baseline2_df.shape[0], 1)
reltime_baseline2 = reltime_baseline2/20
baseline2_df['reltime_baseline2',1] = reltime_baseline2

## time for visual breathing
reltime_visual2 = np.arange(0, visual2_df.shape[0], 1)
reltime_visual2 = reltime_visual2/20
visual2_df['reltime_visual2',1] = reltime_visual2

## time for vibro breathing 
reltime_vibro2 = np.arange(0, vibro2_df.shape[0], 1)
reltime_vibro2 = reltime_vibro2/20
vibro2_df['reltime_vibro2',1] = reltime_vibro2

## time for visualvibro breathing
reltime_visualvibro2 = np.arange(0, visualvibro2_df.shape[0], 1)
reltime_visualvibro2 = reltime_visualvibro2/20
visualvibro2_df['reltime_visualvibro2',1] = reltime_visualvibro2

## time for insync breathing
reltime_insync2 = np.arange(0, insync2_df.shape[0], 1)
reltime_insync2 = reltime_insync2/20
insync2_df['reltime_insync2',1] = reltime_insync2
'''

##############
# NORMALIZE THE DFs
##############
def normalize(breathing):
    normalizedBreathing = []
    mean = np.mean(breathing)
    std = np.std(breathing)
    #print(len(breathing))
    i=0
    
    while i < len(breathing):
        normalizedBreathing.append((breathing.iloc[i]-mean)/np.std(breathing))
        i+=1
    return normalizedBreathing

#FOR USER 1
#Normalize the breathing signal
normalized_breathingData1 = normalize(breathingData1.value)
breathingData1['normalizedValue'] = normalized_breathingData1

'''
#Normalize the baseline breathing signal
normalized_baseline1 = normalize(baseline1_df.value)
baseline1_df['normalizedValue'] = normalized_baseline1

#Normalize the visual breathing signal
normalized_visual1 = normalize(visual1_df.value)
visual1_df['normalizedValue'] = normalized_visual1

#Normalize the vibro breathing signal
normalized_vibro1 = normalize(vibro1_df.value)
vibro1_df['normalizedValue'] = normalized_vibro1

#Normalize the visualvibro breathing signal
normalized_visualvibro1 = normalize(visualvibro1_df.value)
visualvibro1_df['normalizedValue'] = normalized_visualvibro1

#Normalize the insync breathing signal
normalized_insync1 = normalize(insync1_df.value)
insync1_df['normalizedValue'] = normalized_insync1

'''
#FOR USER 2
#Normalize the breathing signal
normalized_breathingData2 = normalize(breathingData2.value)
breathingData2['normalizedValue'] = normalized_breathingData2
'''

#Normalize the baseline breathing signal
normalized_baseline2 = normalize(baseline2_df.value)
baseline2_df['normalizedValue'] = normalized_baseline2

#Normalize the visual breathing signal
normalized_visual2 = normalize(visual2_df.value)
visual2_df['normalizedValue'] = normalized_visual2

#Normalize the vibro breathing signal
normalized_vibro2 = normalize(vibro2_df.value)
vibro2_df['normalizedValue'] = normalized_vibro2

#Normalize the visualvibro breathing signal
normalized_visualvibro2 = normalize(visualvibro2_df.value)
visualvibro2_df['normalizedValue'] = normalized_visualvibro2

#Normalize the insync breathing signal
normalized_insync2 = normalize(insync2_df.value)
insync2_df['normalizedValue'] = normalized_insync2
'''

##############
# BUTTERWORTH FILTER
##############

def butter_lowpass_filter(data, cutoff, fs, order):
    baseline_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, baseline_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

## filter requirements

# T = 16.83         # Sample Period (NOT USED)
fs = 20.0       # sample rate, Hz
cutoff = 2      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
nyq = 0.5 * fs  # Nyquist Frequency = 50
order = 2       # sin wave can be approx represented as quadratic
# n = int(T * fs) # total number of samples (NOT USED)


## Filter the data, and plot both the original and filtered signals.
#User1
ybreathingdata1 = butter_lowpass_filter(normalized_breathingData1, cutoff, fs, order)
'''
yb1 = butter_lowpass_filter(normalized_baseline1, cutoff, fs, order)
yv1 = butter_lowpass_filter(normalized_visual1, cutoff, fs, order)
yvb1 = butter_lowpass_filter(normalized_vibro1, cutoff, fs, order)
yvv1 = butter_lowpass_filter(normalized_visualvibro1, cutoff, fs, order)
yi1 = butter_lowpass_filter(normalized_insync1, cutoff, fs, order)
'''

#User2
ybreathingdata2 = butter_lowpass_filter(normalized_breathingData2, cutoff, fs, order)

'''
yb2 = butter_lowpass_filter(normalized_baseline2, cutoff, fs, order)
yv2 = butter_lowpass_filter(normalized_visual2, cutoff, fs, order)
yvb2 = butter_lowpass_filter(normalized_vibro2, cutoff, fs, order)
yvv2 = butter_lowpass_filter(normalized_visualvibro2, cutoff, fs, order)
yi2 = butter_lowpass_filter(normalized_insync2, cutoff, fs, order)
'''


'''
##############
# RSP RATE
##############
#User 1
rsp_ratebreathingdata1 = nk.rsp_rate(ybreathingdata1, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm baseline 1: ", np.mean(rsp_ratebreathingdata1))

rsp_rateb1 = nk.rsp_rate(yb1, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm baseline 1: ", np.mean(rsp_rateb1))

rsp_ratev1 = nk.rsp_rate(yv1, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm visual 1: ", np.mean(rsp_ratev1))

rsp_ratevb1 = nk.rsp_rate(yvb1, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm vibro 1: ", np.mean(rsp_ratevb1))

rsp_ratevv1 = nk.rsp_rate(yvv1, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm visualvibro1: ", np.mean(rsp_ratevv1))

rsp_ratei1 = nk.rsp_rate(yi1, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm insync 1: ", np.mean(rsp_ratei1))


#User 2
rsp_ratebreathingdata2 = nk.rsp_rate(ybreathingdata2, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm baseline 1: ", np.mean(rsp_ratebreathingdata2))

rsp_rateb2 = nk.rsp_rate(yb2, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm baseline 2: ", np.mean(rsp_rateb2))

rsp_ratev2 = nk.rsp_rate(yv2, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm visual 2: ", np.mean(rsp_ratev2))

rsp_ratevb2 = nk.rsp_rate(yvb2, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm vibro 2: ", np.mean(rsp_ratevb2))

rsp_ratevv2 = nk.rsp_rate(yvv2, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm visualvibro 2: ", np.mean(rsp_ratevv2))

rsp_ratei2 = nk.rsp_rate(yi2, sampling_rate=20, method="peak") # Note: You can also replace info with peaks dictionary
print("bpm insync 2: ", np.mean(rsp_ratei2))
'''

########
#RSP PROCESS
######
#User 1
signalsbd1, infobd1 = nk.rsp_process(ybreathingdata1, sampling_rate=20)
signalsbd1.to_csv('/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp15/ProcessedData1.csv')
#User 2
signalsbd2, infobd2 = nk.rsp_process(ybreathingdata2, sampling_rate=20)
signalsbd2.to_csv('/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp15/ProcessedData2.csv') 


'''
signalsb1, infob1 = nk.rsp_process(yb1, sampling_rate=20)
figb1 = nk.rsp_plot(signalsb1)
figb1.show()

signalsv1, infob1 = nk.rsp_process(yv1, sampling_rate=20)
figv1 = nk.rsp_plot(signalsv1)
figv1.show()

signalsvb1, infovb1 = nk.rsp_process(yvb1, sampling_rate=20)
figvb1 = nk.rsp_plot(signalsvb1)
figvb1.show()

signalsvv1, infovv1 = nk.rsp_process(yvv1, sampling_rate=20)
figvv1 = nk.rsp_plot(signalsvv1)
figvv1.show()

signalsi1, infoi1 = nk.rsp_process(yi1, sampling_rate=20)
figi1 = nk.rsp_plot(signalsi1)
figi1.show()
'''

#User 2
signalsbd2, infobd2 = nk.rsp_process(ybreathingdata2, sampling_rate=20)
#figbd2 = nk.rsp_plot(signalsbd2)
signalsbd2.to_csv('/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp15/ProcessedData2.csv') 
#figbd2.show()

'''
signalsb2, infob2 = nk.rsp_process(yb2, sampling_rate=20)
figb2 = nk.rsp_plot(signalsb2)
figb2.show()

signalsv2, infob2 = nk.rsp_process(yv2, sampling_rate=20)
figv2 = nk.rsp_plot(signalsv2)
figv2.show()

signalsvb2, infovb2 = nk.rsp_process(yvb2, sampling_rate=20)
figvb2 = nk.rsp_plot(signalsvb2)
figvb2.show()

signalsvv2, infovv2 = nk.rsp_process(yvv2, sampling_rate=20)
figvv2 = nk.rsp_plot(signalsvv2)
figvv2.show()

signalsi2, infoi2 = nk.rsp_process(yi2, sampling_rate=20)
figi2 = nk.rsp_plot(signalsi2)
figi2.show()
'''

########
#SIGNAL SYNCHRONY
######

coupling_h = nk.signal_synchrony(ybreathingdata1, ybreathingdata2, method="hilbert")
pd.DataFrame(coupling_h).to_csv('/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp15/SyncData.csv')

