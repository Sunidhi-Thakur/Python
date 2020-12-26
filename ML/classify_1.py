from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

#Loading Datasets
iris = datasets.load_iris()

features = iris.data
labels = iris.target

''':Attribute Information:
        - sepal length in cm
        - sepal width in cm
        - petal length in cm
        - petal width in cm'''

# Training classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[1, 6.4, 7, 1]])
if preds == 0:
    print("Iris-Setosa")
elif preds == 1:
    print("Iris-Versicolour")
elif preds == 2:
    print("Iris-Virginica")
else:
    print("Check Input")

