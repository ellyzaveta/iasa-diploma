import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

from data_processing._data_processing_private.data.context import GPTContext
from data_processing._data_processing_private.data.errors import value_error


class OpenAI_Client:

    def __init__(self):

        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        if api_key is not None:
            OpenAI.api_key = api_key
            self._client = OpenAI()
        else:
            raise ValueError(value_error)

    def get_response(self, context):

        try:
            response = self._client.chat.completions.create(
                model=context.model,
                messages=context.messages
            )

            response_content = response.choices[0].message.content
            return response_content.strip()

        except OpenAIError:
            return None
