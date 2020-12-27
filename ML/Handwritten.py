''' Handwritten DIgit Recognition on MNIST dataset.
    Set of small images (28x28 pixels) labelled with the respective digit they represent
    [70000 rows x 784 columns]'''

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.imshow
import numpy as np

#pylint: disable=no-member
mnist = fetch_openml('mnist_784')

x, y = mnist['data'], mnist['target']

digit = x.iloc[36]
digit_image = digit.values.reshape(28,28)

plt.imshow(digit_image, cmap=matplotlib.cm.binary, interpolation="nearest")
plt.show()

x_train = x.iloc[:60]
x_test = x.iloc[60:80]
y_train = y.iloc[:60]
y_test = y.iloc[60:80]

shuffle = np.random.permutation(60) 
x_train, y_train = x_train.iloc[shuffle], y_train.iloc[shuffle]

# convert string to int
y_train = y_train.astype(np.int8)
y_test = y_test.astype(np.int8)

# Digit Detector
y_train_D = (y_train == 6)
y_test_D = (y_test == 6)

clf = LogisticRegression()
clf.fit(x_train, y_train_D)

print(clf.predict([digit]))

#Check Accuracy
accuracy = cross_val_score(clf, x_train, y_train_D, cv = 3, scoring = "accuracy")
print(int((accuracy.mean())*100), "%")