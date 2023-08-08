from imports import *

aidsvu_file = 'data/AIDSVu_County_SDOH_2020.csv'
county_file = 'data/county.csv'
join_ages_file_path = 'data/join_ages.csv'

aidsvu_file_df = pd.read_csv(aidsvu_file)
county_file_df = pd.read_csv(county_file)
join_ages_df = pd.read_csv(join_ages_file_path)

county_file_df = county_file_df.rename(columns={"county": "County"})
aidsvu_file_df['County'] = aidsvu_file_df['County'].str.replace(' County', '')

merged_temp = pd.merge(aidsvu_file_df, county_file_df, on='County', how='left')
merged2 = pd.merge(merged_temp, join_ages_df, on='County', how='left')

columns_to_drop = ['GEO ID', 'State Abbreviation', 'County', 'State_x', 'nh_count', 'State_y', 'state_x', 'priority',	'county', 	'state_y', 'Region', 'GEOID',	'LSAD',	'ALAND',	'AWATER', 'geometry', 'Unnamed: 0.1', 	'Unnamed: 0', 	'STATEFP', 	'COUNTYFP',	'COUNTYNS',	'AFFGEOID', 'hiv_rate', 'Rates of Persons, aged 45 to 54, Living with HIV, 2020', 'HIV aged 45+' ]
merged2 = merged2.drop(columns=columns_to_drop, errors='ignore')

merged2 = merged2.dropna()
merged2 = merged2.rename(columns={'Rates of Persons, aged 55+, Living with HIV, 2020': 'hiv55+'})
merged2 = merged2[merged2['hiv55+'] != 'undefined']
merged2['hiv55+'] = pd.to_numeric(merged2['hiv55+'], errors='coerce')

x = merged2[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate','avg_nh_score']]

y = merged2['hiv55+']


# Making Histogram
features = x.columns.to_list()
melted_data = merged2[features].melt()

g = sns.FacetGrid(melted_data, col="variable", col_wrap=3, sharex=False, height=4)
g.map(sns.histplot, "value", bins=30, kde=False)
g.set_axis_labels("Value", "Counts")

# Set the x-axis label for each facet to its corresponding feature
for ax, title in zip(g.axes.flat, features):
    ax.set_xlabel(title)
    ax.set_title('')  # Clear the title

# Rotate x-axis labels for "Median Household Income" plot
g.set_xticklabels(rotation=30)

g.tight_layout()
plt.savefig('figs/55+population.png')
plt.show()


lg = LinearRegression()
pipeline = Pipeline(steps=[('m',lg)])

n_scores = cross_val_score(pipeline, x, y, cv=KFold(n_splits=10, shuffle=True, random_state=1))
x = x.dropna()
y = y.loc[x.index]

print("\n\nLinear Regression - 55+ Population\n")

results = sm.OLS(y,x, hasconst=True).fit()
print(results.summary())  

print('Cross-validated R^2:', np.mean(n_scores))

lasso = LassoCV(cv=KFold(n_splits=10, shuffle=True, random_state=1))

pipeline = Pipeline(steps=[('m',lasso)])


pipeline.fit(x, y)

lasso_coef = pd.Series(pipeline.named_steps['m'].coef_, index = x.columns)


print("Ranked features by Lasso:")
print(lasso_coef.abs().sort_values(ascending=False))
print('\n Unfortunately Average Nursing Home Score is at the bottom of the list. Again.')
