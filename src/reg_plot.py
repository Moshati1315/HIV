import matplotlib.pyplot as plt
import numpy as np

# Define the feature
X_avg_nh_score = X_train[['avg_nh_score']]

# Create a new Linear Regression model
lr_single = LinearRegression()

# Fit the model with the single feature
lr_single.fit(X_avg_nh_score, y_train)

# Create a range of values for 'avg_nh_score' to plot against
avg_nh_score_range = np.linspace(X_avg_nh_score.min(), X_avg_nh_score.max()).reshape(-1, 1)

# Predict the target for 'avg_nh_score_range'
y_range_pred = lr_single.predict(avg_nh_score_range)

# Plot 'avg_nh_score' against 'Rates of Persons Living with HIV, 2020'
plt.scatter(X_avg_nh_score, y_train, color='blue')
plt.plot(avg_nh_score_range, y_range_pred, color='red')
plt.xlabel('avg_nh_score')
plt.ylabel('Rates of Persons Living with HIV, 2020')
plt.title('Linear Regression Model Plot')
plt.show()