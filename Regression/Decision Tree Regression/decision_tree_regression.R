# Decision Tree Regression
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

library(rpart)
regressor = rpart(formula = Salary ~ ., 
                  data = dataset,
                  control = rpart.control(minsplit = 1))

library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + geom_point(aes(dataset$Level, dataset$Salary)) + 
  geom_line(aes(x_grid, predict(regressor, newdata = data.frame(Level = x_grid)))) +
  ggtitle('Salary Vs Level') + xlab('Level') + ylab('Salary')

prediction = predict(regressor, data.frame(Level = 6.5))