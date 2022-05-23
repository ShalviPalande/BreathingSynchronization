import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb

breathingData =  pd.read_excel("/Users/shalvipalande/Desktop/syncscore.xlsx",sheet_name = "RRModerate")

df = pd.DataFrame(breathingData)

fig = go.Figure()
# Create and style traces

fig.add_trace(go.Box(y=df.Baseline, name='Baseline',marker_color='mediumaquamarine'))
fig.add_trace(go.Box(y=df.Visual, name='Visual',marker_color='mediumturquoise'))
fig.add_trace(go.Box(y=df.Vibro, name='Vibrotactile',marker_color=' mediumvioletred'))
fig.add_trace(go.Box(y=df.VisualVibro, name='VisualVibro',marker_color='mediumorchid'))
fig.add_trace(go.Box(y=df.InSync, name='InSync',marker_color='mediumpurple'))


fig.update_layout(
     title=go.layout.Title(
        text="Rate Sync <br><sup>(using Pearson R  >=  0.5 (Moderate Correlation) )</sup>"),
    xaxis_title="Modality",
    yaxis_title="Duration of Synchronization(s)",
    legend_title="Correlation by Modality ",
     showlegend = False,
    font=dict(
         family="Montserrat",
        size=15,
         color="Black"
    )
)
fig.show()


