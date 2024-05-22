validation_json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "patternProperties": {
        ".*": {
            "type": "array",
            "items": [
                {"type": "string"},
                {"type": "array", "items": {"type": "integer"}},
                {"type": "string", "enum": ["met", "not met", "no relevant information"]}
            ]
        }
    },
    "additionalProperties": False
}

empty_json = "{}"
