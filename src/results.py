from sklearn.model_selection import cross_val_score

features = ['avg_nh_score', 'Percent Living in Poverty', 'Percent High School Education',
            'Median Household Income', 'Gini Coefficient', 'Percent Uninsured',
            'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden', 'Syphilis Rate']

best_score = 0
best_features = None

for i in range(len(features)):
    for j in range(i+1, len(features)):
        X = merged_df[[features[i], features[j]]]
        y = merged_df['Rates of Persons Living with HIV, 2020']

        lr = LinearRegression()

        # Perform 5-fold cross validation
        scores = cross_val_score(lr, X, y, cv=5, scoring='explained_variance')
        score = scores.mean()

        if score > best_score:
            best_score = score
            best_features = (features[i], features[j])

print("Best score:", best_score)
print("Best features:", best_features)

# Import necessary libraries
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Define the features (X) and the target (y)
X = merged_df[['avg_nh_score', 'Percent Living in Poverty', 'Percent High School Education', 'Median Household Income', 'Gini Coefficient', 'Percent Uninsured', 'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden', 'Syphilis Rate']]
y = merged_df['Rates of Persons Living with HIV, 2020']

# Create a Linear Regression model
lr = LinearRegression()

# Perform 5-fold cross-validation
scores = cross_val_score(lr, X, y, cv=5)

# Print the mean score and the 95% confidence interval for the score estimate
print("Cross-validation Score: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))