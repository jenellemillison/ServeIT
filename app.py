# -*- coding: utf-8 -*-
"""
Graphs based off of Annual_Payroll

@author: Zaqttack
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import time

st.set_page_config(
    page_title="ServiceIT",
    page_icon=":bell:",
)

PAYROLL = 'Tot_Annual_Payroll'
DATA_URL = ('https://raw.githubusercontent.com/jenellemillison/ServeIT/main/small_business_service_dataset.csv')

st.header(':bell: Welcome to ServeIT :bell:')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, index_col=0, parse_dates=True)
    return data

# Load all rows into the dataframe
data = load_data(1453)

OPTION = st.selectbox(
    'How would you like to compare Annual Payroll?',
    ('Income', 'Firms', 'Establishments', 'MEDIAN_AGE_TOT')
)

st.subheader('Total Annual Payroll' + " vs " + OPTION)

chart = alt.Chart(data).mark_line().encode(
            x=alt.X(OPTION, axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y(PAYROLL))
st.altair_chart(chart, use_container_width=True)
st.caption('The graph above represents the amount of payroll a business has available per ' + OPTION + ' they currently have.')

# st.write(data.iloc[0:1, -1:])
# st.write(data.iloc[0:1, -2:-1])
# PERCENT_CHANGE = data.loc['Anderson', 'pct_chg_10_20']
# POPULATION = data.loc['Anderson', 'population']
# PERCENT_CHANGE.astype(int)
# st.metric(label="Population Change", value=PERCENT_CHANGE, delta=POPULATION)

st.subheader('Population by County')
df = data.copy()
st.pydeck_chart(pdk.Deck(
map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=29.42,
        longitude=-98.49,
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ColumnLayer',
            data=df,
            get_position='[Long, Lat]',
            radius=10000,
            get_elevation='population',
            elevation_scale=1,
            elevation_range=[0, 1000],
            get_color='[200, 30, 0, 160]',
            pickable=True,
            extruded=True,
            auto_highlight=True
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[Long, Lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=600,
        ),
    ],
))

with st.expander("Open to see the raw data"):
    st.subheader('Raw Data')
    st.write(data)
