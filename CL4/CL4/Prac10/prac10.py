# Iris Dataset Clustering using K-Means
#  to install sklearn, run: pip install scikit-learn
#  to install pandas, run: pip install pandas
#  to install matplotlib, run: pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# ---------------- LOAD DATASET ----------------
iris = load_iris()

X = iris.data
Y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)

print("Dataset:\n")
print(df.head())

# ---------------- BEFORE CLUSTERING ----------------
plt.figure(figsize=(6,5))

plt.scatter(X[:,0], X[:,1])

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Before Clustering")

plt.show()

# ---------------- K-MEANS CLUSTERING ----------------
kmeans = KMeans(n_clusters=3, random_state=1)

kmeans.fit(X)

clusters = kmeans.labels_

# Add Cluster Column
df["Cluster"] = clusters

print("\nClustered Data:\n")
print(df.head())

# ---------------- AFTER CLUSTERING ----------------
plt.figure(figsize=(6,5))

plt.scatter(X[:,0], X[:,1], c=clusters)

# Cluster Centers
centers = kmeans.cluster_centers_

plt.scatter(
    centers[:,0],
    centers[:,1],
    marker="X",
    s=200
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("After K-Means Clustering")

plt.show()

# ---------------- KNN CLASSIFICATION ----------------
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=1
)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, Y_train)

predictions = knn.predict(X_test)

# ---------------- CONFUSION MATRIX ----------------
cm = confusion_matrix(Y_test, predictions)

print("\nConfusion Matrix:\n")
print(cm)

# ---------------- CLASSIFICATION REPORT ----------------
report = classification_report(Y_test, predictions)

print("\nClassification Report:\n")
print(report)