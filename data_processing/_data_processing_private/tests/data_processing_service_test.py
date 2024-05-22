import unittest
import pandas as pd
from data_processing._data_processing_private.services.dataframe_processor import get_plain_result_dataframe, validate_input_dataframe, DataFrameValidationError


class DataProcessingService(unittest.TestCase):

    def test_get_plain_result_dataframe(self):
        df = get_plain_result_dataframe()
        expected_columns = ['input', 'output', 'criteria_type', 'total_criteria_number',
                            'query_id', 'doc_id', 'relevance']

        self.assertEqual(list(df.columns), expected_columns)
        self.assertTrue(df.empty)

    def test_validate_input_dataframe_correct(self):
        data = {
            'query_id': [1],
            'patient_note': ['note'],
            'doc_id': [1],
            'title_title': ['title'],
            'trial_criteria': ['criteria'],
            'trial_criteria_total_number': [1],
            'trial_criteria_type': ['type'],
            'relevance': [1]
        }

        df_input = pd.DataFrame(data)
        self.assertTrue(validate_input_dataframe(df_input))

    def test_validate_input_dataframe_missing_columns(self):
        data = {
            'query_id': [1],
            'patient_note': ['note'],
            'doc_id': [1]
        }

        df_input = pd.DataFrame(data)

        with self.assertRaises(DataFrameValidationError):
            validate_input_dataframe(df_input)

    def test_validate_input_dataframe_attribute_error(self):
        df_input = "not_a_dataframe"

        with self.assertRaises(DataFrameValidationError):
            validate_input_dataframe(df_input)


if __name__ == '__main__':
    unittest.main()
