# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 01:20:17 2021

@author: JAMil
"""

import pandas as pd

#horrible practice... I know... I know, but it's a hackathon ¯\_(ツ)_/¯
unemp = pd.read_csv('./cleaned_data/2016-to-2020-unemployment-data.csv')
business = pd.read_csv('./cleaned_data/2019_tx_county_final_business_data.csv')
age = pd.read_csv('./cleaned_data/2020_tx_county_age_data.csv')
grads = pd.read_csv('./cleaned_data/2020-graduation-rate-data.csv')
income = pd.read_csv('./cleaned_data/median-income-data.csv')

'''
FILE_DATA = ['unemployment', 'business', 'graduation', 'age', 'income']
dfs = []

for file in [f for f in listdir('./cleaned_data') if isfile(join(mypath,f))]:
    dfs.append(pd.read_csv(file))
#can't use iloc now because order here is unpredictable
'''

