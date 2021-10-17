import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table = pd.read_html('https://txcip.org/tac/census/morecountyinfo.php?MORE=1042', skiprows=1, header=None)

uRate = table[0]

YEARS = ['2016', '2017', '2018', '2019']
for year in YEARS:
    uRate.replace('%', '', regex=True, inplace=True)
    uRate[1].astype(float)
    uRate[2].astype(float)
    uRate[3].astype(float)
uRate.to_csv('../cleaned_data/2016-to-2020-unemployment-data.csv', index=False, header=False)

