# SVR - Support Vector Regression
dataset = read.csv('POsition_Salaries.csv')
dataset = dataset[2:3]

# Fitting SVR Regressor to the dataset
library(e1071)
svr_regressor = svm(formula = Salary ~ Level, 
                    data = dataset, 
                    type = 'eps-regression',
                    cost = 10.0)

# Plotting the model
library(ggplot2)
ggplot() + 
  geom_point(aes(dataset$Level, dataset$Salary)) + 
  geom_line(aes(dataset$Level, predict(svr_regressor, data = dataset)), color = 'red') +
  ggtitle('Level Vs Salary') + xlab('Level') + ylab('Salary')

# Predict a new Data point
value = predict(svr_regressor, data.frame(Level = 6.5))