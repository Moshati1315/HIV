from imports import sns, sm, pd, np, plt

merged = pd.read_csv('data/group3data.csv')
value_vars_list = ['Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
                   'Percent Unemployed', 'Syphilis Rate', 'avg_nh_score',
                   'Percent Living with Severe Housing Cost Burden',
                   'Percent Living in Poverty', 'Percent High School Education',
                   'nh_count']
merged = merged[value_vars_list]
corr_matrix = merged.corr()

plt.figure(figsize=(14,10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap ')
plt.savefig('figs/heatmap.png')
plt.show()


# Group 3 - MS & TM