import pandas as pd
import json


def count_criteria_status(input_data):
    data = json.loads(input_data)

    counters = {
        "met": 0,
        "not met": 0,
        "no relevant information": 0
    }

    for key, value in data.items():
        status = value[2]
        if status in counters:
            counters[status] += 1

    total = sum(counters.values())
    if total != 0:
        for key in counters:
            counters[key] = round(counters[key] / total, 3)

    return counters["met"], counters["not met"], counters["no relevant information"]


def criterion_level_split(df, df_base):
    rows = []

    for index, row in df.iterrows():

        json_string = row['output']
        item = json.loads(json_string)

        criterion_text = df_base.iloc[index, 4]
        criterion_type = df_base.iloc[index, 6]

        criteria = criterion_text.split('\n\n')

        criteria_index = 0

        for criterion, details in item.items():
            new_row = {
                'criterion type': criterion_type,
                'criterion': criterion,
                'criterion description': criteria[criteria_index],
                'relevance explanation': details[0],
                'relevant sentence indexes': details[1],
                'label': details[2],
            }

            criteria_index += 1

            rows.append(new_row)

    return pd.DataFrame(rows)


def aggregate_level_split(df):

    df_percent = pd.DataFrame()

    df_percent['met_percent'], df_percent['not_met_percent'], df_percent['no_relevant_percent'], = zip(
        *df['output'].apply(count_criteria_status))

    df_percent['relevance'] = df['relevance']
    df_percent['criteria_type'] = df['criteria_type']

    return df_percent

