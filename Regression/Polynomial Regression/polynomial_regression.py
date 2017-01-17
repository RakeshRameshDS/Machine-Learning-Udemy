# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:34:13 2017

@author: rakes
"""

# Polynomial Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

plt.scatter(x=X, y=y)

# Fitting Linear Regression to the Dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the Dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_poly = LinearRegression()
lin_reg_poly.fit(X_poly, y)

# Visualizing the Linear Regression results
y_pred_lin = lin_reg.predict(X)
plt.scatter(X, y, color='red')
plt.plot(X, y_pred_lin)
plt.show()

# Visualizing the Polynomial Regression results
y_pred_poly = lin_reg_poly.predict(X_poly)
plt.scatter(X, y, color='red')
plt.plot(X, y_pred_poly)
plt.show()

# Predicting a new result with lin_reg
res = lin_reg.predict(6.5)
print(res)

# Predicting a new result with Polynomial Regression
P = poly_reg.fit_transform(6.5)
res_poly = lin_reg_poly.predict(P)
print(res_poly)