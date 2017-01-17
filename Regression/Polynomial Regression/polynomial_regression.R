# Polynomial Regression
# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Fitting Linear Regression to the Dataset
lin_reg = lm(formula = Salary ~ ., data = dataset)
dataset_lin = dataset
summary(lin_reg)
library(ggplot2)

# Fitting Polynomial Regression model to the Dataset
dataset$level_sqr = dataset$Level^2
dataset$level_cube = dataset$Level^3
dataset$level_quad = dataset$Level^4
poly_reg = lm(formula = Salary ~ ., data = dataset)
summary(poly_reg)

ggplot() + 
  geom_point(aes(dataset$Level, dataset$Salary)) + 
  geom_line(aes(dataset$Level, predict(poly_reg, data = dataset)), color = 'red') + 
  geom_line(aes(dataset_lin$Level, predict(lin_reg, data = dataset_lin)), color = 'green') +
  ggtitle('Level Vs Salary') + xlab('Level') + ylab('Salary')

# Predicting Salary given a Level - Linear Model
y_pred_lin = predict(lin_reg, data.frame(Level = 6.5))

# Predicting Salary givem a Level - Polynomial Model
y_pred_poly = predict(poly_reg, data.frame(Level = 6.5,
                                           level_sqr = 6.5^2,
                                           level_cube = 6.5^3,
                                           level_quad = 6.5^4))