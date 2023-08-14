from imports import sns, plt, pd

merged = pd.read_csv('data/group3data.csv')

plt.figure(figsize=(10, 8))
sns.scatterplot(x='nh_count', y='Rates of Persons Living with HIV, 2020', data=merged)
plt.title('Nursing Home Count vs. Rates of Persons Living with HIV, 2020')
plt.xlabel('nh_count')
plt.ylabel('Rates of Persons Living with HIV, 2020')
plt.savefig('figs/nh_outlier_scatter.png')
plt.savefig('docs/figs/nh_outlier_scatter.png')
plt.show()