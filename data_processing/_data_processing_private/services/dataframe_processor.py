import pandas as pd
from data_processing._data_processing_private.data.context import create_prompt_context, create_df_input_context
from data_processing._data_processing_private.data.errors import DataFrameValidationError, dataframe_type_error, unexpected_error, MISSING_COLUMNS_ERROR
import json


def get_plain_result_dataframe():
    return pd.DataFrame(columns=['input', 'output', 'criteria_type', 'trial_criteria_total_number',
                                 'query_id', 'doc_id', 'relevance'])


def validate_input_dataframe(df_input):
    expected_columns = ['query_id', 'patient_note', 'doc_id', 'trial_title',
                        'trial_criteria', 'trial_criteria_total_number', 'trial_criteria_type', 'relevance']

    if not isinstance(df_input, pd.DataFrame):
        raise DataFrameValidationError(dataframe_type_error)

    try:
        if set(expected_columns).issubset(df_input.columns):
            return True
        else:
            missing_columns = set(expected_columns) - set(df_input.columns)
            raise DataFrameValidationError(MISSING_COLUMNS_ERROR.format(missing_columns))
    except AttributeError as e:
        raise DataFrameValidationError(dataframe_type_error) from e
    except Exception as e:
        raise DataFrameValidationError(unexpected_error) from e


def create_input_context(row):
    return create_df_input_context(
        row['patient_note'],
        row['trial_title'],
        row['trial_criteria'],
        row['trial_criteria_total_number'],
        row['trial_criteria_type'],
        row['query_id'],
        row['doc_id'],
        row['relevance']
    )


def create_user_prompt_context(input_context):
    return create_prompt_context(input_context.patient_note, input_context.trial_title,
                                 input_context.trial_criteria, input_context.trial_criteria_total_number)


def write_to_df_result(df_result, prompt, index, input_context, output):
    df_result.at[index, 'input'] = json.dumps(prompt)
    df_result.at[index, 'output'] = output
    df_result.at[index, 'criteria_type'] = input_context.trial_criteria_type
    df_result.at[index, 'trial_criteria_total_number'] = input_context.trial_criteria_total_number
    df_result.at[index, 'query_id'] = input_context.query_id
    df_result.at[index, 'doc_id'] = input_context.doc_id
    df_result.at[index, 'relevance'] = input_context.relevance
