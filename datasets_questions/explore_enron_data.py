#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import locale
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(locale.setlocale(locale.LC_ALL, 'en_US.UTF-8'))

persons = enron_data.keys()
print('Person in the dataset: {0}'.format(len(persons)))
for p in persons:
    print('- {0}'.format(p))
print('')

features = enron_data[persons[0]]
print('Features for each person: {0}'.format(len(features)))
for f in features:
    print('- {0}'.format(f))
print('')

persons_of_interest = []
for p in persons:
    if enron_data[p]['poi'] == 1:
        persons_of_interest.append(p)
print('POI in dataset: {0}\n'.format(len(persons_of_interest)))

print('Total value of the stock belonging to James Prentice: {0}\n'.format(
    locale.currency(enron_data['PRENTICE JAMES']['total_stock_value'], grouping=True)
))

print('Email messages from Wesley Colwell to persons of interest: {0}\n'.format(
    enron_data['COLWELL WESLEY']['from_this_person_to_poi']))

print('Stock options exercised by Jeffrey K Skilling: {0}\n'.format(
    locale.currency(enron_data['SKILLING JEFFREY K']['exercised_stock_options'], grouping=True)
))

print('Lay\'s total payments: {0}'.format(
    locale.currency(enron_data['LAY KENNETH L']['total_payments'], grouping=True)
))
print('Skilling\'s total payments: {0}'.format(
    locale.currency(enron_data['SKILLING JEFFREY K']['total_payments'], grouping=True)
))
print('Fastow\'s total payments: {0}'.format(
    locale.currency(enron_data['FASTOW ANDREW S']['total_payments'], grouping=True)
))
print('')


known_salary = 0
known_email_address = 0
for p in persons:
    if enron_data[p]['salary'] != 'NaN':
        known_salary += 1
    if enron_data[p]['email_address'] != 'NaN':
        known_email_address += 1
print('Folks with quantified salary: {0}\nFolks with known email address: {1}\n'
    .format(known_salary, known_email_address))


unknown_total_payments = 0
for p in persons:
    if enron_data[p]['total_payments'] == 'NaN':
        unknown_total_payments += 1
print('People with unknown total payments: {0}, {1:.2f}% of the total.\n'
    .format(
        unknown_total_payments,
        (float(unknown_total_payments) / len(persons) * 100)
    )
)

pois_unknown_total_payments = 0
for p in persons_of_interest:
    if enron_data[p]['total_payments'] == 'NaN':
        pois_unknown_total_payments += 1

print('POIs with unknown total payments: {0}, {1:.2f}% of the total.\n'
    .format(
        pois_unknown_total_payments,
        (float(pois_unknown_total_payments) / len(persons_of_interest) * 100)
    )
)
