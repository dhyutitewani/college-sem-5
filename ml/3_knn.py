import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split as t_t
from sklearn.preprocessing import StandardScaler as ss
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import confusion_matrix as cm

data = pd.read_csv('data.csv')

x = data.iloc[:, [2,3]].values
y = data.iloc[:, 4].values

x_train, x_test, y_train, y_test = t_t(x, y, test_size = 0.25, random_state = 0)

x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

# applying knn
classifier = knn(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

cm = cm(y_test, y_pred)

# visualizing
def visualize_results(x_set, y_set, title):
    x1, x2 = np.meshgrid(np.arange(start=x_set[:, 0].min() - 1, stop=x_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=x_set[:, 1].min() - 1, stop=x_set[:, 1].max() + 1, step=0.01))
    
    plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
                 alpha=0.75, cmap=ListedColormap(('purple', 'green')))
    
    plt.xlim(x1.min(), x1.max())
    plt.ylim(x2.min(), x2.max())
    
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                    c=ListedColormap(('purple', 'green'))(i), label=j)
    
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()

# Visualize training set results
visualize_results(x_train, y_train, 'KNN Algorithm (Training set)')

# Visualize test set results
visualize_results(x_test, y_test, 'KNN Algorithm (Test set)')
