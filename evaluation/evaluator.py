from evaluation._controllers._aggregate_level_controller import AggregateLevelController
from evaluation._controllers._criterion_level_controller import CriterionLevelController
from evaluation._data.contexts import create_filepath_context


class Evaluator:

    def __init__(self, base_filepath, valid_filepath, for_evaluation_filepath_list):
        filepath_context = create_filepath_context(base_filepath, valid_filepath, for_evaluation_filepath_list)
        self.criterion_level = CriterionLevelController(filepath_context)
        self.aggregate_level = AggregateLevelController(for_evaluation_filepath_list[0]['filepath'])

    def get_criterion_level_label_report(self):
        self.criterion_level.evaluate_label()

    def get_criterion_level_sentence_index_report(self):
        self.criterion_level.evaluate_sentence_index()

    def get_criterion_level_explanation_report(self):
        self.criterion_level.evaluate_explanation()

    def get_aggregate_level_report(self):
        self.aggregate_level.evaluate_aggregate()


