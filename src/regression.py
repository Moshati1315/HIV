# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define the features (X) and the target (y)
X = merged_df[['avg_nh_score', 'Percent Living in Poverty', 'Percent High School Education', 'Median Household Income', 'Gini Coefficient', 'Percent Uninsured', 'Percent Unemployed', 'Percent Living with Severe Housing Cost Burden', 'Syphilis Rate']]
y = merged_df['Rates of Persons Living with HIV, 2020']

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
lr = LinearRegression()

# Fit the model with the training data
lr.fit(X_train, y_train)

# Predict the target for the test set
y_pred = lr.predict(X_test)


# Print train and test scores
print("Train Score:", lr.score(X_train, y_train))
print("Test Score:", lr.score(X_test, y_test))
coefficients = lr.coef_

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

# Create a base classifier
lr = LinearRegression()

# Create the RFE model and select 3 attributes
rfe = RFE(lr, n_features_to_select=3, step=1)
rfe = rfe.fit(X, y)

# Summarize the selection of the attributes
print('Selected features: %s' % list(X.columns[rfe.support_]))