from evaluation._services.factories.split_strategies.split_strategies import CriterionLevelSplitStrategy, \
    AggregateLevelSplitStrategy


class SplitFactorySelector:
    factory_map = {
        'criterion-level': CriterionLevelSplitStrategy(),
        'aggregate-level': AggregateLevelSplitStrategy(),
    }

    @staticmethod
    def get_factory(factory_type):
        return SplitFactorySelector.factory_map.get(factory_type, None)


class CriterionLevelSplit:

    def __init__(self):
        self.factory = SplitFactorySelector().get_factory('criterion-level')

    def split(self, df, df_base):
        return self.factory.split(df, df_base)


class AggregateLevelSplit:

    def __init__(self):
        self.factory = SplitFactorySelector().get_factory('aggregate-level')

    def split(self, df, df_base):
        return self.factory.split(df, df_base)

