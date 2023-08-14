from imports import sns, plt, pd

merged = pd.read_csv('data/group3data.csv')
merged = merged[~merged['nh_count'].isin([205, 375])]

plt.figure(figsize=(10, 8))
sns.scatterplot(x='nh_count', y='Rates of Persons Living with HIV, 2020', data=merged)
plt.title('Nursing Home Count after removal of counties with\nLA, Chicago\nvs.\nRates of Persons Living with HIV, 2020')
plt.xlabel('nh_count')
plt.ylabel('Rates of Persons Living with HIV, 2020')

plt.savefig('figs/nh_outlier_CUT1scatter.png')
plt.savefig('docs/figs/nh_outlier_CUT1scatter.png')
plt.show()