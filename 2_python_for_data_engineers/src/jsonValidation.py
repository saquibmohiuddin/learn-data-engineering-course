import json, jsonschema
from pprint import pprint
from jsonschema import validate

transaction_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "InvoiceNo": {"type": "integer"},
        "StockCode": {"type": "integer"},
        "Description": {"type": "string"},
        "Quantity": {"type": "integer"},
        "InvoiceDate": {"type": "string"},
        "UnitPrice": {"type": "number"},
        "CustomerID": {"type": "integer"},
        "Country": {"type": "string"}
    },
    "required": ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
}

# creating validation function

def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as error:
        return False
    return True


def validate_json_schema(json_data):
    """REF: https://json-schema.org/"""
    try:
        validate(instance=json_data, schema=transaction_schema)
    except jsonschema.exceptions.ValidationError as error:
        print(f"Error: {error}")
        error = "Given JSON data is InValid"
        return False, error
    error_message = "Given JSON data is Valid"
    return True, error_message

if __name__ == "__main__":
    # 1. Load JSONs from file
    with open('././instructor_resources/1_python2/data/data_subset.json') as f:
        employees = json.load(f)

    valid_transaction_dict = employees[0]
    pprint(valid_transaction_dict)

    res = validate(instance=valid_transaction_dict, schema=transaction_schema)
    print(res)

    customer_id_missing_dict = {
        "InvoiceNo": "536373",
        "StockCode": 85123,
        "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
        "Quantity": 6,
        "InvoiceDate": "2010-12-01 08:26:00",
        "UnitPrice": 2.55,
        "Country": "United Kingdom"
    }

    InvoiceNo_is_a_string = {
        "InvoiceNo": "536373",
        "StockCode": 85123,
        "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
        "Quantity": 6,
        "InvoiceDate": "2010-12-01 08:26:00",
        "UnitPrice": 2.55,
        "Country": "United Kingdom",
        "CustomerID": 17850
    }

    # Loan valid JSON string
    valid_json_string = json.dumps(valid_transaction_dict)
    
    # Create invalid JSON string - missing ',' delimeter.

    invalid_json_string = '{"InvoiceNo": 536370 "StockCode": 22492, "Description":  "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45",   "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'

    # validate JSON string
    res = validate_json(valid_json_string)
    print(res)


    # validate invalid JSON string
    res = validate_json(invalid_json_string)
    print(res)

    # validate data with valid schema
    res = validate_json_schema(valid_transaction_dict, my_schema = transaction_schema)
    print(res)

    # validate data with inValid schema
    res = validate_json_schema(InvoiceNo_is_a_string, my_schema = transaction_schema)
    print(res)

    



