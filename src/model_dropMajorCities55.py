from imports import *

merged = pd.read_csv('data/group3data.csv')
merged = merged[~merged['nh_count'].isin([101, 81, 205, 375, 65, 70, 73])]
merged = merged.dropna()
merged = merged.rename(columns={'Rates of Persons, aged 55+, Living with HIV, 2020': 'hiv55+'})
merged = merged[merged['hiv55+'] != 'undefined']


x = merged[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate','avg_nh_score']]

y = merged['hiv55+']



lg = LinearRegression()
pipeline = Pipeline(steps=[('m',lg)])

n_scores = cross_val_score(pipeline, x, y, cv=KFold(n_splits=5, shuffle=True, random_state=1))


print("\n\nLinear Regression - 55+ Population - after major cities drop\n")

results = sm.OLS(y,x, hasconst=True).fit()
print(results.summary())  

print('\n Cross-validated R^2:', np.mean(n_scores))

lasso = LassoCV(cv=KFold(n_splits=10, shuffle=True, random_state=1))


pipeline = Pipeline(steps=[('m',lasso)])


pipeline.fit(x, y)


lasso_coef = pd.Series(pipeline.named_steps['m'].coef_, index = x.columns)

print("\nRanked features by Lasso:\n")
print(lasso_coef.abs().sort_values(ascending=False))
print('\n Unfortunately Average Nursing Home Score is not statistically significant\n along with being ranked last using Lasso feature selection.')
print('\n Not overly surprising since this model looks at HIV rates for all ages,\n and nursing home score is likely only relevant to an older age group.\nRun make m55 to look at just an older age group.')



# Group 3 - MS & TM