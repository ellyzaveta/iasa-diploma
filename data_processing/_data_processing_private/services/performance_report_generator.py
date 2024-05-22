import matplotlib.pyplot as plt
from IPython.display import clear_output
import matplotlib as mpl
import data_processing._data_processing_private.data.style as style

mpl.rcParams.update(mpl.rcParamsDefault)
plt.style.use(style.plt_style)

mpl.rcParams['font.size'] = style.plt_font_size
mpl.rcParams['font.family'] = style.plt_font_style


def print_current_iteration(iteration_num):
    clear_output(wait=True)
    print("iteration: ", iteration_num)


def print_report(report_context):
    total_time = sum(report_context.time_tracking)
    total_attempts = sum(report_context.attempt_tracking)

    print("\nmodel: ", report_context.model)

    print("\ntotal number of instances: ", report_context.total_iteration_num)

    print("\ntotal time (seconds): ", round(total_time, 3))
    print("total time (minutes): ", round(total_time / 60, 3))
    print("total attempts number: ", total_attempts)

    print("\naverage number of attempts per iteration: ",
          round(total_attempts / report_context.total_iteration_num, 3))
    print("average time per iteration (s): ",
          round(total_time / report_context.total_iteration_num, 3))

    print("\n\n\n")

    _show_attempts_pie_chart(report_context.attempt_tracking)
    _show_time_pie_chart(report_context.time_tracking)


def _show_attempts_pie_chart(attempts):

    counts = {
        '1 attempt': sum(1 for attempt in attempts if attempt == 1),
        '2-3 attempts': sum(1 for attempt in attempts if 2 <= attempt <= 3),
        '4-5 attempts': sum(1 for attempt in attempts if attempt > 3)
    }

    filtered_counts = {category: count for category, count in counts.items() if count > 0}

    total = sum(filtered_counts.values())

    percentages = [count / total * 100 for count in filtered_counts.values()]

    colors = [style.green, style.orange, style.red]

    plt.figure(figsize=(5, 5))
    wedges, texts, autotexts = plt.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors,
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 1})

    plt.title('Attempts per iteration distribution')

    plt.legend(wedges, counts.keys(), loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.show()


def _show_time_pie_chart(times):

    counts = {
        '2s  <  t': sum(1 for time in times if time < 2.0),
        '2s  <= t < 5s': sum(1 for time in times if 2.0 <= time < 5.0),
        '5s  <= t < 10s': sum(1 for time in times if 5.0 <= time < 10.0),
        '10s <= t < 50s': sum(1 for time in times if 10.0 <= time < 50.0),
        '50s <= t': sum(1 for time in times if time >= 50.0),
    }

    filtered_counts = {category: count for category, count in counts.items() if count > 0}

    total = sum(filtered_counts.values())

    percentages = [count / total * 100 for count in filtered_counts.values()]

    colors = [style.green, style.yellow, style.orange, style.light_red, style.red]

    plt.figure(figsize=(5, 5))
    wedges, texts, autotexts = plt.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors,
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 1})

    plt.title('Time (s) per iteration distribution')

    plt.legend(wedges, counts.keys(), loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.show()