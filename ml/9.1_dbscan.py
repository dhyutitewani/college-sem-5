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
plt.legend(((g, k, r, b), ('Label M.0', 'Label M.1', 'Label M.2', 'Label M.-1'))
plt.show()

# Step 7: Tuning the parameters
dts = DBSCAN(eps=0.0375, min_samples=50).fit(M_principal)
labeling = dts.labels_

# Step 8: Visualization of the changes
colors1 = {0: 'r', 1: 'g', 2: 'b', 3: 'c', 4: 'y', 5: 'm', -1: 'k'}
cvec = [colors1[label] for label in labeling]
colors = ['r', 'g', 'b', 'c', 'y', 'm', 'k' ] 
r = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[0]) 
g = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[1]) 
b = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[2]) 
c = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[3]) 
y = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[4]) 
m = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[5]) 
k = pplt.scatter(M_principal['C1'], M_principal['C2'], marker ='o', color = colors[6])
plt.figure(figsize=(9, 9))
plt.scatter(M_principal['C1'], M_principal['C2'], c = cvec)
plt.legend((r, g, b, c, y, m, k), 
 ('Label M.0', 'Label M.1', 'Label M.2', 'Label M.3', 'Label M.4','Label M.5', 'Label M.-1'), scatterpoints = 1, loc ='upper left',
 ncol = 3, fontsize = 10)
plt.show()
