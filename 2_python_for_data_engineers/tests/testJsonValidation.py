import pytest, json

from jsonschema import validate

from src.jsonValidation import validate_json, validate_json_schema

class Test_JSONValidation:

    def test_validate_json_return_true_for_valid_json(self):

        # arrange
        json_string = {
            "InvoiceNo": 536373,
            "StockCode": 85123,
            "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
            "Quantity": 6,
            "InvoiceDate": "2010-12-01 08:26:00",
            "UnitPrice": 2.55,
            "CustomerID": 17850,
            "Country": "United Kingdom"
        }

        # act
        is_valid_json = validate_json(json_string)

        # assert
        assert is_valid_json == False


    def test_validate_json_schema_return_false_for_invalid_json(self):

        # arrange
        invoiceno_string = {
            "InvoiceNo": "536373",
            "StockCode": 85123,
            "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
            "Quantity": 6,
            "InvoiceDate": "2010-12-01 08:26:00",
            "UnitPrice": 2.55,
            "CustomerID": 12583,
            "Country": "United Kingdom"
            
        }

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

        # act
        is_valid_json_schema, error_message = validate_json_schema(invoiceno_string, my_schema=transaction_schema)


        # assert
        assert is_valid_json_schema == False
        assert error_message == "Given JSON data is InValid"

    def test_validate_json_schema_return_true_for_valid_json(self):

        # arrange
        valid_transaction_dict = {
            "InvoiceNo": 536373,
            "StockCode": 85123,
            "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
            "Quantity": 6,
            "InvoiceDate": "2010-12-01 08:26:00",
            "UnitPrice": 2.55,
            "CustomerID": 17850,
            "Country": "United Kingdom"
        }

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

        # act
        is_valid_json_schema, error_message = validate_json_schema(valid_transaction_dict, my_schema=transaction_schema)

        # assert
        assert is_valid_json_schema == True
        assert error_message == "Given JSON data is Valid"

        # test for pytest.ini having *_test set

    def run_validate_json_return_true_for_valid_json_test(self):

        # arrange
        valid_json_string = {
            "InvoiceNo": 536373,
            "StockCode": 85123,
            "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
            "Quantity": 6,
            "InvoiceDate": "2010-12-01 08:26:00",
            "UnitPrice": 2.55,
            "CustomerID": 17850,
            "Country": "United Kingdom"
        }

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

        # act
        is_valid_json, message = validate_json(valid_json_string, my_schema=transaction_schema)

        # assert
        assert is_valid_json == True
        assert message == "Given JSON data is Valid"
