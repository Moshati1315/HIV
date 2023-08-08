## Equitable Health Care - HIV Prevalence & Nursing Home Ratings


### Stakeholder

Prof. Brianne Olivieri-Mui, Dept of Health Sciences

### Project partners - Group 3

* Timothy Moriarity - moriarity.t@northeastern.edu
* Mohammed Shati - shati.m@northeastern.edu

### Story 

HIV and aids is a significant public health issue that has resulted in the deaths of millions of people. Medicaid is the only public insurance that pays for nursing home care. A significant portion of people living with HIV (PLWH) have Medicaid, many are also dually eligible for Medicare. Having Medicaid or Medicare means access to Part D prescription drug coverage which is mandated to cover HIV medications (they are one of the 6 protected classes of drugs). Nursing homes however do not keep these drugs on formulary because they are relatively rare and is potentially contributing to issues with antiretroviral therapy (ART) adherence in this setting. There exists publicly available data provided by Medicare.gov that ranks nursing homes on a star rating from 1 to 5, with 1 indicating the worst care and 5 indicating the best care. For this reason we are looking for a relationship between the ratings of an areas nursing homes and the prevelance of HIV in that area.

Based on this hypothesis we are looking at what if any relationship there is between a nursing home ratings and the prevelance of HIV in an area. We have a hypothesis that the higher the ratings of nursing homes in an area the lower the prevalence of HIV. If this holds true, this would support the allocation of public funds to combat HIV by raising the quality of nursing home care.


### Data

All data is publicly available. We have included the necessary files in the data folder of the repo to save time in recreation.

The data can be obtained from the list of links found in the sources.md file in the docs folder.

The necessary data can be recreated with the following command:

```
make data
```
This histogram shows the distributions of our features we are including:
<img src="figs/fullpopulation.png" width="750px">
### Model

Building off the work done by the previous groups we were able to run a linear regression model with the key feature of interest being nursing home ratings.

We are looking to see if the rating of an areas nursing homes has an impact on HIV infections.
```
make model
```
Creates figures & results whcih are partially shown below and in full detail in the results.md file in the docs folder.
```

Linear Regression - Full Population

                                      OLS Regression Results
==================================================================================================
Dep. Variable:     Rates of Persons Living with HIV, 2020   R-squared:                       0.006
Model:                                                OLS   Adj. R-squared:                  0.006
Method:                                     Least Squares   F-statistic:                     131.4
Date:                                    Mon, 07 Aug 2023   Prob (F-statistic):          7.58e-221
Time:                                            22:43:23   Log-Likelihood:            -1.1207e+06
No. Observations:                                  168379   AIC:                         2.241e+06
Df Residuals:                                      168370   BIC:                         2.241e+06
Df Model:                                               8
Covariance Type:                                nonrobust
==================================================================================================================
                                                     coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------------------------
Percent Living in Poverty                          2.2038      0.189     11.636      0.000       1.833       2.575
Percent High School Education                      0.3652      0.078      4.700      0.000       0.213       0.518
Median Household Income                            0.0010   5.95e-05     16.865      0.000       0.001       0.001
Gini Coefficient                                 100.5951     17.472      5.757      0.000      66.350     134.841
Percent Uninsured                                  0.1482      0.117      1.263      0.207      -0.082       0.378
Percent Unemployed                                 1.7285      0.251      6.887      0.000       1.237       2.220
Percent Living with Severe Housing Cost Burden     0.9847      0.174      5.666      0.000       0.644       1.325
Syphilis Rate                                      0.2495      0.050      4.956      0.000       0.151       0.348
avg_nh_score                                      -8.0424      0.461    -17.446      0.000      -8.946      -7.139
==============================================================================
Omnibus:                   117034.545   Durbin-Watson:                   0.158
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          2470338.299
Skew:                           3.102   Prob(JB):                         0.00
Kurtosis:                      20.710   Cond. No.                     2.22e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.22e+06. This might indicate that there are
strong multicollinearity or other numerical problems.

The indepth results can be found in docs folder results.md, including a recreation of this summary as well as cross validated rsquared scores, lasso feature reduction ranks, and analysis. 

```

#### Second model - only populations above age 55 HIV prevalence rates used as a dependent variable.

Creates a model with only 55+ age group.

```
make m55
```
The results are in the results.md file. 


### Referencing

sources.md in src folder

##### We are building off the work of two previous groups.

##### Every file will have a reference to where it originated, and if it has been modified or not. 
##### This will be done by a reference to the group at the bottom of every file.

#### Group 1
* Nick Barnes
* Paige Norris
* https://github.com/ds5110/bioscience

#### Group 2 
* Amanda Haskell
* Mian Wang
* Nicholas Letarte
* https://github.com/ds5110/projects-spring-2023-ahaskell83/tree/main


Group 3