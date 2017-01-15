# Simple Linear Regression

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Simple Linear Regression to the Training Set
regressor = lm(formula = Salary ~ YearsExperience, 
               data = training_set)

# Predicting the Test Set Results
y_pred = predict(regressor, newdata = test_set)

# Visualizing the Training set results
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), 
             color = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, new_data = training_set)), 
            color = 'blue') +
  ggtitle('Salary Vs Experience (Training Set)') + 
  xlab('Years of Experience') + 
  ylab('Salary in USD')
  
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary), color = 'red') +
  geom_line(aes(x = test_set$YearsExperience, y = y_pred), color = 'blue') + 
  ggtitle('Salary Vs Experience (Test Set)') + 
  xlab('Years of Experience') + 
  ylab('Salary in USD')