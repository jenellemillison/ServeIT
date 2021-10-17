# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:06:32 2021

@author: JAMil
"""

import pandas as pd

age_data = pd.read_csv('../raw_data/cc-est2019-agesex-48.csv', header=0)
age_data['CTYNAME'].replace(' County', '', regex=True, inplace=True)
age_data = age_data[age_data['YEAR'] == 11]
age_data_cleaned = age_data.iloc[:, -3:]
age_data_cleaned.insert(0, 'County', pd.Series(age_data['CTYNAME']))

age_data_cleaned.to_csv('../cleaned_data/2020_tx_county_age_data.csv', index=False)