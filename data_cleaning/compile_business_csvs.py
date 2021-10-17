# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:35:13 2021

@author: JAMil
"""

import pandas as pd

COL_BUSINESS_DATA = ['State', 'State_Name', 'County_Num', 'County', 'NAICS', 'NAICS_Description', 'Enterprise_Size', 'Firms', 'Establishments', 'Employment', 'Employment_Noise_Flag', 'Annual_Payroll', 'Annual_Payroll_Noise_Flag']
SERVICE_INDUSTRIES = ['Food Services and Drinking Places', 'Accommodation and Food Services', 'Accommodation', 'Food and Beverage Stores', 'Retail Trade', 'General Merchandise Stores', 'Clothing and Clothing Accessories Stores']
ENTERPRISE = ['2: <20 employees', '3: 20-99 employees']
TOTAL = ['1: Total']

serveIT_df = pd.DataFrame()

business_data = pd.read_csv('../raw_data/county_3digitnaics_2018.csv', header=0)#, columns=COL_BUSINESS_DATA)

#name columns properly and dispose of first column (a number that indicates state) because we will use state name
rename = dict(zip(business_data.columns, COL_BUSINESS_DATA))
business_data.rename(columns = rename, inplace=True)
business_data_clean = business_data.drop(['State', 'County_Num', 'NAICS', 'Employment_Noise_Flag', 'Annual_Payroll_Noise_Flag'], axis=1)
business_data_clean = business_data_clean[business_data_clean.State_Name == 'Texas']

#get rid of commas
for col in ['Annual_Payroll', 'Employment', 'Establishments', 'Firms']:
    business_data_clean[col].replace(',', '', regex=True, inplace=True)
#Annual_Payroll column into floats
business_data_clean['Annual_Payroll'].astype(float)
#Employment column into ints
business_data_clean['Employment'].astype(int)
#Establishment column into ints
business_data_clean['Establishments'].astype(int)
#Firms column into ints
business_data_clean['Firms'].astype(int)
#dont need the state_name anymore because all are TX
business_data_clean.drop('State_Name', axis=1, inplace=True)

#extract out county totals
business_data_clean_total = business_data_clean[business_data_clean['NAICS_Description'] == 'Total']
business_data_clean_total = business_data_clean_total[business_data_clean_total['Enterprise_Size'].isin(TOTAL)]
business_data_clean_total = business_data_clean_total.drop('Enterprise_Size', axis=1)

#filter out everything that is not service industry
business_data_clean = business_data_clean[business_data_clean['NAICS_Description'].isin(SERVICE_INDUSTRIES)]
#filter out big business and combine stats for everything under 100 employees
business_data_clean = business_data_clean[business_data_clean['Enterprise_Size'].isin(ENTERPRISE)]
aggregation_functions = {'Firms':'sum', 'Establishments':'sum', 'Employment':'sum', 'Annual_Payroll':'sum'}
business_data_clean_agg = business_data_clean.groupby(['County', 'NAICS_Description'], as_index=False).aggregate(aggregation_functions)

#combine and sort small businesses and total
business_data_clean_final = business_data_clean_agg.append(business_data_clean_total)
business_data_clean_final.sort_values(by=["County"], inplace = True)

business_data_clean_final.to_csv('../cleaned_data/2019_tx_county_final_business_data.csv', index=False)