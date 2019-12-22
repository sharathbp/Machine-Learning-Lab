from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix
kmm = KMeans(3)
kmm.fit(iris.data)
accuracy = accuracy_score(iris.target, kmm.labels_)
print("Accuracy=%.2f" % accuracy)
print("Confusion Matrix : \n", confusion_matrix(iris.target, kmm.labels_))

import matplotlib.pyplot as plt
import numpy as np
colormap = np.array(['red', 'lime', 'black'])

plt.figure(figsize=(10,3))
plt.subplot(1,2,1)
plt.scatter(iris.data[:,0], iris.data[:,1], c=colormap[iris.target], s=40)
plt.title('Sepal')
plt.subplot(1,2,2)
plt.scatter(iris.data[:,2], iris.data[:,3], c=colormap[iris.target], s=40)
plt.title('Petal')

plt.figure(figsize=(10,3))
plt.subplot(1,2,1)
plt.scatter(iris.data[:,2], iris.data[:,3], c=colormap[iris.target], s=40)
plt.title('Real Classification')
plt.subplot(1,2,2)
plt.scatter(iris.data[:,2], iris.data[:,3], c=colormap[kmm.labels_], s=40)
plt.title('K-Means Classification')


