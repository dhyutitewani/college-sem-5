import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA

# Step 2: Loading the Data
M = pd.read_csv('sampleDataset.csv').drop('CUST_ID', axis=1).fillna(method='ffill')

# Step 3: Preprocessing the data
M_normalized = pd.DataFrame(normalize(StandardScaler().fit_transform(M)))

# Step 4: Reduce the dimensionality of the data
M_principal = pd.DataFrame(PCA(n_components=2).fit_transform(M_normalized), columns=['C1', 'C2'])

# Step 5: Build a clustering model
db_default = DBSCAN(eps=0.0375, min_samples=3).fit(M_principal)
labeling = db_default.labels_

# Step 6: Visualize the clustering model
colors = {0: 'g', 1: 'k', 2: 'r', -1: 'b'}
cvec = [colors[label] for label in labeling]
plt.figure(figsize=(9, 9))
plt.scatter(M_principal['C1'], M_principal['C2'], c=cvec)
plt.legend([plt.scatter([], [], color=color) for color in colors.values()], [f'Label M.{label}' for label in colors.keys()])
plt.show()

# Step 7: Tuning the parameters
dts = DBSCAN(eps=0.0375, min_samples=50).fit(M_principal)
labeling = dts.labels_

# Step 8: Visualization of the changes
colors1 = {i: plt.cm.jet(float(i) / max(labeling + 1)) for i in set(labeling)}
cvec = [colors1[label] for label in labeling]
plt.figure(figsize=(9, 9))
for label, color in colors1.items():
    plt.scatter(M_principal.loc[labeling == label, 'C1'], M_principal.loc[labeling == label, 'C2'], color=color)
plt.legend([plt.scatter([], [], color=color) for color in colors1.values()], [f'Label M.{label}' for label in colors1.keys()])
plt.show()
