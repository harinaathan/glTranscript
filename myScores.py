#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
# In[3]:


df = pd.read_excel("scoreLog.xlsx")
dfP = df.copy()
dfP["My Score"] = dfP["My Score"].div(dfP["Total Score"])
dfP["Batch Median Score"] = dfP["Batch Median Score"].div(dfP["Total Score"])
dfP["Batch Max Score"] = dfP["Batch Max Score"].div(dfP["Total Score"])
dfP = dfP[["Course","My Score","Batch Median Score","Batch Max Score"]]


# In[4]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=dfP.Course,y=dfP["Batch Median Score"],mode='none',fill='tozeroy',name="Batch Median Score"))
fig.add_trace(go.Scatter(x=dfP.Course,y=dfP["Batch Max Score"],mode='none',fill='tonexty',name="Batch Max Score"))
fig.add_trace(go.Bar(x=dfP.Course,y=dfP["My Score"],))

