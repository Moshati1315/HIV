from imports import *
import seaborn as sns
import matplotlib.pyplot as plt

aidsvu_file = 'data/AIDSVu_County_SDOH_2020.csv'
county_file = 'data/county.csv'
join_ages_file_path = 'data/join_ages.csv'

aidsvu_file_df = pd.read_csv(aidsvu_file)
county_file_df = pd.read_csv(county_file)
join_ages_df = pd.read_csv(join_ages_file_path)

county_file_df = county_file_df.rename(columns={"county": "County"})
aidsvu_file_df['County'] = aidsvu_file_df['County'].str.replace(' County', '')

merged_temp = pd.merge(aidsvu_file_df, county_file_df, on='County', how='left')
merged = pd.merge(merged_temp, join_ages_df, on='County', how='left')

columns_to_drop = ['GEO ID', 'State Abbreviation', 'County', 'State_x', 'nh_count', 'State_y', 'state_x', 'priority',	'county', 	'state_y', 'Region', 'GEOID',	'LSAD',	'ALAND',	'AWATER', 'geometry', 'Unnamed: 0.1', 	'Unnamed: 0', 	'STATEFP', 	'COUNTYFP',	'COUNTYNS',	'AFFGEOID', 'hiv_rate', 'Rates of Persons, aged 45 to 54, Living with HIV, 2020','Rates of Persons, aged 55+, Living with HIV, 2020', 'HIV aged 45+' ]
merged = merged.drop(columns=columns_to_drop, errors='ignore')

merged = merged.dropna()
merged = merged[merged['Rates of Persons Living with HIV, 2020'] != 'undefined']
merged['Rates of Persons Living with HIV, 2020'] = pd.to_numeric(merged['Rates of Persons Living with HIV, 2020'], errors='coerce')

merged.head()

x = merged[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate', 'avg_nh_score']]

y = merged['Rates of Persons Living with HIV, 2020']

long_df = pd.melt(merged, id_vars='Rates of Persons Living with HIV, 2020',
                  value_vars=['Percent Living with Severe Housing Cost Burden', 'Percent Living in Poverty', 'Syphilis Rate'])


g = sns.FacetGrid(long_df, col='variable', height=4, aspect=1, sharex=False, sharey=False, col_wrap=3)
g = g.map(sns.regplot, 'value', 'Rates of Persons Living with HIV, 2020', scatter_kws={'alpha':0.4}, line_kws={'color':'red'})

g.set_axis_labels('', 'Rates of Persons Living with HIV, 2020')


axes = g.axes.flatten()
axes[0].set_xlabel('Percent Living with Severe Housing Cost Burden')
axes[1].set_xlabel('Percent Living in Poverty')
axes[2].set_xlabel('Syphilis Rate')

g.set_titles(col_template="{col_name}")

plt.show()
'''

import pandas as pd

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
merged2 = merged.drop(columns=columns_to_drop, errors='ignore')

merged2 = merged.dropna()


from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np

x = merged2[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate','avg_nh_score']]

y = merged2['Rates of Persons, aged 55+, Living with HIV, 2020']

lg = LinearRegression()
pipeline = Pipeline(steps=[('m',lg)])

n_scores = cross_val_score(pipeline, x, y, cv=KFold(n_splits=10, shuffle=True, random_state=1))
x = x.dropna()
y = y.loc[x.index]
print('Cross-validated R^2:', np.mean(n_scores))

from sklearn.linear_model import LassoCV


lasso = LassoCV(cv=KFold(n_splits=10, shuffle=True, random_state=1))

pipeline = Pipeline(steps=[('m',lasso)])


pipeline.fit(x, y)

lasso_coef = pd.Series(pipeline.named_steps['m'].coef_, index = x.columns)


print("Top 3 features selected by Lasso:")
print(lasso_coef.abs().sort_values(ascending=False).head(3).index.tolist())

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


long_df = pd.melt(merged2, id_vars='Rates of Persons, aged 55+, Living with HIV, 2020',
                  value_vars=['Syphilis Rate', 'Median Household Income', 'Percent Living in Poverty'])


g = sns.FacetGrid(long_df, col='variable', height=4, aspect=1, sharex=False, sharey=False, col_wrap=3)
g = g.map(sns.regplot, 'value', 'Rates of Persons, aged 55+, Living with HIV, 2020', scatter_kws={'alpha':0.4}, line_kws={'color':'red'})

g.set_axis_labels('', 'Rates of Persons, aged 55+, Living with HIV, 2020')


axes = g.axes.flatten()
axes[0].set_xlabel('Syphilis Rate')
axes[1].set_xlabel('Median Household Income')
axes[2].set_xlabel('Percent Living in Poverty')


for ax in g.axes.flat:
    for label in ax.get_xticklabels():
        label.set_rotation(30)

g.set_titles(col_template="{col_name}")

plt.tight_layout()
plt.show()
'''