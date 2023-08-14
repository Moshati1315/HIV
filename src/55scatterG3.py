from imports import sns, plt, pd


merged = pd.read_csv('data/group3data.csv')

value_vars_list = ['Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
                   'Percent Unemployed', 'Syphilis Rate', 'avg_nh_score',
                   'Percent Living with Severe Housing Cost Burden',
                   'Percent Living in Poverty', 'Percent High School Education',
                   'nh_count']

data = merged.melt(id_vars=['hiv55+'], value_vars=value_vars_list)


g = sns.FacetGrid(data, col="variable", col_wrap=3, sharex=False, sharey=False, height=4)
g = (g.map(plt.scatter, "value", "hiv55+", edgecolor="w")
      .set_titles("{col_name} vs. HIV Rates")
      .set_axis_labels("Value", "Rates of Persons Living with HIV 55+, 2020"))

plt.subplots_adjust(top=0.9)
g.fig.suptitle('Scatter Plots of Predictors vs. Rates of Persons Living with HIV over 55 years old, 2020')

plt.savefig('figs/FeatureScatter55.png')
plt.savefig('docs/figs/FeatureScatter55.png')
plt.show()

# Group 3 - MS & TM