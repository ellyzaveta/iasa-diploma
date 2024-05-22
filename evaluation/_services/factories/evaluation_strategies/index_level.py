from evaluation._data.contexts import create_DF_context, create_metrics_context, create_metrics_per_category_context
from evaluation._services.factories.evaluation_strategies.level_strategy import LevelStrategy
from evaluation._services.factories.score_factory import OverallScoresFactory, InclusionOverallScoresFactory, \
    ExclusionOverallScoresFactory, InclusionAccuracyScorePerCategoryFactory, ExclusionAccuracyScorePerCategoryFactory
from evaluation._services.visualiser import metrics_report
from evaluation._services.factories.evaluation_strategies.utils.metrics_calculator import (accuracy_score,
                                                                                           precision_score,
                                                                                           recall_score,
                                                                                           f1_score)
from styles.colors import green_color_list


class SentenceIndexLevelStrategy(LevelStrategy):

    def evaluate(self, validation_context, contexts):

        print("Sentence index level evaluation")

        scores_dict = {}
        scores_dict_incl = {}
        scores_dict_excl = {}
        scores_dict_incl_per_category = {}
        scores_dict_excl_per_category = {}

        function_context = create_metrics_context(accuracy_score, precision_score, recall_score, f1_score,
                                                  "relevant sentence indexes")

        function_context_per_category = create_metrics_per_category_context(accuracy_score, "relevant sentence indexes")

        for context in contexts:
            valid_match_indexes = validation_context.dataframe['label'] == context.dataframe['label']

            df_valid_context = create_DF_context("validation", validation_context.dataframe[valid_match_indexes])

            new_context = create_DF_context(context.model_name, context.dataframe[valid_match_indexes])

            contexts_list = [new_context]

            factory = OverallScoresFactory()
            scores_overall = factory.get_report(df_valid_context, contexts_list, function_context)
            scores_dict[context.model_name] = scores_overall[context.model_name]

            factory = InclusionOverallScoresFactory()
            scores_incl = factory.get_report(df_valid_context, contexts_list, function_context)
            scores_dict_incl[context.model_name] = scores_incl[context.model_name]

            factory = ExclusionOverallScoresFactory()
            scores_excl = factory.get_report(df_valid_context, contexts_list, function_context)
            scores_dict_excl[context.model_name] = scores_excl[context.model_name]

            factory = InclusionAccuracyScorePerCategoryFactory()
            scores_incl_per_category = factory.get_report(df_valid_context, contexts_list, function_context_per_category)
            scores_dict_incl_per_category[context.model_name] =  scores_incl_per_category[context.model_name]

            factory = ExclusionAccuracyScorePerCategoryFactory()
            scores_excl_per_category = factory.get_report(df_valid_context, contexts_list, function_context_per_category)
            scores_dict_excl_per_category[context.model_name] = scores_excl_per_category[context.model_name]

        metrics_report("Overall evaluation metrics", scores_dict, colors=green_color_list)
        metrics_report("Evaluation metrics (Inclusion criteria)", scores_dict_incl, colors=green_color_list)
        metrics_report("Evaluation metrics (Exclusion criteria)", scores_dict_excl, colors=green_color_list)
        metrics_report("Accuracy score per category (Inclusion criteria)", scores_dict_incl_per_category, colors=green_color_list)
        metrics_report("Accuracy score per category (Exclusion criteria)", scores_dict_excl_per_category, colors=green_color_list)

