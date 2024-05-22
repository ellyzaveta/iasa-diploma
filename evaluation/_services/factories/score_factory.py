from evaluation._services.factories.score_strategies.score_strategies import OverallScoresStrategy, \
    InclusionOverallScoresStrategy, ExclusionOverallScoresStrategy, InclusionAccuracyScorePerCategoryStrategy, \
    ExclusionAccuracyScorePerCategoryStrategy


class ScoreFactorySelector:
    factory_map = {
        'overall': OverallScoresStrategy(),
        'inclusion': InclusionOverallScoresStrategy(),
        'exclusion': ExclusionOverallScoresStrategy(),
        'inclusion per category': InclusionAccuracyScorePerCategoryStrategy(),
        'exclusion per category': ExclusionAccuracyScorePerCategoryStrategy(),
    }

    @staticmethod
    def get_factory(factory_type):
        return ScoreFactorySelector.factory_map.get(factory_type, None)


class OverallScoresFactory:

    def __init__(self):
        self.factory = ScoreFactorySelector().get_factory('overall')

    def get_report(self, validation_context, input_context, function_context):
        return self.factory.get_report(validation_context, input_context, function_context)


class InclusionOverallScoresFactory:

    def __init__(self):
        self.factory = ScoreFactorySelector().get_factory('inclusion')

    def get_report(self, validation_context, input_context, function_context):
        return self.factory.get_report(validation_context, input_context, function_context)


class InclusionAccuracyScorePerCategoryFactory:

    def __init__(self):
        self.factory = ScoreFactorySelector().get_factory('inclusion per category')

    def get_report(self, validation_context, input_context, function_context):
        return self.factory.get_report(validation_context, input_context, function_context)


class ExclusionOverallScoresFactory:

    def __init__(self):
        self.factory = ScoreFactorySelector().get_factory('exclusion')

    def get_report(self, validation_context, input_context, function_context):
        return self.factory.get_report(validation_context, input_context, function_context)


class ExclusionAccuracyScorePerCategoryFactory:

    def __init__(self):
        self.factory = ScoreFactorySelector().get_factory('exclusion per category')

    def get_report(self, validation_context, input_context, function_context):
        return self.factory.get_report(validation_context, input_context, function_context)