from imports import *

merged = pd.read_csv('data/group3data.csv')
merged = merged[~merged['nh_count'].isin([101, 81, 205, 375, 65, 70, 73])]
merged = merged.dropna()
merged = merged[merged['Rates of Persons Living with HIV, 2020'] != 'undefined']
merged['Rates of Persons Living with HIV, 2020'] = pd.to_numeric(merged['Rates of Persons Living with HIV, 2020'], errors='coerce')

x = merged[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate', 'avg_nh_score']]

y = merged['Rates of Persons Living with HIV, 2020']


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
print('\n\nUnfortunately avg_nh_score is the 7th feature selected.\n')

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
print('\n\nUnfortunately avg_nh_score is the 7th feature selected. Again.')



# Group 3 - TM