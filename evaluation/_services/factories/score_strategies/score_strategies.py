from abc import ABC, abstractmethod
from evaluation._data.contexts import create_DF_context
from evaluation._services.factories.score_strategies.utils.score_calculator import get_scores, \
    get_accuracy_score_per_category


class ScoreStrategy(ABC):

    @abstractmethod
    def get_report(self, validation_context, input_context, function_context):
        pass


class OverallScoresStrategy(ScoreStrategy):

    def get_report(self, validation_context, input_context, function_context):
        scores_overall = {}

        for context in input_context:
            scores_overall[context.model_name] = get_scores(validation_context, context, function_context)

        return scores_overall


class InclusionOverallScoresStrategy(ScoreStrategy):

    def get_report(self, validation_context, input_context, function_context):
        scores_overall = {}

        validation_dataframe = validation_context.dataframe
        filtered_dataframe = validation_dataframe[validation_dataframe['criterion type'] == "inclusion"]

        valid_context = create_DF_context("validation", filtered_dataframe)

        for context in input_context:
            context_dataframe = context.dataframe
            filtered_input = context_dataframe[context_dataframe['criterion type'] == "inclusion"]
            new_context = create_DF_context(context.model_name, filtered_input)

            scores_overall[context.model_name] = get_scores(valid_context, new_context, function_context)

        return scores_overall


class InclusionAccuracyScorePerCategoryStrategy(ScoreStrategy):

    def get_report(self, validation_context, input_context, function_context):
        scores_overall = {}

        validation_dataframe = validation_context.dataframe
        filtered_dataframe = validation_dataframe[validation_dataframe['criterion type'] == "inclusion"]

        valid_context = create_DF_context("validation", filtered_dataframe)

        for context in input_context:
            context_dataframe = context.dataframe
            filtered_input = context_dataframe[context_dataframe['criterion type'] == "inclusion"]
            new_context = create_DF_context(context.model_name, filtered_input)

            scores_overall[context.model_name] = get_accuracy_score_per_category(valid_context, new_context, function_context)

        return scores_overall


class ExclusionOverallScoresStrategy(ScoreStrategy):

    def get_report(self, validation_context, input_context, function_context):
        scores_overall = {}

        validation_dataframe = validation_context.dataframe
        filtered_dataframe = validation_dataframe[validation_dataframe['criterion type'] == "exclusion"]

        valid_context = create_DF_context("validation", filtered_dataframe)

        for context in input_context:
            context_dataframe = context.dataframe
            filtered_input = context_dataframe[context_dataframe['criterion type'] == "exclusion"]

            new_context = create_DF_context(context.model_name, filtered_input)

            scores_overall[context.model_name] = get_scores(valid_context, new_context, function_context)

        return scores_overall


class ExclusionAccuracyScorePerCategoryStrategy(ScoreStrategy):

    def get_report(self, validation_context, input_context, function_context):
        scores_overall = {}

        validation_dataframe = validation_context.dataframe
        filtered_dataframe = validation_dataframe[validation_dataframe['criterion type'] == "exclusion"]

        valid_context = create_DF_context("validation", filtered_dataframe)

        for context in input_context:
            context_dataframe = context.dataframe
            filtered_input = context_dataframe[context_dataframe['criterion type'] == "exclusion"]

            new_context = create_DF_context(context.model_name, filtered_input)

            scores_overall[context.model_name] = get_accuracy_score_per_category(valid_context, new_context, function_context)

        return scores_overall