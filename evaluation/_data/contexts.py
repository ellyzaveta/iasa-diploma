class DFContext:
    def __init__(self, model_name, dataframe):
        self.model_name = model_name
        self.dataframe = dataframe


class InputContext:
    def __init__(self, model_name, filepath):
        self.model_name = model_name
        self.filepath = filepath


class FilePathContext:
    def __init__(self, base_file, valid_file, test_files):
        self.base_file = base_file
        self.valid_file = valid_file
        self.test_files = test_files


class MetricsContext:
    def __init__(self, accuracy_score, precision_score, recall_score, f1_score, column):
        self.accuracy_score = accuracy_score
        self.precision_score = precision_score
        self.recall_score = recall_score
        self.f1_score = f1_score
        self.column = column


class MetricsPerCategoryContext:
    def __init__(self, accuracy_score, column):
        self.accuracy_score = accuracy_score
        self.column = column


def create_input_context(model_name, filepath):
    return InputContext(
        model_name=model_name,
        filepath=filepath,
    )

def create_filepath_context(base_file, valid_file, test_files):
    return FilePathContext(
        base_file=base_file,
        valid_file=valid_file,
        test_files=test_files
    )


def create_DF_context(model_name, dataframe):
    return DFContext(
        model_name=model_name,
        dataframe=dataframe,
    )


def create_metrics_per_category_context(accuracy_score, column):
    return MetricsPerCategoryContext(
        accuracy_score=accuracy_score,
        column=column,
    )


def create_metrics_context(accuracy_score, precision_score, recall_score, f1_score, column):
    return MetricsContext(
        accuracy_score=accuracy_score,
        precision_score=precision_score,
        recall_score=recall_score,
        f1_score=f1_score,
        column=column
    )


