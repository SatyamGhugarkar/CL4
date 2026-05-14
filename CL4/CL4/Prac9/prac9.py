# Iris Dataset Classification using KNN
# to install sklearn: pip install scikit-learn
#  to install pandas: pip install pandas
#  to install matplotlib: pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

# ---------------- LOAD DATASET ----------------
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(df.head())

# Features and Target
X = iris.data
Y = iris.target

# ---------------- VISUALIZATION ----------------
plt.figure(figsize=(6,5))

plt.scatter(
    X[:,0],      # Sepal Length
    X[:,1],      # Sepal Width
    c=Y          # Color by class
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset Visualization")

plt.show()

# ---------------- SPLIT DATASET ----------------
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=1
)

print("\nTest Dataset Size:")
print("X:", X_test.shape)
print("Y:", Y_test.shape)

# ---------------- TRAIN MODEL ----------------
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, Y_train)

# ---------------- PREDICTION ----------------
predictions = model.predict(X_test)

# ---------------- CONFUSION MATRIX ----------------
cm = confusion_matrix(Y_test, predictions)

print("\nConfusion Matrix:\n")
print(cm)

# ---------------- CLASSIFICATION REPORT ----------------
report = classification_report(Y_test, predictions)

print("\nClassification Report:\n")
print(report)