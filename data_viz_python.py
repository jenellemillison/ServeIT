# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 23:11:32 2021

@author: JAMil
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



orig_dataset = pd.read_csv('./small_business_service_dataset.csv')

selected_cols = ['Unemp_2020', 'Firms', 'Establishments', 'MEDIAN_AGE_TOT', 'DIST_ALLR_GRAD', 'Income']
corr_coefs = {}
for col in selected_cols:
    orig_dataset[col].astype(float)
    print(type(orig_dataset[col][0]))

for col_name in selected_cols:
  corr_coefs[col_name] = np.corrcoef((orig_dataset[col_name]).astype(int), orig_dataset['Annual_Payroll'])
for corr_coef in corr_coefs:
  print(corr_coef, corr_coefs[corr_coef][0][1])
