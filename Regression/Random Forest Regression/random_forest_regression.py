# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:55:23 2017

@author: rakes
"""

# Random Forest Regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Random Forest Model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0, 
                                  max_features= 'sqrt')
regressor.fit(X, y)

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid))
plt.title('Salary Vs Label (Random Forest)')
plt.xlabel('Label')
plt.ylabel('Salary')
plt.show()

# Predict salary of a new employee
value = regressor.predict(np.array([[6.5]]))
print(value)