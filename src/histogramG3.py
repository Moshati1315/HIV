from imports import *

merged = pd.read_csv('data/group3data.csv')


x = merged[['Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden',
            'Syphilis Rate', 'avg_nh_score']]

y = merged['Rates of Persons Living with HIV, 2020']

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
plt.savefig('figs/fullpopulation.png')
plt.show()


# Group 3 - MS