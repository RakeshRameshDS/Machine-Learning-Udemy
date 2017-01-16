# Multiple Linear Regression

# Data Preprocessing template

# Importing the dataset
dataset = read.csv('Fifty_Startups.csv')
# Encoding categorical data
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'), 
                       labels = c(1, 2, 3))
# Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Multiple Linear Regression to the Training Set
regressor = lm(formula = Profit ~ R.D.Spend, 
               data = training_set)
summary(regressor)

# Predicting the Test Set results
y_pred = predict(regressor, newdata = test_set)