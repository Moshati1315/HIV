### Take from Group 1

url: https://github.com/ds5110/bioscience

### Taken from Group 2
Direct URL for the repo: https://github.com/ds5110/projects-spring-2023-ahaskell83
## Data Pipeline:

For the detailed code used in the pipeline described below, refer to get_data.py

We began by extracting the data used in version one of the project.<sup>1</sup> Below is the code used within a cloned copy of the v1 repo to generate the data for mapping (gdf, stateFIPS) and for the scatter plots (scat3, scat4) from that version. 
As shown, the data was written to files. Those files were then transferred to the v2 repo and uploaded.

```
# Write general v1 data for use in v2.
gdf = get_gdf.gdf
gdf.to_json()
gdf.to_file("data/v1gdf.GeoJSON",driver='GeoJSON')

stateFIPS_df = get_gdf.stateFIPS_df
stateFIPS_df.to_csv("data/v1stateFIPS_df.csv")

# Write v1 data used for scatter plots for v2 updates.
scat3 = scatter3.gdf2
#scat3.to_csv("data/scat3.csv")

scat4 = scatter4.gdf2
#scat4.to_csv("data/scat4.csv")'''
```

Next we gathered data for HIV prevalence for all ages (used for feasibility study) and for the 45+ age group. We were able to retrieve data for all ages, ages 45-54, and 55+ from AIDSVu.org.<sup>2</sup>  AIDSVu.org does not provide a url link to their data, so copies were downloaded to the repo. The data is provided in the age groups as specified above, so we then had to combine the 45-54 age group, and the 55+ age group into one.

To do that we read the data from both age groups into dataframes and merged those dataframes on county and state- keeping the prevalence rates separated initially. We included data which had a recorded prevalence rate for both age ranges, and data which had a recorded prevalence rate for only one or the other age range. We converted the prevalence data to numeric data within the dataframe.

AIDSVu represents suppressed and/or missing data as -1, -2, -4, or -9. This does not represent actual numeric data, but translates to a reason the data was omitted, so we excluded any prevalence data marked with a negative number. 

Finally, we combined the HIV prevalence rates for both age groups into one prevalence rate for ages 45+ using relative populations to scale correctly.<sup>3</sup>  The final data for the 45+ age group was saved to the repo in the file hiv_rates45+.csv.

Additionally, we pulled county level data regarding census details pertinent to HIV rates from AIDSVu.org and saved that to the repo as AIDSVu_County_SDOH_2020.csv.

We used the data saved to the repo in age_filter.ipynb to provide the interactive mapping and filtering requested by the stakeholder.

The following may be used to generate the age_filter notebook. The data within the repo will need to be cloned for the notebook to function correctly. Per the request of our stakeholder, this repo has been kept as private, so data may only be read locally.

```
Make notebook
```

In the second block of code in the notebook v1gdf.GeoJSON, v1stateFIPS_df.csv, hiv_rates45+.csv, AIDSVu_County_SDOH_2020.csv, and data regarding priority jurisdiction used in v1 (url provided) were read into separate dataframes. 

The ages 45+ data was updated to include regions, priority jurisdictions, and state codes (merging with priority jurisdiction data, and mapped to values with stateFIPS and regions).
 
The ages 45+ data was merged with v1gdf into a single dataframe- gdf. The data from AIDSVu_County_SDOH_2020 was then added to this dataframe. All columns were renamed to be easily understood when filtering maps. Any counties that did not have a reported HIV prevalence rate for all ages or ages 45+ was dropped. Counties that had data for one age group but not the other were kept. This final dataframe was used for all the interactive mapping shown in the notebook.

## Data explaination  

url: https://aidsvu.org/data-methods/data-methods-statecounty/

Dataset Variables

The downloadable datasets may have suppressed/missing values for several reasons. Suppressed and/or missing data are represented as -1, -2, -4, or -9 in the dataset and indicate the following:

-1: Data are not shown to protect privacy because a small number of cases and/or a small population size for reasons listed in the Data Suppression and Rate Stability section.
-2: Data were not released to AIDSVu because the state health department, per its HIV data re-release agreement with CDC, requested not to release data to AIDSVu below a certain population threshold. The data re-release agreement was updated last year, which is why the data for this year may look different than last year.
-4: Data are not available at county-level for these counties as this time.

-9: Data are missing.

The downloadable datasets include a rate stability variable for each indicator. As is standard in the display of health statistics, rates generated from a numerator less than 12 are considered unreliable and should be interpreted with caution.

Y: Reliable rates (i.e. those generated with a numerator of 12 or greater)

N: Unreliable rates (i.e. those generated with a numerator less than 12)

Rate stability for suppressed rates is listed as -9 for HIV data and -1 for PrEP data.

Please see the “Data Suppression and Rate Stability” section of the Data Methods above for specific information regarding the suppression rules and rate stability criteria.
