from imports import *


# Import stateFIPS dataset
stateFIPS_df = pd.read_csv('data/stateFIPS.csv', usecols = ['state', 'code', 'fips', 'region'])
# Get state FIPS codes as strings:
stateFIPS_df['STATEFP'] = stateFIPS_df['fips'].astype(str)

# Add '0' before single-digit fips nums (to make all 2-digit codes):
for index in stateFIPS_df.index:
    # get FIPS code:
    fips = stateFIPS_df['STATEFP'][index]
    # If 1-digit, add a 0 prefix:
    if len(fips) == 1:
        fips = '0' + fips
    # Reassign value:
    stateFIPS_df['STATEFP'][index] = fips

stateFIPS_df.to_csv("data/v1stateFIPS_df.csv")

#HIV data
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
hiv_merge = pd.merge(hiv_45, hiv_55, left_on=['county', 'state'], right_on=['county', 'state'], how="outer")
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
filtered_df = hiv_merge
# add two age columns toegther to get prevelance age 45 or greater. Use relative populations to scale correctly
#https://www.statista.com/statistics/241488/population-of-the-us-by-sex-and-age/ used as reference for population volumes below
filtered_df["HIV aged 45+"] = (hiv_merge['Rates of Persons, aged 45 to 54, Living with HIV, 2020']*0.3) + (hiv_merge['Rates of Persons, aged 55+, Living with HIV, 2020']*0.7)
# change zero values added above back to nan to indicate areas with no reported HIV rates
filtered_df["HIV aged 45+"] = filtered_df["HIV aged 45+"].replace(0,np.nan)
# write combined and adjusted data to csv file for future use/use in notebook
######filtered_df.to_csv('data/hiv_rates45+.csv')
# merge v1 data for all ages with v2 data for ages 45+
# add state abbreviation to ages 45+ df

stateFIPS=pd.read_csv('data/v1stateFIPS_df.csv')
merge_filtered_df= filtered_df
merge_filtered_df['state'] = merge_filtered_df['state'].map(stateFIPS.set_index('state')['code'])
# outer merge, preserve v1 data, add v2 data where available, and vice versa
aidsvu_file_df = pd.read_csv('data/AIDSVu_County_SDOH_2020.csv')
county_file_df = pd.read_csv('data/county.csv')
aidsvu_file_df['County'] = aidsvu_file_df['County'].str.replace(' County', '')

merged_temp = pd.concat([aidsvu_file_df, county_file_df], axis=1)
merged = pd.concat([merged_temp, merge_filtered_df], axis=1)
county_url = "data/county.csv"
provider_url = "data/NH_ProviderInfo_May2023.csv"
states_url = 'data/stateFIPS.csv'
stateFIPS_url = 'data/stateFIPS.csv'
# Import the HIV Rates dataset, drop NAs:
county_df = pd.read_csv(county_url).dropna()
# Rename features:
df2 = county_df
df2 = df2.rename(columns={'county': 'County', 'state': 'State','Rates of Persons Living with HIV, 2020': 'Rate'})
# Drop undefined rows (Rate='undefined') as well as all negative values (Rates containing '-'):
df2 = df2[df2.Rate.str.isnumeric()]
# Convert rates from string to numeric value:
df2['Rate'] = pd.to_numeric(df2['Rate'])
# Import the provider data set. Only want state, county, and rating features:
provider_df = pd.read_csv(provider_url, sep=",", encoding='cp1252')
 #usecols = ['Provider County Name', 'Provider State', 'Overall Rating']).dropna()
# Rename features:
provider_df = provider_df.rename(columns={'Provider County Name': 'County', 'Provider State': 'State', 'Overall Rating': 'Rating'})
# Get average NH score by county by state:
group = provider_df.groupby(['County', 'State'])
county_nh_scores = group['Rating'].mean()
# Get number of NHs per county by state:
county_nh_count = group.size()
states_df = pd.read_csv(states_url, usecols = ['state', 'code'])
# Convert the 'state' column in df2 (county.csv) from full name to state code:
df2['State'] = df2['State'].map(states_df.set_index('state')['code'])
#Merge dataframes into one:
scores_index = county_nh_scores.index.to_frame(index = False)
# Get dataframe containing average nursing home scores by county:
scores_df = pd.DataFrame(data=county_nh_scores.values, columns=['avg_nh_score'])
# Get dataframe containing total nursing home counts by county:
counts_df = pd.DataFrame(data=county_nh_count.values, columns=['nh_count'])
# Merge dataframes:
df0 = pd.merge(scores_df, counts_df, left_index=True, right_index=True)
# Generate dataframe with avg NH score, county, state:
df00 = pd.merge(df0, scores_index, left_index=True, right_index=True)
# Merge with dataframe containing HIV rates by county/state:
cols = ['State', 'County']
dfX = df00.merge(df2, on=cols)

#Final DataFrame
merged = pd.concat([merged, dfX], axis=1)
merged = merged.dropna()
# Note that we lost a bunch of rows after this merge ^
# Because we dropped those rows without usable HIV data.
merged = merged[merged['Rates of Persons Living with HIV, 2020'] != 'undefined']
merged['Rates of Persons Living with HIV, 2020'] = pd.to_numeric(merged['Rates of Persons Living with HIV, 2020'], errors='coerce')
merged['nh_count'] = merged['nh_count'].astype(int)
#merged = merged[(merged >= 0).all(axis=1)]
# new code 8/11
#jur.to_csv('data/jur.csv')
# Saving file in data folder
merged = merged.rename(columns={'Rates of Persons, aged 55+, Living with HIV, 2020': 'hiv55+'})
merged = merged[merged['hiv55+'] != 'undefined']
#merged['hiv55+'] = pd.to_numeric(merged['hiv55+'], errors='coerce')
merged = merged.dropna()
# CSV of FINAL Dataframe
merged.to_csv('data/group3data.csv')
