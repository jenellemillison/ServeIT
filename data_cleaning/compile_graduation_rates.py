import pandas as pd

educationFields = ['CNTYNAME', 'DIST_ALLR_GRAD']

educationData = pd.read_csv('../raw_data/texas-grad-rate-by-county.csv', skipinitialspace=True, usecols=educationFields)
educationData.to_csv('../cleaned_data/2020-graduation-rate-data.csv', index=False)
print(educationData)
