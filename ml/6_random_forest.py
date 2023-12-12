import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split as t_t
from sklearn.preprocessing import StandardScaler as ss
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix as cm

data_set = pd.read_csv('user_data.csv')

x= data_set.iloc[:, [2,3]].values 
y= data_set.iloc[:, 4].values

x_train, x_test, y_train, y_test = t_t(x, y, test_size = 1/3, random_state = 0)

x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')

y_pred = classifier.predict(x_test)

cm = cm(y_test, y_pred)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def plot_decision_boundary(x_set, y_set, title):
    x1, x2 = np.meshgrid(np.arange(x_set[:, 0].min() - 1, x_set[:, 0].max() + 1, step=0.01),
                         np.arange(x_set[:, 1].min() - 1, x_set[:, 1].max() + 1, step=0.01))
    
    plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
                 alpha=0.75, cmap=ListedColormap(('purple', 'green')))
    
    plt.xlim(x1.min(), x1.max())
    plt.ylim(x2.min(), x2.max())
    
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                    c=ListedColormap(('purple', 'green'))(i), label=str(j))
    
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()

# Visualizing the training set results
plot_decision_boundary(x_train, y_train, 'Random Forest Algorithm (Training set)')

# Visualizing the test set results
plot_decision_boundary(x_test, y_test, 'Random Forest Algorithm (Test set)')
