# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:35:13 2021

@author: JAMil
"""

import pandas as pd

COL_BUSINESS_DATA = ['State', 'State_Name', 'County', 'County_Name', 'NAICS', 'NAICS_Description', 'Enterprise Size', 'Firms', 'Establishments', 'Employment', 'Employment_Noise Flag', 'Annual_Payroll', 'Annual_Payroll_Noise_Flag']

serveIT_df = pd.DataFrame()

business_data = pd.read_csv('county_3digitnaics_2018.csv', header=0)#, columns=COL_BUSINESS_DATA)

rename = dict(zip(business_data.columns, COL_BUSINESS_DATA))
business_data.rename(columns = rename, inplace=True)
business_data_clean = business_data.iloc[1:]
business_data_clean = business_data_clean[business_data_clean.State_Name == 'Texas']

business_data_clean
print(business_data_clean)

business_data_clean[Annual_Payroll].astype(double)