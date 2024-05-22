import unittest
from data_processing._data_processing_private.services.json_validator import is_json_valid


class TestJsonValidation(unittest.TestCase):

    def test_valid_json_correct_length(self):
        json_string = '{"inclusion_criterion_1": ["rationale", [1, 2, 4], "met"]}'
        result = is_json_valid(json_string, 1)
        self.assertTrue(result)

    def test_valid_json_incorrect_length(self):
        json_string = '{"inclusion_criterion_1": ["rationale", [1, 2, 4], "met"]}'
        result = is_json_valid(json_string, 2)
        self.assertFalse(result)

    def test_invalid_json(self):
        json_string = '{"inclusion_criterion_1": ["rationale", [1, 2, 4], "met"]'
        result = is_json_valid(json_string, 1)
        self.assertFalse(result)

    def test_json_incorrect_array_validation_fails(self):
        json_string = '{"inclusion_criterion_1": ["rationale", "sentence_indexes", "met"]}'
        result = is_json_valid(json_string, 1)
        self.assertFalse(result)

    def test_json_incorrect_label_validation_fails(self):
        json_string = '{"inclusion_criterion_1": ["rationale", [], "irrelevant"]}'
        result = is_json_valid(json_string, 1)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
