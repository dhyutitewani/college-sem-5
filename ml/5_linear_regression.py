import numpy as np
import pandas as pd 
import matplotlib.pyplot as mtp
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split as t_t
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix as cm

data = pd.read_csv('data.csv')

x = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

x_train, x_test, y_train, y_test = t_t(x, y, test_size = 1/3, random_state = 0)

regressor = LinearRegression()
regressor.fit(x_train, x_train)

y_pred= regressor.predict(x_test) 
x_pred= regressor.predict(x_train)

mtp.scatter(x_train, y_train, color="green") 
mtp.plot(x_train, x_pred, color="red") 
mtp.title("Salary vs Experience (Training Dataset)") 
mtp.xlabel("Years of Experience") 
mtp.ylabel("Salary(In Rupees)") 
mtp.show() 

mtp.scatter(x_test, y_test, color="blue") 
mtp.plot(x_train, x_pred, color="red") 
mtp.title("Salary vs Experience (Test Dataset)") 
mtp.xlabel("Years of Experience") 
mtp.ylabel("Salary(In Rupees)") 
mtp.show()