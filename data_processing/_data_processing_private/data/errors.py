value_error = "API key must be set in the environment variables."

dataframe_type_error = "Invalid input: Expected a pandas DataFrame."

unexpected_error = "An unexpected error occurred."

MISSING_COLUMNS_ERROR = "Required columns {} missed."


class DataFrameValidationError(Exception):
    """Exception raised for errors in the input DataFrame validation process."""
    def __init__(self, message):
        super().__init__(message)