# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 06:58:50 2021

@author: JAMil
"""

import pandas as pd

long_lats = pd.read_csv('../raw_data/Texas_Counties_Centroid_Map.csv')

print(long_lats)

long_lats = long_lats.iloc[:, :3]
long_lats.rename(columns={'X (Lat)':'Lat', 'Y (Long)':'Long', 'CNTY_NM':'County'}, inplace=True)
print(long_lats)
long_lats.to_csv('../cleaned_data/long_lats.csv', index=False)