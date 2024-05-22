import matplotlib.pyplot as plt
import matplotlib as mpl
import styles.plt_style as style
import styles.colors as color
import pandas as pd
import seaborn as sns

mpl.rcParams.update(mpl.rcParamsDefault)
plt.style.use(style.plt_style)

mpl.rcParams['font.size'] = style.plt_font_size
mpl.rcParams['font.family'] = style.plt_font_style


def metrics_report(title, scores, colors):

    df = pd.DataFrame(scores)

    print("\n", title)
    print()
    print(df)

    df.plot(kind='bar', color=colors, figsize=(10, 5))
    plt.title(title)
    plt.ylabel('')
    plt.xlabel('')
    plt.xticks(rotation=0)
    plt.legend(title='Model', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.show()


def display_pie_chart(cosine_similarities):
    labels = ['>0.9', '0.7-0.9', '0.5-0.7', '0.3-0.5', '0-0.3']
    very_high_similarity_count = (cosine_similarities > 0.9).sum()
    high_similarity_count = ((cosine_similarities > 0.7) & (cosine_similarities <= 0.9)).sum()
    medium_similarity_count = ((cosine_similarities > 0.5) & (cosine_similarities <= 0.7)).sum()
    low_similarity_count = ((cosine_similarities > 0.3) & (cosine_similarities <= 0.5)).sum()
    very_low_similarity_count = (cosine_similarities <= 0.3).sum()

    sizes = [very_high_similarity_count, high_similarity_count,
             medium_similarity_count, low_similarity_count, very_low_similarity_count]

    colors = [color.o_1, color.o_2, color.o_3, color.o_4, color.o_5]

    plt.figure(figsize=(5, 5))
    wedges, texts, autotexts = plt.pie(sizes, autopct='%1.1f%%', startangle=140, colors=colors,
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 1})

    plt.title('Distribution of Cosine Similarity Scores')
    plt.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.show()


def layout(data_list, type):
    titles = ['% met', '% not met', '% no relevant information']

    custom_colors = [color.orange_base, color.red, color.green]

    fig, ax = plt.subplots(1, 3, figsize=(12, 6))

    for idx, data in enumerate(data_list):
        df_melted = pd.DataFrame([(key, value) for key, values in data.items() for value in values],
                                 columns=['Columns', 'Values'])

        sns.boxplot(x='Columns', y='Values', hue='Columns', data=df_melted, palette=custom_colors,
                    showfliers=False, ax=ax[idx], legend=False)
        ax[idx].set_title(titles[idx])
        ax[idx].set_xlabel('')
        ax[idx].set_ylabel('')

    fig.suptitle(f"Correlation between percentages and patient eligibility labels  ({type} criteria)", fontsize=14)
    plt.tight_layout()
    plt.show()
