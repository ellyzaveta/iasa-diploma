from evaluation._services.visualiser import layout


class AggregateLevelEvaluation:

    def evaluate(self, df):
        incl_data_list = []
        excl_data_list = []

        percent_columns = ['met_percent', 'not_met_percent', 'no_relevant_percent']
        relevance_labels = ['no relevant', 'excluded', 'eligible']

        for percent in percent_columns:
            incl_data = {}
            excl_data = {}

            for label, relevance in zip(relevance_labels, range(3)):
                incl_data[label] = df[(df["relevance"] == relevance) &
                                      (df["criteria_type"] == "inclusion")][percent]
                excl_data[label] = df[(df["relevance"] == relevance) &
                                      (df["criteria_type"] == "exclusion")][percent]

            incl_data_list.append(incl_data)
            excl_data_list.append(excl_data)

        layout(incl_data_list, "Inclusion")

        excl_data_list = [excl_data_list[1], excl_data_list[0], excl_data_list[2]]
        layout(excl_data_list, "Exclusion")





