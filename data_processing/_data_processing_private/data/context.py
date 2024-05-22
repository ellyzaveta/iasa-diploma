class ParamsContext:
    def __init__(self, messages, expected_json_length):
        self.messages = messages
        self.expected_json_length = expected_json_length


class PromptContext:
    def __init__(self, patient_note, trial_title, trial_criteria, trial_criteria_total_number):
        self.patient_note = patient_note
        self.trial_title = trial_title
        self.trial_criteria = trial_criteria
        self.trial_criteria_total_number = trial_criteria_total_number


class GPTContext:
    def __init__(self, model, messages):
        self.model = model
        self.messages = messages


class DFInputContext:
    def __init__(self, patient_note, trial_title, trial_criteria, trial_criteria_total_number,
                 trial_criteria_type, query_id, doc_id, relevance):
        self.patient_note = patient_note
        self.trial_title = trial_title
        self.trial_criteria = trial_criteria
        self.trial_criteria_total_number = trial_criteria_total_number
        self.trial_criteria_type = trial_criteria_type
        self.query_id = query_id
        self.doc_id = doc_id
        self.relevance = relevance


class ReportContext:
    def __init__(self, model, time_tracking, attempt_tracking, total_iteration_num):
        self.model = model
        self.time_tracking = time_tracking
        self.attempt_tracking = attempt_tracking
        self.total_iteration_num = total_iteration_num


def create_report_context(model, time_tracking, attempt_tracking, total_iteration_num):
    return ReportContext(
        model=model,
        time_tracking=time_tracking,
        attempt_tracking=attempt_tracking,
        total_iteration_num=total_iteration_num,
    )


def create_df_input_context(patient_note, trial_title, trial_criteria, trial_criteria_total_number,
                            trial_criteria_type, query_id, doc_id, relevance):
    return DFInputContext(
        patient_note=patient_note,
        trial_title=trial_title,
        trial_criteria=trial_criteria,
        trial_criteria_total_number=trial_criteria_total_number,
        trial_criteria_type=trial_criteria_type,
        query_id=query_id,
        doc_id=doc_id,
        relevance=relevance,
    )


def create_prompt_context(patient_note, trial_title, trial_criteria, trial_criteria_total_number):
    return PromptContext(
        patient_note=patient_note,
        trial_title=trial_title,
        trial_criteria=trial_criteria,
        trial_criteria_total_number=trial_criteria_total_number
    )


def create_GPT_context(model, messages):
    return GPTContext(
        model=model,
        messages=messages
    )


def create_params_context(messages, expected_json_length):
    return ParamsContext(
        messages=messages,
        expected_json_length=expected_json_length
    )
