from imports import pd, sns, plt

merged = pd.read_csv('data/group3data.csv')

cols_to_plot = ['Percent Living in Poverty', 'Percent High School Education',
                'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
                'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
                'Syphilis Rate', 'Rates of Persons Living with HIV, 2020',
                'avg_nh_score', 'nh_count']

plt.figure(figsize=(15,10))

for idx, col in enumerate(cols_to_plot, start=1):
    plt.subplot(3, 4, idx)
    sns.boxplot(y=col, data=merged)
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
plt.savefig('figs/FeatureBox.png')
plt.savefig('docs/figs/FeatureBox.png')
plt.show()