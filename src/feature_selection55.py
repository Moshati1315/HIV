from imports import *
'''
aidsvu_file_df = pd.read_csv('data/AIDSVu_County_SDOH_2020.csv')
county_file_df = pd.read_csv('data/county.csv')
join_ages_df = pd.read_csv('data/join_ages.csv')

county_file_df = county_file_df.rename(columns={"county": "County"})
aidsvu_file_df['County'] = aidsvu_file_df['County'].str.replace(' County', '')

merged_temp = pd.concat([aidsvu_file_df, county_file_df], axis=1)
merged = pd.concat([merged_temp, join_ages_df], axis=1)
'''

merged = pd.read_csv('data/group3data.csv')

merged = merged.dropna()
merged = merged[merged['Rates of Persons Living with HIV, 2020'] != 'undefined']
merged['Rates of Persons Living with HIV, 2020'] = pd.to_numeric(merged['Rates of Persons Living with HIV, 2020'], errors='coerce')

merged2 = merged.dropna()
merged2 = merged2.rename(columns={'Rates of Persons, aged 55+, Living with HIV, 2020':'hiv55+'})
merged2 = merged2[merged2['hiv55+'] != 'undefined']
merged2['hiv55+'] = pd.to_numeric(merged2['hiv55+'], errors='coerce')

x = merged2[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate', 'avg_nh_score']]

y = merged2['hiv55+']


# Forward Feature Selection
feature_names = np.array(x.columns)
ridge = RidgeCV()
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=1, direction="forward").fit(x, y)
print('\nFirst Feature Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(x, y)
print('\nFirst 2 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=3, direction="forward").fit(x, y)
print('\nFirst 3 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=4, direction="forward").fit(x, y)
print('\nFirst 4 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=5, direction="forward").fit(x, y)
print('\nFirst 5 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=6, direction="forward").fit(x, y)
print('\nFirst 6 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=7, direction="forward").fit(x, y)
print('\nFirst 7 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=8, direction="forward").fit(x, y)
print('\nFirst 8 Features Selected by Forward Selection: \n\n',feature_names[sfs_forward.get_support()])
#print('\n\nUnfortunately avg_nh_score is the 7th feature selected.\n')

# Backward Feature Selection
feature_names = np.array(x.columns)
ridge = RidgeCV()
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=1, direction="backward").fit(x, y)
print('\nFirst Feature Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(x, y)
print('\nFirst 2 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=3, direction="backward").fit(x, y)
print('\nFirst 3 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=4, direction="backward").fit(x, y)
print('\nFirst 4 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=5, direction="backward").fit(x, y)
print('\nFirst 5 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=6, direction="backward").fit(x, y)
print('\nFirst 6 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=7, direction="backward").fit(x, y)
print('\nFirst 7 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=8, direction="backward").fit(x, y)
print('\nFirst 8 Features Selected by Backward Selection: \n\n',feature_names[sfs_forward.get_support()])
#print('\n\nUnfortunately avg_nh_score is the 7th feature selected. Again.')


# Group 3 - TM