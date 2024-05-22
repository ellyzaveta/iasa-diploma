import unittest
from unittest.mock import MagicMock, patch
from data_processing.patient_trial_match import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def setUp(self):

        self.mock_model = MagicMock()
        self.data_processor = DataProcessor(self.mock_model)

        self.data_processor._openai_client = MagicMock()
        self.data_processor._timer = MagicMock()
        self.data_processor._timer.start.return_value = None
        self.data_processor._timer.end.return_value = 10

    def test_init(self):
        self.data_processor._init(total_attempts_per_request=3)
        self.assertEqual(self.data_processor._total_attempts_per_request, 3)
        self.assertIsInstance(self.data_processor._attempt_tracking, list)
        self.assertIsInstance(self.data_processor._time_tracking, list)
        self.assertEqual(self.data_processor._total_iteration_num, 0)

    @patch('utils.contexts.contexts.create_GPT_context')
    @patch('utils.json_validator.is_json_valid')
    def test_send_request(self, mock_is_json_valid, mock_create_GPT_context):
        mock_create_GPT_context.return_value = 'mock_context'
        mock_is_json_valid.side_effect = [False, False, True]
        self.data_processor._openai_client.get_response.return_value = 'valid_json'

        params = MagicMock()
        params.messages = ["Hello", "World"]
        params.expected_json_length = 5
        result, attempts = self.data_processor._send_requests(params)

        self.assertEqual(result, 'valid_json')
        self.assertEqual(attempts, 3)
        mock_is_json_valid.assert_called_with('valid_json', 5)

    @patch('controller.data_processing_service')
    def test_process(self, mock_dps):
        # Prepare the dataframe and mocks
        df_input = MagicMock()
        df_input.iterrows.return_value = iter([(0, 'row1'), (1, 'row2')])
        mock_dps.validate_input_dataframe.return_value = None
        mock_dps.get_plain_result_dataframe.return_value = MagicMock()

        # Testing the process method
        with patch.object(self.data_processor, '_send_request') as mock_send_request, \
             patch.object(self.data_processor, '_print_performance_report') as mock_print_report:
            mock_send_request.return_value = ('output', 1)
            result = self.data_processor.process(df_input)

            # Check that the report and _data frame manipulations are as expected
            mock_dps.write_to_df_result.assert_called()
            mock_print_report.assert_called_once()
            self.assertIsInstance(result, MagicMock)

if __name__ == '__main__':
    unittest.main()
