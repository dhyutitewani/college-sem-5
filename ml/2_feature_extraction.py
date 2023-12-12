import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split as t_t
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import confusion_matrix as cm

data = pd.read_csv('wine.csv')

x = data.iloc[:, 0:13].values
y = data.iloc[:, 13].values

x_train, x_test, y_train, y_test = t_t(x, y, test_size = 0.25, random_state = 0)

ss = StandardScaler()

x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

pca = PCA(n_components = 1)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)

explained_variance = pca.explained_variance_ratio_

classifier_1 = lr(random_state = 0)
classifier_1.fit(x_train, y_train)

y_pred = classifier_1.predict(x_test)

cm = cm(y_test, y_pred)

from matplotlib.colors import ListedColormap as LCM

def visualize_results(X_set, Y_set, title, classifier, colors):
    X_1, X_2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                           np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    
    plt.contourf(X_1, X_2, classifier.predict(np.array([X_1.ravel(), X_2.ravel()]).T).reshape(X_1.shape),
                 alpha=0.75, cmap=LCM(colors))
    
    plt.xlim(X_1.min(), X_1.max())
    plt.ylim(X_2.min(), X_2.max())
    
    for s, t in enumerate(np.unique(Y_set)):
        plt.scatter(X_set[Y_set == t, 0], X_set[Y_set == t, 1],
                    c=LCM(('red', 'green', 'blue'))(s), label=t)
    
    plt.title(title)
    plt.xlabel('PC_1')
    plt.ylabel('PC_2')
    plt.legend()
    plt.show()

# Visualize training set results
visualize_results(x_train, y_train, 'Logistic Regression for Training set:', classifier_1, ('yellow', 'grey', 'green'))

# Visualize test set results
visualize_results(x_test, y_test, 'Logistic Regression for Testing set:', classifier_1, ('pink', 'grey', 'aquamarine'))

