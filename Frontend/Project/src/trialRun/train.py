# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('merged_data.csv')

#Introducing the independent and dependent variables

# x axis- all the columns except the yield
X = dataset.iloc[:, :-1]

# y axis- daily yield
y = dataset.iloc[:, 3]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Training the dataset

# Gettting multiple independent parameters into x axis to train using linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results by x_test
y_pred = regressor.predict(X_test)

# Finding the accuracy of the model by r2.. 1-(sum of residual/sum of mean)
from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)

#Pickle part

#Saving the model to pkl
pickle.dump(regressor, open('train.pkl','wb'))
#Loading the model to check
pickleModel = pickle.load(open('train.pkl','rb'))

