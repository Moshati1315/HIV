from imports import *
'''
aidsvu_file = 'data/AIDSVu_County_SDOH_2020.csv'
county_file = 'data/county.csv'
join_ages_file_path = 'data/join_ages.csv'

aidsvu_file_df = pd.read_csv(aidsvu_file)
county_file_df = pd.read_csv(county_file)
join_ages_df = pd.read_csv(join_ages_file_path)

county_file_df = county_file_df.rename(columns={"county": "County"})
aidsvu_file_df['County'] = aidsvu_file_df['County'].str.replace(' County', '')

'''
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

merged = merged.rename(columns={'Rates of Persons, aged 55+, Living with HIV, 2020': 'hiv55+'})
merged = merged[merged['hiv55+'] != 'undefined']
#merged['hiv55+'] = pd.to_numeric(merged['hiv55+'], errors='coerce')
merged = merged.dropna()
#merged['hiv55+'] = merged['hiv55+'].astype(int)


x = merged[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate','avg_nh_score']]

y = merged['hiv55+']


# Making Histogram
features = x.columns.to_list()
melted_data = merged[features].melt()

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
#x = x.dropna()
#y = y.loc[x.index]

print("\n\nLinear Regression - 55+ Population\n")

results = sm.OLS(y,x, hasconst=True).fit()
print(results.summary())  

print('\nCross-validated R^2:', np.mean(n_scores))

lasso = LassoCV(cv=KFold(n_splits=10, shuffle=True, random_state=1))

pipeline = Pipeline(steps=[('m',lasso)])


pipeline.fit(x, y)

lasso_coef = pd.Series(pipeline.named_steps['m'].coef_, index = x.columns)


print("\nRanked features by Lasso:\n")
print(lasso_coef.abs().sort_values(ascending=False))
#print('\n Unfortunately Average Nursing Home Score is at the bottom of the list. Again.')
