import numpy as np
import pandas as pd 
import matplotlib.pyplot as mtp
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split as t_t
from sklearn.preprocessing import StandardScaler as ss
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix as cm

data_set = pd.read_csv('data.csv')

x= data_set.iloc[:, [2,3]].values 
y= data_set.iloc[:, 4].values

x_train, x_test, y_train, y_test = t_t(x, y, test_size = 1/3, random_state = 0)

x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

classifier = LogisticRegression(random_state = 0)

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

cm = cm()