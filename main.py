#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# In[2]:
df = pd.read_csv("./scoreLog.csv")
dfP = df.copy()
dfP["My Score"] = dfP["My Score"].div(dfP["Total Score"]).round(3)
dfP["Batch Median Score"] = dfP["Batch Median Score"].div(dfP["Total Score"]).round(3)
dfP["Batch Max Score"] = dfP["Batch Max Score"].div(dfP["Total Score"]).round(3)
dfP = dfP[["Course","My Score","Batch Median Score","Batch Max Score"]]

# In[3]:
fig = go.Figure()
fig.add_trace(go.Bar(x=dfP.Course,y=dfP["My Score"],name="My Score",hovertemplate="My Score<br>%{y}"))
fig.add_trace(go.Scatter(x=dfP.Course,y=dfP["Batch Median Score"],fillcolor='rgba(99, 110, 250,1)',
                         name="Batch Median Score",hovertemplate="Batch Median Score<br>%{y}"))
fig.add_trace(go.Scatter(x=dfP.Course,y=dfP["Batch Max Score"],fillcolor='rgba(239, 85, 59,1)',
                         name="Batch Max Score",hovertemplate="Batch Max Score<br>%{y}"))
fig.update_yaxes(title=dict(text="Score",standoff=0),
                 type='log',tickformat='0%')
fig.update_xaxes(title=dict(text="Modules",standoff=0))
fig.update_layout(legend=dict(yanchor='bottom',y=1,orientation='h',xanchor='right',x=1))
fig.update_layout(title=dict(text='My learning curve through the course',
                             yanchor='top',y=0.9,xanchor='left',x=0))
fig.update_layout(autosize=False,height=500,width=500);

# In[4]:
st.title('Check this out')
st.plotly_chart(fig)
