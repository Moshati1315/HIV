
''' 

Imports for use in other files in src. 

'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Needed to recreate Group 2 work
#import geopandas as gpd
#import plotly.express as px


from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Group 1 - Modified by Group 3