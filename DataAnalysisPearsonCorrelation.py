import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, filtfilt
import neurokit2 as nk
import logging
from plotly.subplots import make_subplots
import plotly.express as px
import scipy.stats
from scipy.stats import pearsonr


filename1 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp1/User1.csv"
filename2 = "/Users/shalvipalande/Desktop/FinalExperimentDataLogging/Exp1/User2.csv"

try:
    breathingData1 =  pd.read_csv(filename1, encoding='cp1252')
    breathingData2 =  pd.read_csv(filename2, encoding='cp1252')
    breathingData1.columns=['timestamp','value', 'type']
    breathingData2.columns=['timestamp','value', 'type']

except IOError:
    logging.error('Could not open file with breathing data')
    
#user1
#baseline1_df = breathingData1[breathingData1['type'] == 'Baseline']
#visual1_df = breathingData1[breathingData1['type'] == 'Visual']
#vibro1_df = breathingData1[breathingData1['type'] == 'Vibrotactile']
#visualvibro1_df = breathingData1[breathingData1['type'] == 'VisualVibro']
insync1_df = breathingData1[breathingData1['type'] == 'InSync']

#user2
#baseline2_df = breathingData2[breathingData2['type'] == 'Baseline']
#visual2_df = breathingData2[breathingData2['type'] == 'Visual']
#vibro2_df = breathingData2[breathingData2['type'] == 'Vibrotactile']
#visualvibro2_df = breathingData2[breathingData2['type'] == 'VisualVibro']
insync2_df = breathingData2[breathingData2['type'] == 'InSync']


##############
# Normalize the DFs
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


##############
# Butterworth Filter
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


#Filter the data, and plot both the original and filtered signals.
yb1 = butter_lowpass_filter(normalized_baseline1, cutoff, fs, order)
yv1 = butter_lowpass_filter(normalized_visual1, cutoff, fs, order)
yvb1 = butter_lowpass_filter(normalized_vibro1, cutoff, fs, order)
yvv1 = butter_lowpass_filter(normalized_visualvibro1, cutoff, fs, order)
yi1 = butter_lowpass_filter(normalized_insync1, cutoff, fs, order)

yb2 = butter_lowpass_filter(normalized_baseline2, cutoff, fs, order)
yv2 = butter_lowpass_filter(normalized_visual2, cutoff, fs, order)
yvb2 = butter_lowpass_filter(normalized_vibro2, cutoff, fs, order)
yvv2 = butter_lowpass_filter(normalized_visualvibro2, cutoff, fs, order)
yi2 = butter_lowpass_filter(normalized_insync2, cutoff, fs, order)

#Create dataframes for plotting graphs/further analysis etc.
dfb1 = pd.DataFrame(yb1)
dfb2 = pd.DataFrame(yb2)
dfv1 = pd.DataFrame(yv1)
dfv2 = pd.DataFrame(yv2)
dfvb1 = pd.DataFrame(yvb1)
dfvb2 = pd.DataFrame(yvb2)
dfvv1 = pd.DataFrame(yvv1)
dfvv2 = pd.DataFrame(yvv2)
dfi1 = pd.DataFrame(yi1)
dfi2 = pd.DataFrame(yi2)

########
#Pearson Rolling Window Correlation
########
Pcorrb = dfb1.rolling(250).corr(dfb2)
Pcorrv = dfv1.rolling(250).corr(dfv2)
Pcorrvb = dfvb1.rolling(250).corr(dfvb2)
Pcorrvv = dfvv1.rolling(250).corr(dfvv2)
Pcorri = dfi1.rolling(250).corr(dfi2)
