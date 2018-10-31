#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn.cross_validation import  train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.tree import DecisionTreeClassifier
from time import time


clf = DecisionTreeClassifier()
t0 = time()
clf.fit(features, labels)
print("training time:", round(time()-t0, 3), "s")
t1 = time()
pred = clf.predict(features)
print("predict time:", round(time()-t1, 3), "s")
print("accuracy:", accuracy_score(pred, labels))

print("")
x_train, x_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
t0 = time()
clf.fit(x_train, y_train)
print("training time:", round(time()-t0, 3), "s")
t1 = time()
pred = clf.predict(x_test)
print("predict time:", round(time()-t1, 3), "s")
print("accuracy:", accuracy_score(pred, y_test))

print("POIs predicted: {0}".format(len(filter(lambda p: p == 1, pred))))
print("Total people: {0}".format(len(y_test)))
print("Accuracy if all '0' were predicted: {0}".format(
    accuracy_score([0]*len(y_test), y_test))
)
print("True positives: {0}".format(
    len(filter(lambda t: t[0] == t[1] == 1, zip(pred, y_test)))
))

print("Precision score: {0}".format(
    precision_score(y_test, pred)
))
print("Recall score: {0}".format(
    recall_score(y_test, pred)
))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print("True positives: {0}".format(
    len(filter(lambda t: t[0] == t[1] == 1, zip(predictions, true_labels)))
))
print("True negatives: {0}".format(
    len(filter(lambda t: t[0] == t[1] == 0, zip(predictions, true_labels)))
))
print("False positives: {0}".format(
    len(filter(lambda t: t[0] == 1 and t[1] == 0, zip(predictions, true_labels)))
))
print("False negatives: {0}".format(
    len(filter(lambda t: t[0] == 0 and t[1] == 1, zip(predictions, true_labels)))
))
print("Precision score: {0}".format(
    precision_score(true_labels, predictions)
))
print("Recall score: {0}".format(
    recall_score(true_labels, predictions)
))
