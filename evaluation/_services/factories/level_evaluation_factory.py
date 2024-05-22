from evaluation._services.factories.evaluation_strategies.explanation_level import ExplanationLevelStrategy
from evaluation._services.factories.evaluation_strategies.index_level import SentenceIndexLevelStrategy
from evaluation._services.factories.evaluation_strategies.label_level import LabelLevelStrategy


class LevelEvaluationFactorySelector:

    factory_map = {
        'label': LabelLevelStrategy(),
        'index': SentenceIndexLevelStrategy(),
        'explanation': ExplanationLevelStrategy(),
    }

    @staticmethod
    def get_factory(factory_type):
        return LevelEvaluationFactorySelector.factory_map.get(factory_type, None)


class LabelLevelEvaluationFactory:

    def __init__(self):
        self.factory = LevelEvaluationFactorySelector().get_factory('label')

    def evaluate(self, validation_context, input_context):
        return self.factory.evaluate(validation_context, input_context)


class IndexLevelEvaluationFactory:

    def __init__(self):
        self.factory = LevelEvaluationFactorySelector().get_factory('index')

    def evaluate(self, validation_context, input_context):
        return self.factory.evaluate(validation_context, input_context)


class ExplanationLevelEvaluationFactory:

    def __init__(self):
        self.factory = LevelEvaluationFactorySelector().get_factory('explanation')

    def evaluate(self, validation_context, input_context):
        return self.factory.evaluate(validation_context, input_context)
