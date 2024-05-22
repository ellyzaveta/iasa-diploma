import unittest

from data_processing._data_processing_private.services.factories.prompt_factory import PromptFactory

from data_processing._data_processing_private.data.context import create_prompt_context
from data_processing._data_processing_private.data.prompts import INCL_SYSTEM_PROMPT, PROMPT_INCLUSION_CRITERIA, ASSISTANT_PROMPT,EXCL_SYSTEM_PROMPT, PROMPT_EXCLUSION_CRITERIA


class TestPromptFactories(unittest.TestCase):
    def setUp(self):
        self.context = create_prompt_context(
            patient_note='patient note',
            trial_title='trial title',
            trial_criteria='trial criteria',
            trial_criteria_total_number=5
        )

    def test_inclusion_criteria_prompt(self):

        factory = PromptFactory.get_prompt_creator('inclusion')

        result = factory.create(self.context)

        expected_user_prompt = PROMPT_INCLUSION_CRITERIA.format(
            self.context.patient_note, self.context.trial_title,
            self.context.trial_criteria, self.context.trial_criteria_total_number)

        expected_messages = [
            {"role": "system", "content": INCL_SYSTEM_PROMPT},
            {"role": "user", "content": expected_user_prompt},
            {"role": "assistant", "content": ASSISTANT_PROMPT}
        ]

        self.assertEqual(result, expected_messages)

    def test_exclusion_criteria_prompt(self):

        factory = PromptFactory.get_prompt_creator('exclusion')

        result = factory.create(self.context)

        expected_user_prompt = PROMPT_EXCLUSION_CRITERIA.format(
            self.context.patient_note, self.context.trial_title,
            self.context.trial_criteria, self.context.trial_criteria_total_number)

        expected_messages = [
            {"role": "system", "content": EXCL_SYSTEM_PROMPT},
            {"role": "user", "content": expected_user_prompt},
            {"role": "assistant", "content": ASSISTANT_PROMPT}
        ]

        self.assertEqual(result, expected_messages)


if __name__ == '__main__':
    unittest.main()