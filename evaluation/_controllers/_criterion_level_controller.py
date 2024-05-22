import pandas as pd

from evaluation._data.contexts import create_DF_context
from evaluation._services.factories.level_evaluation_factory import LabelLevelEvaluationFactory, \
    IndexLevelEvaluationFactory, ExplanationLevelEvaluationFactory
from evaluation._services.factories.split_factory import CriterionLevelSplit


class CriterionLevelController:

    def __init__(self, filepath_context):

        self.evaluator = None

        df_base = pd.read_csv(filepath_context.base_file)
        df_valid = pd.read_csv(filepath_context.valid_file)

        splitter = CriterionLevelSplit()

        df_valid_split = splitter.split(df_valid, df_base)
        self.valid_context = create_DF_context("validation", df_valid_split)

        self.contexts = []

        for file in filepath_context.test_files:
            df = pd.read_csv(file['filepath'])
            df_split = splitter.split(df, df_base)

            name = file['model_name']

            context = create_DF_context(name, df_split)
            self.contexts.append(context)

    def evaluate_label(self):
        self.evaluator = LabelLevelEvaluationFactory()
        self.evaluator.evaluate(self.valid_context, self.contexts)

    def evaluate_sentence_index(self):
        self.evaluator = IndexLevelEvaluationFactory()
        self.evaluator.evaluate(self.valid_context, self.contexts)

    def evaluate_explanation(self):
        self.evaluator = ExplanationLevelEvaluationFactory()
        self.evaluator.evaluate(self.valid_context, self.contexts[::-1])