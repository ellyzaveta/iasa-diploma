from abc import ABC, abstractmethod

from evaluation._services.factories.split_strategies.utils.split_methods import criterion_level_split, \
    aggregate_level_split


class SplitStrategy(ABC):

    @abstractmethod
    def split(self, df, df_base):
        pass


class CriterionLevelSplitStrategy(SplitStrategy):

    def split(self, df, df_base):
        return criterion_level_split(df, df_base)


class AggregateLevelSplitStrategy(SplitStrategy):

    def split(self, df, df_base):
        return aggregate_level_split(df)
