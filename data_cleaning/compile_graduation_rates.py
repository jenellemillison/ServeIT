import pandas as pd

educationFields = ['CNTYNAME', 'DIST_ALLR_GRAD']
educationData = pd.read_csv('../raw_data/texas-grad-rate-by-county.csv', skipinitialspace=True, usecols=educationFields)
educationData.rename(columns={'CNTYNAME':'County'}, inplace=True)
educationData['County'].replace(' County', '', regex=True, inplace=True)
aggregation_functions = {'DIST_ALLR_GRAD': 'mean'}
educationData = educationData.groupby(['County'], as_index=False).aggregate(aggregation_functions)


educationData.to_csv('../cleaned_data/2020-graduation-rate-data.csv', index=False)
