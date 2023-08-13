# Import imports:
from imports import *
import mapping

# Get GeoDataFrame from get_gdf.py:
gdf = mapping.gdf
# Get stateFIPS_df from get_gdf.py:
stateFIPS_df = mapping.stateFIPS_df

'''
Use a scatterplot to demonstrate relationship between rates of PLWH
and average nursing home quality by county (including priority jurisdictions):
'''

gdf2 = gdf.copy()

jur = pd.read_csv('data/jurisdictions.csv')
for i in jur.index:
    state = jur['state'][i]
    if state == "Washington, D.C.": 
        jur['state'][i] = "DC"
        continue
    row = stateFIPS_df[stateFIPS_df['state'] == state]
    code = row['code'].iloc[0]
    jur['state'][i] = code

# Assign values to column describing whether county is a priority jurisdiction:
gdf2['priority'] = 'No'
for i in gdf2.index:
    for j in jur.index:
        if ((gdf2['State'][i] == jur['state'][j]) & 
            (gdf2['County'][i] == jur['county'][j])):
            gdf2['priority'][i] = 'Yes'

gdf2.to_csv("data/gdf2.csv")


# Group 1 - Modified by Group 3 - TM