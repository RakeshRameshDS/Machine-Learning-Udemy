# Random Forest - Regression

# Import the Data set
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Fitting the Random Forest Regression model to the dataset
library(randomForest)
set.seed(1234)
regressor = randomForest(formula = Salary ~ ., data = dataset, ntree = 100)

# Predicting the salary of a new employee
prediction = predict(regressor, data.frame(Level = 6.5))

# Plotting
library(ggplot2)
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + geom_point(aes(dataset$Level, dataset$Salary)) +
  geom_line(aes(X_grid, predict(regressor, data.frame(Level = X_grid)), color = 'red')) +
  ggtitle('Salary Vs Level (Random Forest)') + xlab('Level') + ylab('Salary')