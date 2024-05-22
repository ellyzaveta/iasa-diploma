import unittest
from unittest.mock import patch
from data_processing._data_processing_private.services.openai_client import OpenAI_Client

class TestOpenAI_Client(unittest.TestCase):

    @patch('utils.openai_client.os.getenv')
    def test_value_error_on_missing_api_key(self, mock_getenv):

        mock_getenv.return_value = None

        with self.assertRaises(ValueError):
            instance = OpenAI_Client()


if __name__ == '__main__':
    unittest.main()