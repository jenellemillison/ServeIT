# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 07:28:51 2021

@author: JAMil
"""

import pandas as pd
#import numpy as np
df = pd.read_csv("../raw_data/2019_txpopest_county.csv")
df = df.drop(['pct_chg_10_19','cqr_census_2010_count','july1_2019_pop_est','num_chg_10_20','num_chg_10_19','FIPS'],axis=1)

df.rename(columns={'county':'County', 'jan1_2020_pop_est':'population'},inplace=True)
df.to_csv('../cleaned_data/2020_population.csv', index=False)
