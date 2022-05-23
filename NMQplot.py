import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

breathingData =  pd.read_excel("/Users/shalvipalande/Desktop/FinalExperimentDataLogging/AllNMQ.xlsx")

df = pd.DataFrame(breathingData)
#print(df)


#dd=pd.melt(df,id_vars=['Condition'],value_vars=['Selfcloseattention','Partnercloseattention'],var_name='Conditions')
#sns.boxplot(x='Condition',y='value',data=dd,hue='Conditions',palette="GnBu")

#dd=pd.melt(df,id_vars=['Condition'],value_vars=['Selfdistraction','Partnerdistraction'],var_name='Conditions')
#sns.boxplot(x='Condition',y='value',data=dd,hue='Conditions',palette="OrRd")

#dd=pd.melt(df,id_vars=['Condition'],value_vars=['Selfignore','Partnerignore'],var_name='Conditions')
#sns.boxplot(x='Condition',y='value',data=dd,hue='Conditions',palette="PiYG")

#dd=pd.melt(df,id_vars=['Condition'],value_vars=['Selfinfluence','Partnerinfluence'],var_name='Conditions')
#sns.boxplot(x='Condition',y='value',data=dd,hue='Conditions',palette="PuRd")

dd=pd.melt(df,id_vars=['Condition'],value_vars=['Selfdependence','Partnerdependence'],var_name='Conditions')
sns.boxplot(x='Condition',y='value',data=dd,hue='Conditions',palette="YlGn")

plt.show()


