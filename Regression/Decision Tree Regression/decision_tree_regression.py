# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 07:06:06 2017

@author: rakes
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting Decision Tree to the Dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Plotting the model
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Salary Vs Level')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

# Predicting value of a new point
prediction = regressor.predict(np.array([[6.5]]))
print(prediction)