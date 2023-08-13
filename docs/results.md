This project built off the work of two previous groups. The first issue we encountered was creating a pipeline of transparent code to reproduce the datasets the other groups had created. This involved tracking down where intial files were downloaded from, and in some cases created from all of which can be found in docs/sources.md

Based on our hypothesis we ran a basic linear regression model on the whole dataset with the included list of features seen in the summary table below.

The model did not do well. This is seen in our R-squared score of 0.086

### Model 1 - Full Population

Linear Regression - Full Population

```

                                      OLS Regression Results
==================================================================================================
Dep. Variable:     Rates of Persons Living with HIV, 2020   R-squared:                       0.086
Model:                                                OLS   Adj. R-squared:                  0.081
Method:                                     Least Squares   F-statistic:                     17.32
Date:                                    Sun, 13 Aug 2023   Prob (F-statistic):           8.02e-25
Time:                                            13:52:47   Log-Likelihood:                -10036.
No. Observations:                                    1478   AIC:                         2.009e+04
Df Residuals:                                        1469   BIC:                         2.014e+04
Df Model:                                               8
Covariance Type:                                nonrobust
==================================================================================================================
                                                     coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------------------------
Percent Living in Poverty                          6.9459      1.824      3.807      0.000       3.367      10.524
Percent High School Education                     -4.1979      0.812     -5.171      0.000      -5.790      -2.606
Median Household Income                            0.0030      0.001      4.828      0.000       0.002       0.004
Gini Coefficient                                 668.5884    192.331      3.476      0.001     291.315    1045.862
Percent Uninsured                                  2.8547      1.455      1.962      0.050       0.001       5.709
Percent Unemployed                                -7.3420      2.911     -2.522      0.012     -13.052      -1.632
Percent Living with Severe Housing Cost Burden     3.9185      2.005      1.955      0.051      -0.014       7.851
Syphilis Rate                                      0.1380      0.502      0.275      0.783      -0.846       1.122
avg_nh_score                                       2.9649      5.533      0.536      0.592      -7.889      13.819
==============================================================================
Omnibus:                     1073.939   Durbin-Watson:                   1.734
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            21878.153
Skew:                           3.181   Prob(JB):                         0.00
Kurtosis:                      20.742   Cond. No.                     2.01e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.01e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
```

##### Cross Validation
```
Cross-validated R^2: 0.08393503551491376
```
##### Lasso Rankings
```
Ranked features by Lasso:

Percent Living in Poverty                         3.995628
Syphilis Rate                                     0.424319
Median Household Income                           0.000613
Percent High School Education                     0.000000
Gini Coefficient                                  0.000000
Percent Uninsured                                 0.000000
Percent Unemployed                                0.000000
Percent Living with Severe Housing Cost Burden    0.000000
avg_nh_score                                      0.000000
dtype: float64
```

Unfortunately Average Nursing Home Score is not statistically significant along with being ranked last using Lasso feature selection.

### Model 2 - 55+ Population


We repeated the same modeling and cross-validation with an abbreviated dataset looking at only populations about 55 years old.
```
Linear Regression - 55+ Population

                            OLS Regression Results
==============================================================================
Dep. Variable:                 hiv55+   R-squared:                       0.138
Model:                            OLS   Adj. R-squared:                  0.134
Method:                 Least Squares   F-statistic:                     29.47
Date:                Sun, 13 Aug 2023   Prob (F-statistic):           6.00e-43
Time:                        14:56:46   Log-Likelihood:                -10239.
No. Observations:                1478   AIC:                         2.050e+04
Df Residuals:                    1469   BIC:                         2.054e+04
Df Model:                           8
Covariance Type:            nonrobust
==================================================================================================================
                                                     coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------------------------
Percent Living in Poverty                          2.5241      2.093      1.206      0.228      -1.581       6.630
Percent High School Education                     -6.0130      0.931     -6.456      0.000      -7.840      -4.186
Median Household Income                            0.0043      0.001      6.050      0.000       0.003       0.006
Gini Coefficient                                 427.2252    220.656      1.936      0.053      -5.610     860.060
Percent Uninsured                                  1.7192      1.669      1.030      0.303      -1.555       4.993
Percent Unemployed                                 0.9388      3.339      0.281      0.779      -5.612       7.489
Percent Living with Severe Housing Cost Burden    15.7221      2.300      6.836      0.000      11.211      20.234
Syphilis Rate                                      1.8257      0.576      3.171      0.002       0.696       2.955
avg_nh_score                                       1.2603      6.348      0.199      0.843     -11.192      13.713
==============================================================================
Omnibus:                     1249.711   Durbin-Watson:                   2.008
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            47792.481
Skew:                           3.731   Prob(JB):                         0.00
Kurtosis:                      29.840   Cond. No.                     2.01e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.01e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
```
##### Cross Validation
```
Cross-validated R^2: 0.07993875251666359
```
##### Lasso Rankings
```
Ranked features by Lasso:

Syphilis Rate                                     1.150892
Median Household Income                           0.002016
Percent Living in Poverty                         0.000000
Percent High School Education                     0.000000
Gini Coefficient                                  0.000000
Percent Uninsured                                 0.000000
Percent Unemployed                                0.000000
Percent Living with Severe Housing Cost Burden    0.000000
avg_nh_score                                      0.000000
dtype: float64
```

This model found Syphilis rate to be a stronger feature the Percent Living in Poverty, which was the top feature after lasso in the previous model using the entire population. Unfortunately both models found the avg_nh_score to be the least important of the features. 

This can likely be contributed to a couple of different factors. Firstly the nursing home score itself has its own issue as a metric of measure for one of our features. As it is a generated metric there may be variables that go into its creation that would be better suited for this modeling. 

https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/CertificationandComplianc/downloads/usersguide.pdf

This has the technical details of the scores used for nursing home rating and there maybe a better metric for evaluating nursing homes relative to HIV prevalence, for future modeling.
