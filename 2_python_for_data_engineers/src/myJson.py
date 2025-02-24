import json
from pprint import pprint

"""
agenda:

1. Load JSONs from file
2. Create JSON objects from strings
3. Convert JSON objects to strings
4. Looping though JSON objects
5. Accessing JSON objects - Getting specific data by value from jsons
6. Update part of json 
7. Write JSON to file
"""

# 1. Load JSONs from file
with open('././instructor_resources/1_python2/data/data_subset.json') as f:
    employees = json.load(f)
    pprint(employees)

# 2. Create JSON objects from strings

json_formatted_string = json.dumps(employees)
pprint(json_formatted_string)

# loads json string
transactions_list_dicts = json.loads(json_formatted_string)
pprint(transactions_list_dicts)

# 5. Accessing JSON objects - Getting specific data by value from jsons
pprint(transactions_list_dicts[0].keys())

for transaction in transactions_list_dicts:
    pprint(transaction['InvoiceNo'])

for transaction in transactions_list_dicts:
    pprint(transaction.get('InvoiceNo'))

# using list comprehension
pprint([transaction['InvoiceNo'] for transaction in transactions_list_dicts])
pprint([transaction.get('InvoiceNo') for transaction in transactions_list_dicts])

# show data by specific key value
for transaction in transactions_list_dicts:
    if transaction['InvoiceNo'] == 536372:
        pprint(transaction)

# 6. Update part of json
for transaction in transactions_list_dicts:
    if transaction['InvoiceNo'] == 536372:
        transaction['InvoiceNo'] = 999999

pprint([transaction['InvoiceNo'] for transaction in transactions_list_dicts])

# updating using entire dictionary
update_dict = {
    'InvoiceNo': 999999,
    'StockCode': '12345',
    'Description': 'test',
    'Quantity': 1,
    'InvoiceDate': '2010-12-01 08:26:00',
    'UnitPrice': 1.65,
    'CustomerID': 17850,
    'Country': 'India '
}

for transaction in transactions_list_dicts:
    if transaction['InvoiceNo'] == 999999:
        transaction.update(update_dict)
pprint(transactions_list_dicts)

# 7. Write JSON to file
# dumping back to string
pprint(json.dumps(transactions_list_dicts))

# saving as file
with open('././2_python_for_data_engineers/data/updated_data.json', 'w') as f:
    json.dump(transactions_list_dicts, f)
