# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 23:11:32 2021

@author: JAMil
"""

import pandas as pd
import numpy as np

orig_dataset = pd.read_csv('./small_business_service_dataset.csv')

for col_name in orig_dataset.columns:
  corr_coefs[col_name] = abs(np.corrcoef(orig_dataset[col_name], orig_dataset['']))
for corr_coef in corr_coefs:
  print(corr_coef, corr_coefs[corr_coef][0][1])
data_np = data[selected_cols].to_numpy()

scatterplotmatrix(data_np, names=selected_cols, alpha=0.5)
plt.show()
