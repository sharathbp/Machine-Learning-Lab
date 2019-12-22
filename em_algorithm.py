from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(iris.data)
X = scaler.transform(iris.data)

from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score
gmm = GaussianMixture(3)
gmm.fit(X)
y_pred = gmm.predict(X)
accuracy = accuracy_score(iris.target, y_pred)
print("Accuracy=%.2f" % accuracy)

import matplotlib.pyplot as plt
import numpy as np
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1, 2, 1)
plt.scatter(X[:,2], X[:,3], c=colormap[y_pred], s=40)
plt.title("GMM Classification")

