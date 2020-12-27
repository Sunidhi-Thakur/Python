# classification: To predict whether a flower is iris-Setosa or not
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()

'''print(iris.keys())
dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
Data = features
target = tpyes of iris
descr = description of data and target'''

# Training using one-variable
X = iris["data"][:, 3:]
y = (iris["target"] == 0).astype(np.int)

clf = LogisticRegression()
clf.fit(X, y)

example = clf.predict([[0.2]])
print(example)

# Plotting using Matplotlib
X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
Y_prob = clf.predict_proba(X_new)
plt.plot(X_new, Y_prob[:, 1])
plt.show()