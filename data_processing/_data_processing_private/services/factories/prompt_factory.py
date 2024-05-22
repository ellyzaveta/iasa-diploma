from data_processing._data_processing_private.data import prompts
from abc import ABC, abstractmethod


class Prompt(ABC):

    @abstractmethod
    def create(self, context):
        pass


def _generate_message(system_prompt, user_prompt):

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": prompts.ASSISTANT_PROMPT}
    ]

    return messages


class InclusionCriteriaPrompt(Prompt):

    def create(self, context):

        user_input = prompts.PROMPT_INCLUSION_CRITERIA.format(
            context.patient_note, context.trial_title,
            context.trial_criteria, context.trial_criteria_total_number)

        return _generate_message(prompts.INCL_SYSTEM_PROMPT, user_input)


class ExclusionCriteriaPrompt(Prompt):

    def create(self, context):

        user_input = prompts.PROMPT_EXCLUSION_CRITERIA.format(
            context.patient_note, context.trial_title,
            context.trial_criteria, context.trial_criteria_total_number)

        return _generate_message(prompts.EXCL_SYSTEM_PROMPT, user_input)


class PromptFactory:

    factory_map = {
        'inclusion': InclusionCriteriaPrompt(),
        'exclusion': ExclusionCriteriaPrompt()
    }

    @staticmethod
    def get_prompt_creator(criteria_type):

        return PromptFactory.factory_map.get(criteria_type, None)





