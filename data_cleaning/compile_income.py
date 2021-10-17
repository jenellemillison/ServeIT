import pandas as pd

table = pd.read_html('https://txcip.org/tac/census/morecountyinfo.php?MORE=1013', skiprows=1, header=None)

uRate = table[0]
uRate.rename(columns={0:'County', 1:'Income'}, inplace=True)
uRate['Income'].replace('\$', '', regex=True, inplace=True)
uRate['Income'].replace(',', '', regex=True, inplace=True)
uRate.to_csv('../cleaned_data/median-income-data.csv', index=False)