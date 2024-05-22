import pandas as pd

from evaluation._services.factories.evaluation_strategies.aggregate_level import AggregateLevelEvaluation
from evaluation._services.factories.split_factory import AggregateLevelSplit


class AggregateLevelController:

    def __init__(self, filepath):

        df = pd.read_csv(filepath)
        splitter = AggregateLevelSplit()

        self.df_percent = splitter.split(df, df)

        self.evaluator = None

    def evaluate_aggregate(self):
        self.evaluator = AggregateLevelEvaluation()
        self.evaluator.evaluate(self.df_percent)