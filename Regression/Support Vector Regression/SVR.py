# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 00:27:33 2017

@author: rakes
"""

# SVR - Support Vector Regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:, 2].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(y)

# Build a SVR Model on the scaled feature set
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf', C = 10.0)
regressor.fit(X, Y)

# Visualizing SVR predictions
# Generating grid of X values to obtain a nice smooth curve during plot of the predictions.
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(sc_X.inverse_transform(X), y)
plt.plot(sc_X.inverse_transform(X_grid), sc_Y.inverse_transform(regressor.predict(X_grid)))
plt.title('Level Vs Salary')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

# Predict a new Point
y_new_pred = sc_Y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))
print(y_new_pred)