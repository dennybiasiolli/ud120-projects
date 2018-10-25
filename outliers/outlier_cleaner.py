#!/usr/bin/python
from itertools import izip


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for prediction, age, net_worth in izip(predictions, ages, net_worths):
        error = net_worth[0] - prediction[0]
        cleaned_data.append(
            (age[0], net_worth[0], error)
        )
        # print(age, net_worth, abs(error))
    cleaned_data.sort(key=lambda tup: tup[2], cmp=lambda x,y: int(abs(x) - abs(y)))
    return cleaned_data[:int(len(cleaned_data)*0.9)]

