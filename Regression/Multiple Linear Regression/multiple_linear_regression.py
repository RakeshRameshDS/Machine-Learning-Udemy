# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 12:10:45 2017

@author: rakes
"""

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Fifty_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical variables
from sklearn.preprocessing import LabelEncoder
label_encoder_X = LabelEncoder()
X[:,3] = label_encoder_X.fit_transform(X[:, 3])

from sklearn.preprocessing import OneHotEncoder
Onehotencoder = OneHotEncoder(categorical_features=[3])
X = Onehotencoder.fit_transform(X).toarray()

# Dummy Variable trap Elimination
X = X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 0)

# No feature scaling required. Library will do it for us. 

# Fitting Multi Linear Regression Model to Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Set Results
y_pred = regressor.predict(X_test)

# Building optimal model using Backward Elimination
# Remove variables that are not statistically significant

import statsmodels.formula.api as sm
X = np.append(arr = np.ones(shape=(50,1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 3, 5]]
# OLS - Ordinary Least Squares
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
