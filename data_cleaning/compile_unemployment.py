import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table = pd.read_html('https://txcip.org/tac/census/morecountyinfo.php?MORE=1042', skiprows=1, header=None)

uRate = table[0]

header = uRate.iloc[0:1, :]
uRate = uRate[1:]
uRate.rename(columns={0:'County', 1:'Unemp_2016', 2:'Unemp_2017', 3:'Unemp_2018', 4:'Unemp_2019'}, inplace=True)

YEARS = ['Unemp_2016', 'Unemp_2017', 'Unemp_2018', 'Unemp_2019']
for year in YEARS:
    uRate.replace('%', '', regex=True, inplace=True)
    uRate[year].astype(float)
    uRate[year].astype(float)
    uRate[year].astype(float)
    
print(uRate)


uRate.to_csv('../cleaned_data/2016-to-2020-unemployment-data.csv', index=False)

