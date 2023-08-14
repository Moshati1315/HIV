from imports import pd, sns, plt

merged = pd.read_csv('data/group3data.csv')
merged = merged[~merged['nh_count'].isin([101, 81, 205, 375, 65, 70, 73])]

cols_to_plot = ['Percent Living in Poverty', 'Percent High School Education',
                'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
                'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
                'Syphilis Rate', 'avg_nh_score', 'nh_count']

plt.figure(figsize=(15,10))

for idx, col in enumerate(cols_to_plot, start=1):
    plt.subplot(3, 4, idx)
    sns.boxplot(y=col, data=merged)
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
plt.savefig('figs/FeatureBoxOutlierDrop.png')
plt.savefig('docs/figs/FeatureBoxOutlierDrop.png')
plt.show()