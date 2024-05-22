import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from data_processing._data_processing_private.data import json_schemes


def is_json_valid(json_string, expected_length):

    try:
        data = json.loads(json_string)

        if len(data) != expected_length:
            return False

        validate(instance=data, schema=json_schemes.validation_json_schema)
        return True
    except (ValidationError, json.JSONDecodeError, TypeError):
        return False




