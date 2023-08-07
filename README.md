# Equitable health care

### Project partners - Group 3

* Timothy Moriarity - moriarity.t@northeastern.edu
* Mohammed Shati - shati.m@northeastern.edu


### Stakeholder

Prof. Brianne Olivieri-Mui, Dept of Health Sciences

### Story

Hundreds of millions of federal dollars have been allocated for treatment and eradication HIV. The goal of this study is to look for socioeconomic factors that could give rise to more equitable allocation of funds. The results could have implications for policy makers and government agencies administering those funds. This project builds from previous work accomplished in DS5110 students. Dr. Olivieri-Mui is very interested in seeing this work continue and ready to engage as needed!


### Data

All data is publicly available. We have included the necessary files in the data folder of the repo to save time in recreation.

The data can be obtained from the list of links found in the data.md file in the docs folder.

The necessary data can be recreated with the following command:

```
make data
```

### Model

Building off the work done by the previous groups we were able to run a linear regression model with the key feature of interest being the nursing home rating.

We are looking to see if the rating of an areas nursing homes has an impact on HIV infections.
```
make model
```
### Results

Creates figures & results.

```
make results
```
```
Linear Regression
Full Population
Cross-validated R^2: 0.0060534304566499
Top 3 features selected by Lasso:
['Percent Living in Poverty', 'Syphilis Rate', 'Percent Living with Severe Housing Cost Burden']
```
<img src="figs/fullpopulation.png" width="500px">

```
Linear Regression
55+ Population
Cross-validated R^2: 0.011645046654678281
Top 3 features selected by Lasso:
['Syphilis Rate', 'Median Household Income', 'Percent Living in Poverty']
```
<img src="figs/55+population.png" width="500px">

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