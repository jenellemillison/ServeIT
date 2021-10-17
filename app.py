# -*- coding: utf-8 -*-
"""
Graphs based off of Annual_Payroll

@author: Zaqttack
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import time

st.set_page_config(
    page_title="ServiceIT",
    page_icon=":bell:",
)

PAYROLL = 'Annual_Payroll'
DATA_URL = ('https://raw.githubusercontent.com/jenellemillison/ServeIT/main/small_business_service_dataset.csv')

st.header(':bell: Welcome to **ServeIT** :bell:️')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, index_col=0, parse_dates=True)
    return data

# Load all rows into the dataframe
data = load_data(1453)

OPTION = st.selectbox(
    'How would you like to compare Annual Payroll?',
    ('Firms', 'Establishments')
)

st.subheader(PAYROLL + " vs " + OPTION)

chart = alt.Chart(data).mark_line().encode(
            x=alt.X(OPTION, axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y('Annual_Payroll'))
st.altair_chart(chart, use_container_width=True)

st.caption('The graph above represents the amount of payroll has available per the number of ' + OPTION + ' they currently have.')

with st.expander("Open to see the raw data"):
    st.subheader('Raw Data')
    st.write(data)
