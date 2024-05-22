from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from evaluation._data.contexts import create_metrics_context, create_metrics_per_category_context
from evaluation._services.factories.evaluation_strategies.level_strategy import LevelStrategy
from evaluation._services.factories.score_factory import OverallScoresFactory, InclusionOverallScoresFactory, \
    ExclusionOverallScoresFactory, InclusionAccuracyScorePerCategoryFactory, ExclusionAccuracyScorePerCategoryFactory
from evaluation._services.visualiser import metrics_report
from styles.colors import purple_color_list


class LabelLevelStrategy(LevelStrategy):

    def evaluate(self, validation_context, contexts):

        print("Label level evaluation")

        function_context = create_metrics_context(accuracy_score, precision_score, recall_score, f1_score, "label")
        function_context_per_category = create_metrics_per_category_context(accuracy_score, "label")

        factory = OverallScoresFactory()
        scores_overall = factory.get_report(validation_context, contexts, function_context)
        metrics_report("Overall evaluation metrics", scores_overall, colors=purple_color_list)

        factory = InclusionOverallScoresFactory()
        scores_overall = factory.get_report(validation_context, contexts, function_context)
        metrics_report("Evaluation metrics (Inclusion criteria)", scores_overall, colors=purple_color_list)

        factory = ExclusionOverallScoresFactory()
        scores_overall = factory.get_report(validation_context, contexts, function_context)
        metrics_report("Evaluation metrics (Exclusion criteria)", scores_overall, colors=purple_color_list)

        factory = InclusionAccuracyScorePerCategoryFactory()
        scores_overall = factory.get_report(validation_context, contexts, function_context_per_category)
        metrics_report("Accuracy score per category (Inclusion criteria)", scores_overall, colors=purple_color_list)

        factory = ExclusionAccuracyScorePerCategoryFactory()
        scores_overall = factory.get_report(validation_context, contexts, function_context_per_category)
        metrics_report("Accuracy score per category (Exclusion criteria)", scores_overall, colors=purple_color_list)






