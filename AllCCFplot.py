import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt

breathingData =  pd.read_excel("/Users/shalvipalande/Desktop/ExperimentDataLogging/AllCCF/AllExpDataInSync.xlsx")
#breathingData.columns=['lag','xcorr1','xcorr2','xcorr3','xcorr4','xcorr5','xcorr6','xcorr7','xcorr8','xcorr8','xcorr9','xcorr10','xcorr11','xcorr12','xcorr13','xcorr14','xcorr15',]

df = pd.DataFrame(breathingData)
#print(df)


fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr1, name='Exp1', 
                         line=dict(color='royalblue', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr2, name='Exp2', 
                         line=dict(color='magenta', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr3, name='Exp3', 
                         line=dict(color='mediumblue', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr4, name='Exp4', 
                         line=dict(color='mediumorchid', width=3, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr5, name='Exp5', 
                         line=dict(color='mediumpurple', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr6, name='Exp6', 
                         line=dict(color='mediumseagreen', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr7, name='Exp7', 
                         line=dict(color='mediumslateblue', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr8, name='Exp8', 
                         line=dict(color='mediumspringgreen', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr9, name='Exp9', 
                         line=dict(color='mediumturquoise', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr10, name='Exp10', 
                         line=dict(color='mediumvioletred', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr11, name='Exp11', 
                         line=dict(color='midnightblue', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr12, name='Exp12', 
                         line=dict(color='powderblue', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr13, name='Exp13', 
                         line=dict(color='tomato', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr14, name='Exp14', 
                         line=dict(color='sienna', width=1, shape = 'spline')))

fig.add_trace(go.Scatter(x = df.lag, y = df.xcorr15, name='Exp15', 
                         line=dict(color='maroon', width=1, shape = 'spline')))

fig.update_layout(
     title="Experiment : InSync CCF",
    xaxis_title="lag",
    yaxis_title="CCF",
    legend_title="CCF",
    font=dict(
         family="Montserrat",
        size=15,
         color="Black"
    )
)
fig.show()


