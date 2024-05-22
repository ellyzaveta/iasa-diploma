
def get_accuracy_score_per_category(validation_context, context, function_context):

    valid_df = validation_context.dataframe

    valid_df_met = valid_df[valid_df['label'] == "met"]
    valid_df_not_met = valid_df[valid_df['label'] == "not met"]
    valid_df_no_relevant = valid_df[valid_df['label'] == "no relevant information"]

    indexes_met = valid_df_met.index
    indexes_not_met = valid_df_not_met.index
    indexes_no_relevant = valid_df_no_relevant.index

    df = context.dataframe

    df_met = df.loc[indexes_met]
    df_not_met = df.loc[indexes_not_met]
    df_no_relevant = df.loc[indexes_no_relevant]

    return {
        'met': function_context.accuracy_score(valid_df_met[function_context.column],
                                               df_met[function_context.column]),

        'not met': function_context.accuracy_score(valid_df_not_met[function_context.column],
                                                   df_not_met[function_context.column]),

        'no relevant information': function_context.accuracy_score(valid_df_no_relevant[function_context.column],
                                                                   df_no_relevant[function_context.column]),

    }


def get_scores(validation_context, context, function_context):
    return {
        'accuracy': function_context.accuracy_score(validation_context.dataframe[function_context.column],
                                                    context.dataframe[function_context.column]),

        'precision': function_context.precision_score(validation_context.dataframe[function_context.column],
                                                      context.dataframe[function_context.column], average='macro'),

        'recall': function_context.recall_score(validation_context.dataframe[function_context.column],
                                                context.dataframe[function_context.column], average='macro'),

        'F1': function_context.f1_score(validation_context.dataframe[function_context.column],
                                        context.dataframe[function_context.column], average='macro')
    }