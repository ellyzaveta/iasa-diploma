from abc import ABC, abstractmethod


class LevelStrategy(ABC):

    @abstractmethod
    def evaluate(self, validation_context, input_context_list):
        pass