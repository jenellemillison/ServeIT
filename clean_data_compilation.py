# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 01:20:17 2021
@author: JAMil
"""

import pandas as pd


dfs = []
#horrible practice... I know... I know, but it's a hackathon ¯\_(ツ)_/¯
dfs.append(pd.read_csv('./cleaned_data/2016-to-2020-unemployment-data.csv'))
#dfs.append(pd.read_csv('./cleaned_data/2019_tx_county_final_business_data.csv'))
dfs.append(pd.read_csv('./cleaned_data/total_payroll.csv'))
dfs.append(pd.read_csv('./cleaned_data/2020_tx_county_age_data.csv'))
dfs.append(pd.read_csv('./cleaned_data/2020-graduation-rate-data.csv'))
dfs.append(pd.read_csv('./cleaned_data/median-income-data.csv'))
dfs.append(pd.read_csv('./cleaned_data/rural-counties.csv'))
dfs.append(pd.read_csv('./cleaned_data/long_lats.csv'))
dfs.append(pd.read_csv('./cleaned_data/2020_population.csv'))

final_dataset = pd.DataFrame(columns=['County'])
for i in range(len(dfs)):
    final_dataset = final_dataset.merge(dfs[i], on='County', how='outer')
final_dataset.fillna(0, inplace=True)
final_dataset.to_csv('small_business_service_dataset.csv', index=False)