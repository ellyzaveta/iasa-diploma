from data_processing._data_processing_private.services.factories.prompt_factory import PromptFactory
from data_processing._data_processing_private.data.context import create_GPT_context, create_params_context, create_report_context
from data_processing._data_processing_private.services.openai_client import OpenAI_Client
from data_processing._data_processing_private.services.json_validator import is_json_valid
from data_processing._data_processing_private.data.errors import DataFrameValidationError
from data_processing._data_processing_private.data.json_schemes import empty_json
import data_processing._data_processing_private.services.dataframe_processor as dps
import data_processing._data_processing_private.utils.timer as tmr
import data_processing._data_processing_private.services.performance_report_generator as rv


class DataProcessor:

    def __init__(self, model):
        self._model = model
        self._openai_client = OpenAI_Client()
        self._timer = None
        self._total_iteration_num = None
        self._time_tracking = None
        self._attempt_tracking = None
        self._total_attempts_per_request = None

    def _init(self, total_attempts_per_request):
        self._total_attempts_per_request = total_attempts_per_request
        self._attempt_tracking = []
        self._time_tracking = []
        self._total_iteration_num = 0
        self._timer = tmr.Timer()

    def _send_requests(self, params):
        gpt_context = create_GPT_context(self._model, params.messages)
        total_attempts_number = self._total_attempts_per_request

        while True:
            total_attempts_number -= 1
            result = self._openai_client.get_response(gpt_context)

            if is_json_valid(result, params.expected_json_length):
                return result, self._total_attempts_per_request - total_attempts_number
            if total_attempts_number == 0:
                return empty_json, self._total_attempts_per_request - total_attempts_number

    def _get_result(self, params):

        self._timer.evaluate_sentences()

        result, attempts = self._send_requests(params)

        self._attempt_tracking.append(attempts)
        self._time_tracking.append(self._timer.end())

        return result

    def _get_performance_report(self):

        report_context = create_report_context(self._model,
                                               self._time_tracking,
                                               self._attempt_tracking,
                                               self._total_iteration_num)

        rv.print_report(report_context)

    def process(self, df_input, output_filepath="result.csv", total_attempts_per_request=5):

        try:
            dps.validate_input_dataframe(df_input)
        except DataFrameValidationError:
            raise

        self._init(total_attempts_per_request)

        df_result = dps.get_plain_result_dataframe()

        for index, row in df_input.iterrows():
            input_context = dps.create_input_context(row)
            user_prompt_context = dps.create_user_prompt_context(input_context)

            criteria_prompt_creator = (PromptFactory()
                                       .get_prompt_creator(input_context.trial_criteria_type))

            prompt = criteria_prompt_creator.create(user_prompt_context)

            params = create_params_context(prompt,
                                           input_context.trial_criteria_total_number)

            output = self._get_result(params)

            dps.write_to_df_result(df_result,
                                   prompt,
                                   index,
                                   input_context,
                                   output)

            df_result.to_csv(output_filepath)

            rv.print_current_iteration(self._total_iteration_num)

            self._total_iteration_num += 1

        self._get_performance_report()

        return df_result


