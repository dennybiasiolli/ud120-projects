#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def find_outlier_key(my_data_dict, fn_get_val, exclude_keys=[]):
    # finding the outlier
    outlier_key = ""
    outlier_val = 0
    for key in my_data_dict.keys():
        if key in exclude_keys:
            continue
        tmp_val = fn_get_val(my_data_dict[key])
        if tmp_val > outlier_val:
            outlier_val = tmp_val
            outlier_key = key
    return outlier_key


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

# finding and removing maximum outlier
outlier_key = find_outlier_key(
    data_dict,
    lambda x:
        x["salary"] if x["salary"] != "NaN" else 0
)
print("Biggest outlier (to remove): {0}".format(outlier_key))
data_dict.pop(outlier_key, 0)


# finding other outliers
fisrt_outlier_key = find_outlier_key(
    data_dict,
    lambda x:
        x["salary"] if x["salary"] != "NaN" else 0
        * x["bonus"] if x["bonus"] != "NaN" else 0
)
print("First outlier: {0}".format(fisrt_outlier_key))
second_outlier_key = find_outlier_key(
    data_dict,
    lambda x:
        x["salary"] if x["salary"] != "NaN" else 0
        * x["bonus"] if x["bonus"] != "NaN" else 0,
    exclude_keys=[fisrt_outlier_key]
)
print("Second outlier: {0}".format(second_outlier_key))





features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


