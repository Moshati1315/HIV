import pandas as pd
import numpy as np
import mapping
import gdf2

'''AIDSVu Data Citation:
Sullivan PS, Woodyatt C, Koski C, Pembleton E, McGuinness P, Taussig J, Ricca A, Luisi N, Mokotoff E, Benbow N, Castel AD.
A data visualization and dissemination resource to support HIV prevention and care at the local level: analysis and uses of the AIDSVu Public Data Resource. 
Journal of medical Internet research. 2020;22(10):e23173.
'''
'''
Project Version 1 Citation:
https://github.com/ds5110/bioscience

See below for code snipits used to reproduce results

'''


''' Prevelence rates and SDOH for AIDS data downloaded from AIDSVu interactive dataset- no url
for csv available. urls below are from upload to project repo.'''

#   https://aidsvu.org/wp-content/uploads/2022/11/AIDSVu_County_SDOH_2020.xlsx

#sdoh_2020= "https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/AIDSVu_County_SDOH_2020.csv?token=GHSAT0AAAAAACDRJ3D7NJWB4P3CY7IX62VQZGJTMIA"
sdoh_2020_df = pd.read_csv('data/AIDSVu_County_SDOH_2020.csv') 

#data45= "https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county45_54.csv?token=GHSAT0AAAAAACDRJ3D6L62HESCKXBHRFCTQZGJTM4A"
hiv_45 = pd.read_csv('data/county45_54.csv').dropna()

#data55= "https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county55%2B.csv?token=GHSAT0AAAAAACDRJ3D7SRNYFI2DI32GIL3GZGJTNJQ"
hiv_55 = pd.read_csv('data/county55%2B.csv').dropna()

#all_data= "https://raw.githubusercontent.com/ds5110/project-summer-2023-moriarity-tim/main/data/county.csv?token=GHSAT0AAAAAACDRJ3D7AM27UXKLQJIPYDTCZGOXSGA"
all_df = pd.read_csv('data/county.csv')



# data for HIV rates for all ages
# updated datatype to numeric
all_df['Rates of Persons Living with HIV, 2020'] = pd.to_numeric(
all_df['Rates of Persons Living with HIV, 2020'], errors="coerce")


# HIV prevalance rates for 45+ (merged and adjusted for population)

# merge two age group dataframes, preserve data from both frames- outer merge
hiv_merge = pd.merge(hiv_45, hiv_55, left_on=['county', 'state'], right_on=[
                    'county', 'state'], how="outer")

# convert age columns to numeric
hiv_merge['Rates of Persons, aged 45 to 54, Living with HIV, 2020'] = pd.to_numeric(
hiv_merge['Rates of Persons, aged 45 to 54, Living with HIV, 2020'], errors="coerce")
hiv_merge['Rates of Persons, aged 55+, Living with HIV, 2020'] = pd.to_numeric(
hiv_merge['Rates of Persons, aged 55+, Living with HIV, 2020'], errors="coerce")

# filter df to eliminate any negative values (not reporting HIV rates-see AIDSVu for info on negative values). Set to zero to tabulate 45+ correctly
# for situations where one age group has reported rates, and the other doesn't
#"https://aidsvu.org/data-methods/data-methods-statecounty/" gives explanation of negative numbers
hiv_merge['Rates of Persons, aged 45 to 54, Living with HIV, 2020']=hiv_merge['Rates of Persons, aged 45 to 54, Living with HIV, 2020'].clip(lower=0)
hiv_merge['Rates of Persons, aged 55+, Living with HIV, 2020']=hiv_merge['Rates of Persons, aged 55+, Living with HIV, 2020'].clip(lower=0)

filtered_df = hiv_merge.copy()

# add two age columns toegther to get prevelance age 45 or greater. Use relative populations to scale correctly
#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/ used as reference for population volumes below

filtered_df["HIV aged 45+"] = (hiv_merge['Rates of Persons, aged 45 to 54, Living with HIV, 2020']*0.3) + (hiv_merge['Rates of Persons, aged 55+, Living with HIV, 2020']*0.7)
# change zero values added above back to nan to indicate areas with no reported HIV rates
filtered_df["HIV aged 45+"] = filtered_df["HIV aged 45+"].replace(0,np.nan)

# write combined and adjusted data to csv file for future use/use in notebook
filtered_df.to_csv('data/hiv_rates45+.csv')


# read data written above to use in v2
# v2gdf contains data on priority jurisdictions
v2gdf=pd.read_csv('data/gdf2.csv')

# merge v1 data for all ages with v2 data for ages 45+
# add state abbreviation to ages 45+ df
stateFIPS=pd.read_csv('data/v1stateFIPS_df.csv')
merge_filtered_df= filtered_df.copy()
merge_filtered_df['state'] = merge_filtered_df['state'].map(stateFIPS.set_index('state')['code'])

# outer merge, preserve v1 data, add v2 data where available, and vice versa
join_ages = pd.merge(v2gdf,merge_filtered_df,left_on=["County","State"],right_on=["county","state"],how="outer")
join_ages.to_csv('data/join_ages.csv')


'''
Group 1 & 2  

This file is a combination of the group 1 scatter3.py & scatter4.py as well as Group 2 get_data.py
Some code was removed and modified by Group 3

'''

